from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from decimal import Decimal

from .database import engine, SessionLocal
from . import models, crud, schemas


app = FastAPI(title="Makaveli Bank API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # your frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


models.BankAccount.metadata.create_all(bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create-account", response_model=schemas.AccountResponse)
def create_account(account: schemas.AccountCreate, db: Session = Depends(get_db)):
    db_account = crud.create_account(db, account)
    return db_account


@app.get("/accounts", response_model=list[schemas.AccountResponse])
def list_accounts(db: Session = Depends(get_db)):
    return crud.get_all_accounts(db)


@app.get("/accounts/{account_number}", response_model=schemas.AccountResponse)
def get_account(account_number: str, db: Session = Depends(get_db)):
    db_account = crud.get_account_by_number(db, account_number)
    if not db_account:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account


@app.post("/deposit/{account_number}")
def deposit(account_number: str, payload: schemas.TransactionRequest, db: Session = Depends(get_db)):
    """Deposit money into an account"""
    try:
        account = crud.deposit(db, account_number, payload.amount)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": f"Deposit of ₦{payload.amount} successful.",
                "account_number": account.account_number,
                "new_balance": str(account.balance),
            },
        )
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/withdraw/{account_number}")
def withdraw(account_number: str, payload: schemas.TransactionRequest, db: Session = Depends(get_db)):
    """Withdraw money from an account"""
    try:
        account = crud.withdraw(db, account_number, payload.amount)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": f"Withdrawal of ₦{payload.amount} successful.",
                "account_number": account.account_number,
                "new_balance": str(account.balance),
            },
        )
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/transfer")
def transfer(payload: schemas.TransferRequest, db: Session = Depends(get_db)):
    """Transfer money between two accounts"""
    try:
        result = crud.transfer(
            db,
            payload.sender_account_number,
            payload.receiver_account_number,
            payload.amount,
        )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=result,
        )
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
