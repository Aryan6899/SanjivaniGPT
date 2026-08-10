from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr

from app.db.database import get_connection

router = APIRouter(prefix="/auth", tags=["Authentication"])


class StudentLoginRequest(BaseModel):
    prn: str
    email: EmailStr


@router.post("/student/login")
def student_login(request: StudentLoginRequest):
    connection = get_connection()
    try:
        student = connection.execute(
            """
            SELECT s.prn, s.email, s.name, s.year, s.division, s.role,
                   d.code AS department_code, d.name AS department_name
            FROM students s
            JOIN departments d ON d.id = s.department_id
            WHERE LOWER(s.prn) = LOWER(?) AND LOWER(s.email) = LOWER(?)
            """,
            (request.prn.strip(), request.email.strip()),
        ).fetchone()
    finally:
        connection.close()

    if student is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid PRN or college email.",
        )

    return {
        "message": "Login successful",
        "student": dict(student),
    }


@router.get("/student/demo")
def demo_login_info():
    return {
        "prn": "DEMO-PRN-001",
        "email": "demo.student@sanjivani.edu.in",
    }
