from fastapi import APIRouter

router = APIRouter()

@router.get("/generate/{emp_id}")
async def generate_report(emp_id: str):
    return {"emp_id": emp_id, "report": "Performance and attendance report"}

