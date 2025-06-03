from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import select
from app.model.student import Student
from app.schemas.student_schema import StudentCreate, StudentRead, StudentUpdate
from app.db.database import create_db_and_tables, get_session

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/students/", response_model=StudentRead)
def create_student(student: StudentCreate, session=Depends(get_session)):
    db_student = Student.from_orm(student)
    session.add(db_student)
    session.commit()
    session.refresh(db_student)
    return db_student

@app.get("/students/", response_model=list[StudentRead])
def list_students(session=Depends(get_session)):
    students = session.exec(select(Student)).all()
    return students

@app.get("/students/{student_id}", response_model=StudentRead)
def get_student(student_id: int, session=Depends(get_session)):
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{student_id}", response_model=StudentRead)
def update_student(student_id: int, updated: StudentUpdate, session=Depends(get_session)):
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    update_data = updated.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(student, key, value)
    session.commit()
    session.refresh(student)
    return student

@app.delete("/students/{student_id}")
def delete_student(student_id: int, session=Depends(get_session)):
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    session.delete(student)
    session.commit()
    return {"ok": True}
