from fastapi import FastAPI

from .routers import clients, orders, reports

app = FastAPI(title="CRM API (minimal for QA tests)")

app.include_router(clients.router)
app.include_router(orders.router)
app.include_router(reports.router)

@app.get("/")
def root():
    return {"message": "CRM API running"}
