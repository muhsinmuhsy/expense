from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
import app
from app.schemas import ExpenseCreate, ExpenseResponse
from app import models
from datetime import date

from sqlalchemy import extract

router = APIRouter(
    prefix="/expenses",
    tags=["expenses"],
)

@router.post("/", response_model=ExpenseResponse, status_code=201)
def create_expense(expense_data: ExpenseCreate, db: Session = Depends(get_db)):
    new_expense = models.Expense(**expense_data.dict())
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

@router.get("/", response_model=list[ExpenseResponse])
def get_expenses(db: Session = Depends(get_db)):
    return db.query(models.Expense).all()

@router.get("/month/{year}/{month}", response_model=list[ExpenseResponse])
def get_expenses_by_month(year: int, month: int, db: Session = Depends(get_db)):
    if month < 1 or month > 12:
        return {"error": "Invalid month. Please provide a value between 1 and 12."}
    return db.query(models.Expense).filter(
        extract('year', models.Expense.created_at) == year,
        extract('month', models.Expense.created_at) == month
    ).all()

@router.get("/category/{category}", response_model=list[ExpenseResponse])
def get_expenses_by_category(category: str, db: Session = Depends(get_db)):
    return db.query(models.Expense).filter(models.Expense.category == category).all()


@router.get("/day/{expense_date}", response_model=list[ExpenseResponse])
def get_expenses_by_day(expense_date: date, db: Session = Depends(get_db)):
    return db.query(models.Expense).filter(
        extract('year', models.Expense.created_at) == expense_date.year,
        extract('month', models.Expense.created_at) == expense_date.month,
        extract('day', models.Expense.created_at) == expense_date.day
    ).all()

@router.get("/week/{year}/{week_number}", response_model=list[ExpenseResponse])
def get_expenses_by_week(year: int, week_number: int, db: Session = Depends(get_db)):
    if week_number < 1 or week_number > 53:
        return {"error": "Invalid week number. Please provide a value between 1 and 53."}
    return db.query(models.Expense).filter(
        extract('year', models.Expense.created_at) == year,
        extract('week', models.Expense.created_at) == week_number
    ).all()
