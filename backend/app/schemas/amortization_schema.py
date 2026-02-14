from datetime import datetime
from typing import List
from uuid import UUID
from pydantic import BaseModel, validator

from app.models.amortization_model import AmortizationDataInput

class AmortizationDataCreate(BaseModel):
    percentage: float

    @validator("percentage")
    def validate_percentage(cls, value):
        if value not in (20, 30) or value <= 0:
            raise ValueError("The 'percentage' property must have a value of 30 or 20.")
        return value

class AmortizationCreate(BaseModel):
    name: str
    property_purchase_price: float
    loan_amount: float
    credit_term: int
    interest_rate: float
    amortization_data: AmortizationDataCreate
    
    @validator("property_purchase_price")
    def validate_property_purchase_price(cls, value, values):
        if value < 0 or (values.get("loan_amount") is not None and value < values["loan_amount"]):
            raise ValueError("The property 'property_purchase_price' must be greater than or equal to 'loan_amount' and greater than 0.")
        return value

    @validator("loan_amount")
    def validate_loan_amount(cls, value):
        if value <= 0:
            raise ValueError("The 'loan_amount' property must be greater than 0.")
        return value

    @validator("credit_term")
    def validate_credit_term(cls, value):
        if value <= 0 or value >= 31:
            raise ValueError("The 'credit_term' property must be greater than 0 and equal to or less than 30.")
        return value
    
    @validator("interest_rate")
    def validate_interest_rate(cls, value):
        if value <= 0 or value > 100:
            raise ValueError("The 'interest_rate' property must be greater than 0.00 and less than or equal to 100.00.")
        return value
    

    
class AmortizationOutput(BaseModel):
    amortization_id: UUID
    name: str
    property_purchase_price: float
    loan_amount: float
    credit_term: int
    interest_rate: float
    amortization_data: AmortizationDataInput
    created_at: datetime
    updated_at: datetime



