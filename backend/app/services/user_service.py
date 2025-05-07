from fastapi import HTTPException, status
from app.schemas.user_schema import UserAuth
from app.models.user_model import User
from app.core.security import get_password, verify_password
from typing import Optional
from uuid import UUID

class Userservice:
    
    @staticmethod
    async def create_user(user: UserAuth):
        existing_user = await User.find_one({"email": user.email})

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The email already exists."
            )

        user_in = User(
            username=user.username,
            email=user.email,
            hashed_password=get_password(user.password),
            first_name=user.first_name,
            last_name=user.last_name,
            disabled=False
        )

        await user_in.insert()

        return user_in
    
    @staticmethod
    async def authenticate(email: str, password: str) -> Optional[User]:
        user = await Userservice.get_user_by_email(email=email)
        if not user:
            return None
        if not verify_password(password=password, hashed_pass=user.hashed_password):
            return None
        return user

    @staticmethod
    async def get_user_by_email(email:str) -> Optional[User]:
        user = await User.find_one(User.email == email)
        return user

    @staticmethod
    async def get_user_by_id(id: UUID) -> Optional[User]:
        user = await User.find_one(User.user_id == id)
        return user