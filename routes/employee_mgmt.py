from fastapi import APIRouter, HTTPException
from backend.database.db import get_connection


router = APIRouter()

@router.get("/employees")
def get_employees():
    conn = get_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection failed")

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    conn.close()
    return employees


