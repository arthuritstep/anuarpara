from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str

class TransactionCreate(BaseModel):
    user_id: int
    amount: float