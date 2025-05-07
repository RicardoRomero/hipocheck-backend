from typing import Optional
from datetime import datetime
from beanie import Document
from pydantic import EmailStr, Field
from uuid import UUID, uuid4

class User(Document):
    user_id: UUID = Field(default_factory=uuid4)
    username: str = Field(index=True, unique=True)
    email: EmailStr
    hashed_password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    disabled: Optional[bool] = None

    def __repr__(self) -> str:
        return f"<User {self.email}>"

    def __str__(self) -> str:
        return self.email

    def __hash__(self) -> int:
        return hash(self.email)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.email == other.email
        return False
    
    @property
    def create(self) -> datetime:
        if self.id:
            return self.id.generation_time
        return None

    @classmethod
    async def by_email(cls, email: str) -> "User":
        return await cls.find_one(cls.email == email)
    
    class Settings:
        name = "users"

async def insert_users():
    # Crear un usuario
    user1 = await User(
        username="usuario1",
        email="usuario1@example.com",
        hashed_password="hashedpassword1",
        first_name="Nombre1",
        last_name="Apellido1",
        disabled=False,
    ).insert()

    # Crear otro usuario
    user2 = await User(
        username="usuario2",
        email="usuario2@example.com",
        hashed_password="hashedpassword2",
        first_name="Nombre2",
        last_name="Apellido2",
        disabled=True,
    ).insert()

