from fastapi import APIRouter

router = APIRouter()

@router.get("/get_all_employees")
async def get_all_employees():
    return {"employees": ["emp1", "emp2", "emp3"]}

@router.get("/search_employee/{emp_id}")
async def search_employee(emp_id: str):
    return {"employee_id": emp_id, "name": "Sample Employee", "status": "Active"}

