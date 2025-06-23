from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

prompt_template = """
Bạn là một trợ lý thông minh. Hãy trả lời câu hỏi dựa trên các thông tin trong tài liệu được cung cấp. 
Nếu không có thông tin, bạn có thể suy luận dựa trên kiến thức của mình.Hãy trả lời bằng tiếng việt nhé và không cần nhắc lại câu hỏi

Câu hỏi: {question}
Dữ liệu:
{context}

Trả lời:
"""

prompt = PromptTemplate(template=prompt_template, input_variables=["question", "context"])

class RagService:
    def __init__(self):
        self.qa_chain = None
        self.embeddings = None
        self.llm = None
        self.last_faiss_modified = 0

    def load_model(self):
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.llm = ChatGroq(
            api_key=GROQ_API_KEY,
            model_name="llama3-70b-8192"
        )
        if os.path.exists("faiss_index"):
            self.load_qa_chain()

    def load_qa_chain(self):
        vector_store = FAISS.load_local(
            "faiss_index", 
            self.embeddings, 
            allow_dangerous_deserialization=True
        )
        retriever = vector_store.as_retriever(search_kwargs={"k": 30})
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=retriever,
            chain_type="stuff",
            chain_type_kwargs={"prompt": prompt}
        )
    def reload_if_faiss_updated(self):
        faiss_path = "faiss_index/index.faiss"
        if os.path.exists(faiss_path):
            last_modified = os.path.getmtime(faiss_path)
            if last_modified > self.last_faiss_modified:
                self.last_faiss_modified = last_modified
                self.load_qa_chain()
    def ask(self, query: str) -> str:
        self.reload_if_faiss_updated()
        if not self.qa_chain:
            raise ValueError("QA chain chưa được khởi tạo. Vui lòng gọi load_model() trước.")
        result = self.qa_chain.invoke({"query": query})
        answer = result.get("result", "Không thể trả lời câu hỏi này.")
        return answer.replace("\n", " ").strip()


rag_service = RagService()
