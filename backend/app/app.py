from fastapi import FastAPI
from app.core.config import Settings
from beanie import init_beanie, Document
from motor.motor_asyncio import AsyncIOMotorClient

from app.models.user_model import User, insert_users
from app.models.amortization_model import AmortizationInput
from app.api.api_v1.router import router

app = FastAPI(
    title=Settings().PROJECT_NAME,
    openapi_url=f"{Settings().API_V1_STR}/openapi.json"
)

async def init():
    settings = Settings()
    client = AsyncIOMotorClient(
        {settings.MONGO_CONNECTION_STRING}
    )
    await init_beanie(database=client[settings.MONGO_DB], document_models=[User, AmortizationInput])

@app.on_event("startup")
async def app_startup():
    await init()
    # await insert_users()  # Asegúrate de utilizar 'await' aquí
    print("Beanie initialized and users inserted")

app.include_router(router, prefix=Settings().API_V1_STR)

