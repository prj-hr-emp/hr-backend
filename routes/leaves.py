from fastapi import APIRouter

router = APIRouter()

@router.post("/apply")
async def apply_leave(leave_data: dict):
    return {"message": "Leave applied successfully", "data": leave_data}

@router.get("/status/{emp_id}")
async def leave_status(emp_id: str):
    return {"emp_id": emp_id, "status": "Approved"}

