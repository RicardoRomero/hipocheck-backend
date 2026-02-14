from fastapi import HTTPException, status
from uuid import UUID
from typing import List
from app.models.user_model import User
from app.models.amortization_model import AmortizationInput
from app.schemas.amortization_schema import AmortizationCreate

class AmortizationService:
    @staticmethod
    async def list_amortizations(user: User) -> List[AmortizationInput]:
        amortizations = await AmortizationInput.find(AmortizationInput.owner.id == user.id).to_list()
        return amortizations
    
    @staticmethod
    async def create_amortization(user: User, data: AmortizationCreate) -> AmortizationInput:
        data_dict = data.dict()
        #calculate amortization
        periods = data_dict["credit_term"] * 12
        outstanding_balance = data_dict["loan_amount"]
        annual_interest = (data_dict["interest_rate"] / 12)/100
        interest = outstanding_balance * annual_interest
        denominator = 1 - ((1 + annual_interest) ** (-periods)) 
        monthly_payment = interest / denominator
        amortization = monthly_payment - interest
        #calculate minimum income
        percentage = (data_dict["amortization_data"]["percentage"]) / 100
        minimum_income= monthly_payment / percentage
        # prepayment = 0
        
        data_dict["amortization_data"] = {
            "amortization_table": [],
            "percentage": "{:.2f}".format(round(percentage, 2)),
            "minimum_income": "{:.2f}".format(round(minimum_income, 2)),
            "total_amortization_periods": periods,
            "total_amortization_monthlyPayments": "{:.2f}".format(round(monthly_payment * periods, 2))
        }

        for i in range(1, periods + 1):
            amortization_entry = {
                "period": i,
                "outstanding_balance":"{:.2f}".format(round(outstanding_balance, 2)),
                "interest": "{:.2f}".format(round(interest, 2)),
                "amortization": "{:.2f}".format(round(amortization, 2)),
                "monthly_payment": "{:.2f}".format(round(monthly_payment, 2)),
                # "prepayment": prepayment
            }

            outstanding_balance = outstanding_balance - amortization
            interest = outstanding_balance * annual_interest
            amortization = monthly_payment - interest
            data_dict["amortization_data"]["amortization_table"].append(amortization_entry)
        
        
        amortization = AmortizationInput(**data_dict, owner=user)
        return await amortization.insert()

    @staticmethod
    async def retrieve_amortization(current_user: User, amortization_id: UUID):
        try:
            amortization = await AmortizationInput.find_one(
                {"amortization_id": amortization_id, "owner": {"$ref": "users", "$id": current_user.id}}
            )
            if amortization:
                return amortization
            else:
                raise HTTPException(status_code=404, detail=f"Document not found for amortization_id: {amortization_id}")

        except Exception as e:
            raise HTTPException(status_code=404, detail=f"Document not found for amortization_id: {amortization_id} and user: {current_user.id}")
    
    @staticmethod
    async def delete_amortization(current_user: User, amortization_id: UUID):
        amortization = await AmortizationService.retrieve_amortization(current_user, amortization_id)
        if amortization:
            await amortization.delete()

            return None