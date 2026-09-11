from fastapi import FastAPI
from app.database import engine, Base
from app.routers import expense, totals

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Exp manage Application",
    version="1.0.0",
)

app.include_router(expense.router)
app.include_router(totals.router)


@app.get("/")
def root():
    return {"message": "Welcome to the Exp manage Application!"}