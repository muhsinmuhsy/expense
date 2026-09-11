from  datetime import datetime
from pydantic import BaseModel, Field

class ExpenseCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    amount: float = Field(ge=0)
    category: str = Field(min_length=1, max_length=255)



class ExpenseResponse(ExpenseCreate):
    expense_id: int
    created_at: datetime

    model_config = {
        "from_attributes": True,
    }
class SalaryCreate(BaseModel):
    amount: float = Field(ge=0)

class SalaryResponse(SalaryCreate):
    salary_id: int
    created_at: datetime

    model_config = {
        "from_attributes": True,
    }