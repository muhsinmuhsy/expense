from  datetime import datetime
from sqlalchemy import Float, Integer, String, DateTime
from .database import Base
from sqlalchemy.orm import Mapped, mapped_column


class Expense(Base):
    __tablename__ = "expenses"

    expense_id : Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name : Mapped[str] = mapped_column(String(255))
    amount : Mapped[float] = mapped_column(Float)
    category : Mapped[str] = mapped_column(String(255))
    created_at : Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class Salary(Base):
    __tablename__ = "salaries"

    salary_id : Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    amount : Mapped[float] = mapped_column(Float)
    created_at : Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)