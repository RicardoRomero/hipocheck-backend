from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field, validator
import re

class UserAuth(BaseModel):
    email: EmailStr = Field(..., description="user email")
    username: str = Field(..., min_length=5, max_length=50, description="user username")
    password: str
    @validator("password")
    def validate_password(cls, value):
        # Asegurar que la contraseña cumple con ciertos criterios
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*(),.?\":{}|<>])", value):
            raise ValueError("The password does not meet the security criteria. It should be at least 8 characters long, include both uppercase and lowercase letters, contain at least one number, and use special characters such as !@#$%^&*(),.?:{}|<>. Please ensure that your password adheres to these guidelines for enhanced security.")
        return value
    first_name: str = Field(..., min_length=2, max_length=24)
    last_name: str = Field(..., min_length=2, max_length=24)

class UserOut(BaseModel):
    user_id: UUID
    username: str
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    disabled: Optional[bool] = None