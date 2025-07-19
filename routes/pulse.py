from fastapi import APIRouter

router = APIRouter()

@router.get("/get/{emp_id}")
async def get_pulse(emp_id: str):
    return {"emp_id": emp_id, "pulse_score": 7.5}

@router.post("/update")
async def update_pulse(pulse_data: dict):
    return {"message": "Pulse score updated", "data": pulse_data}

