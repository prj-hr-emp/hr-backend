from fastapi import APIRouter

router = APIRouter()

@router.get("/get/{emp_id}")
async def get_salary(emp_id: str):
    return {"emp_id": emp_id, "salary": "₹60,000"}

@router.post("/upload")
async def upload_salary(salary_data: dict):
    return {"message": "Salary uploaded", "data": salary_data}

