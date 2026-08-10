from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.db.database import get_connection

router = APIRouter(prefix="/auth", tags=["Authentication"])


class StudentLoginRequest(BaseModel):
    prn: str
    email: str


@router.post("/student/login")
def student_login(request: StudentLoginRequest):
    email = request.email.strip().lower()
    if not email.endswith("@sanjivani.edu.in"):
        raise HTTPException(
            status_code=400,
            detail="Please use your Sanjivani college email.",
        )

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
            (request.prn.strip(), email),
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
