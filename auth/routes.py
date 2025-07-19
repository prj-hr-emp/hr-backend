from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/login")
async def login(user: dict):
    email = user.get("email")
    password = user.get("password")
    if email == "admin@hr.com" and password == "admin123":
        return {"message": "Login successful", "role": "HR"}
    elif email.startswith("emp") and password == "emp123":
        return {"message": "Login successful", "role": "Employee"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@router.post("/register")
async def register(user: dict):
    return {"message": f"User {user.get('email')} registered successfully"}



