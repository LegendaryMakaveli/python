from sqlalchemy.orm import Session
from . import models, schemas
import random
from decimal import Decimal
from fastapi import HTTPException




def generate_unique_account_number(db: Session) -> str:
    while True:
        account_number = "14" + str(random.randint(10**7, (10**8) - 1))
        existing = db.query(models.BankAccount).filter_by(account_number=account_number).first()
        if not existing:
            return account_number 

def create_account(db: Session, account: schemas.AccountCreate):
    account_number = generate_unique_account_number(db)

    db_account = models.BankAccount(
        first_name=account.first_name,
        last_name=account.last_name,
        address=account.address,
        email=account.email,
        phone_number=account.phone_number,
        bvn=account.bvn,
        nin=account.nin,
        account_number=account_number,
        balance=0.0
    )
    
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

def get_account_by_number(db: Session, account_number: str):
    return db.query(models.BankAccount).filter(models.BankAccount.account_number == account_number).first()

def get_all_accounts(db: Session):
    return db.query(models.BankAccount).all()



def deposit(db: Session, account_number: str, amount: Decimal):
    account = get_account_by_number(db, account_number)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Deposit amount must be positive")
    if amount > 500000:
        raise HTTPException(status_code=400, detail="Deposit limit exceeded (₦500,000 max)")

    account.balance += amount
    db.commit()
    db.refresh(account)
    return account


def withdraw(db: Session, account_number: str, amount: Decimal):
    account = get_account_by_number(db, account_number)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Withdrawal amount must be positive")
    if amount > account.balance:
        raise HTTPException(status_code=400, detail="Insufficient balance")

    account.balance -= amount
    db.commit()
    db.refresh(account)
    return account


def transfer(db: Session, sender_account_number: str, receiver_account_number: str, amount: Decimal):
    if sender_account_number == receiver_account_number:
        raise HTTPException(status_code=400, detail="Cannot transfer to the same account")

    sender = get_account_by_number(db, sender_account_number)
    receiver = get_account_by_number(db, receiver_account_number)

    if not sender:
        raise HTTPException(status_code=404, detail="Sender account not found")
    if not receiver:
        raise HTTPException(status_code=404, detail="Receiver account not found")

    if amount <= 0:
        raise HTTPException(status_code=400, detail="Transfer amount must be positive")

    if sender.balance < amount:
        raise HTTPException(status_code=400, detail="Insufficient funds")

    sender.balance -= amount
    receiver.balance += amount

    db.commit()
    db.refresh(sender)
    db.refresh(receiver)


    return {
        "message": f"Transfer of ₦{amount} from {sender_account_number} to {receiver_account_number} successful.",
        "sender_balance": float(sender.balance),
        "receiver_balance": float(receiver.balance),
    }

