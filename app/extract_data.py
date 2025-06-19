from app.model.student import Student
from app.model.subject import Subject
from app.model.grade import Grade
from collections import defaultdict

def extract_documents(session):
    docs = []
    students = session.query(Student).all()
    subjects = {s.id: s.name for s in session.query(Subject).all()}

    for student in students:
        grades = session.query(Grade).filter_by(student_id=student.id).all()
        if not grades:
            docs.append(f"Sinh viên {student.name} chưa có điểm.")
            continue
        for grade in grades:
            subject_name = subjects.get(grade.subject_id, "Không xác định")
            docs.append(f"Sinh viên {student.name} đạt {grade.score} điểm môn {subject_name}.")
    return docs


