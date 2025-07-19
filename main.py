from fastapi import FastAPI
from backend.auth.routes import router as auth_router
from backend.routes.hr_dashboard import router as hr_dashboard_router
from backend.routes.employee_mgmt import router as employee_router
from backend.routes.salary import router as salary_router
from backend.routes.leaves import router as leaves_router
from backend.routes.performance import router as performance_router
from backend.routes.pulse import router as pulse_router
from backend.routes.reports import router as reports_router


app = FastAPI(title="HR Portal Backend")

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(hr_dashboard_router, prefix="/hr-dashboard", tags=["HR Dashboard"])
app.include_router(employee_router, prefix="/employees", tags=["Employee Management"])
app.include_router(salary_router, prefix="/salary", tags=["Salary"])
app.include_router(leaves_router, prefix="/leaves", tags=["Leaves"])
app.include_router(performance_router, prefix="/performance", tags=["Performance"])
app.include_router(pulse_router, prefix="/pulse", tags=["Pulse"])
app.include_router(reports_router, prefix="/reports", tags=["Reports"])

@app.get("/")
def root():
    return {"message": "HR Portal Backend Running!"}


