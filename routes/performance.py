from fastapi import APIRouter

router = APIRouter()

@router.get("/score/{emp_id}")
async def get_performance(emp_id: str):
    return {"emp_id": emp_id, "score": 88, "summary": "Excellent"}


