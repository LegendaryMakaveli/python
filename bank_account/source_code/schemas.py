from pydantic import BaseModel, EmailStr
from decimal import Decimal

class AccountBase(BaseModel):
    first_name: str
    last_name: str
    address: str
    email: EmailStr
    phone_number: str
    bvn: str
    nin: str

class AccountCreate(AccountBase):
    pass

class AccountResponse(AccountBase):
    account_number: str
    balance: Decimal

    class Config:
        from_attributes = True
        

class TransactionRequest(BaseModel):
    amount: Decimal

class TransferRequest(BaseModel):
    sender_account_number: str
    receiver_account_number: str
    amount: Decimal
