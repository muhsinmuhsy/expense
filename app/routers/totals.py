from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
import app
from app.schemas import SalaryCreate, SalaryResponse
from app import models
from datetime import date

from sqlalchemy import extract, func

router = APIRouter(
    prefix="/salaries",
    tags=["salaries"],
)

@router.post("/", response_model=SalaryResponse, status_code=201)
def create_salary(salary_data: SalaryCreate, db: Session = Depends(get_db)):
    new_salary = models.Salary(**salary_data.dict())
    db.add(new_salary)
    db.commit()
    db.refresh(new_salary)
    return new_salary


@router.get("/total", response_model=dict)
def get_total_salary(db: Session = Depends(get_db)):
    total_expense = db.query(func.sum(models.Expense.amount)).scalar() or 0
    total_salary = db.query(func.sum(models.Salary.amount)).scalar() or 0
    remaining_amount = total_salary - total_expense
    return {
        "total_expense": total_expense,
        "total_salary": total_salary,
        "remaining_amount": remaining_amount
    }
    