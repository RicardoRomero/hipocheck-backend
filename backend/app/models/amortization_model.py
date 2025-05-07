from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, Link
from pydantic import Field, BaseModel
from .user_model import User
from typing import List

class AmortizationTableInput(BaseModel):
    period: int
    outstanding_balance: float
    interest: float
    amortization: float
    monthly_payment: float
    # prepayment: float

class AmortizationDataInput(BaseModel):
    amortization_table: List[AmortizationTableInput] = []
    total_amortization_periods: int = 0
    total_amortization_monthlyPayments: float = 0
    percentage: float | None = None
    minimum_income: float = 0

class AmortizationInput(Document):
    amortization_id: UUID = Field(default_factory=uuid4)
    name: str
    property_purchase_price: float
    loan_amount: float
    credit_term: int
    interest_rate: float
    amortization_data: AmortizationDataInput = AmortizationDataInput()
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    owner: Link[User]

    def __repr__(self) -> str:
        return f"<AmortizationInput {self.name}, ID: {self.amortization_id}>"

    def __str__(self) -> str:
        return f"{self.name}"

    def __hash__(self) -> int:
        return hash(self.amortization_id)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, AmortizationInput):
            return self.amortization_id == other.amortization_id
        return False

    class Settings:
        name = "amortizations"