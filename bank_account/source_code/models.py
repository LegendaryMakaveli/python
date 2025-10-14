from sqlalchemy import Column, Integer, String, Numeric
from .database import Base

class BankAccount(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone_number = Column(String, nullable=False)
    bvn = Column(String, nullable=False, unique=True)
    nin = Column(String, nullable=False, unique=True) 
    account_number = Column(String, nullable=False, unique=True)
    balance = Column(Numeric(10, 2), nullable=False, default=0.00)
