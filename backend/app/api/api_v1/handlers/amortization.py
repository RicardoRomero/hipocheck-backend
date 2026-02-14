from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends
from app.models.user_model import User
from app.api.deps.user_deps import get_current_user
from app.schemas.amortization_schema import AmortizationOutput, AmortizationCreate
from app.services.amortization_service import AmortizationService
from app.models.amortization_model import AmortizationInput

amortization_router = APIRouter()

@amortization_router.get('/', summary="Get all amortizations of the user", response_model=List[AmortizationOutput])
async def list_amortizations(current_user: User = Depends(get_current_user)):
    return await AmortizationService.list_amortizations(current_user) 

@amortization_router.post('/create', summary="Create an Amortization", response_model=AmortizationInput)
async def create_amortization_handler(data: AmortizationCreate, current_user: User = Depends(get_current_user)):
    return await AmortizationService.create_amortization(current_user, data)

@amortization_router.get('/{amortization_id}', summary="Get a amortization by amortization_id", response_model=AmortizationOutput)
async def retrieve(amortization_id: UUID, current_user: User = Depends(get_current_user)):
    return await AmortizationService.retrieve_amortization(current_user, amortization_id)

@amortization_router.delete('/{amortization_id}', summary=" Delete a amortization by id")
async def delete(amortization_id: UUID, current_user: User = Depends(get_current_user)):
    await AmortizationService.delete_amortization(current_user, amortization_id)
    return None

