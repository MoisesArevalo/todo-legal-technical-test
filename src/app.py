from unicodedata import name
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import utility, models, schema
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/currency/")
async def create_currency(currency: schema.Currency, db: Session = Depends(get_db)):
    # Search currency, if exist not create again.
    db_currency = utility.get_currency(db, currency_name=currency.name)
    if db_currency:
        raise HTTPException(status_code=400, detail="Currency already registered")
    return utility.create_currency(db=db, currency=currency)

@app.post("/currency/value")
async def create_currency(currency: schema.CurrencyValue, db: Session = Depends(get_db)):
    # Search currency by name, if exists, to create referencial value.
    db_currency = utility.get_currency(db, currency_name=currency.name)
    if db_currency:
        return utility.create_currency_value(db,currency, db_currency.id )
    
    raise HTTPException(status_code=400, detail="Currency not exists")

@app.get('/currency/{currency_name}')
async def getcurrency(currency_name, db: Session = Depends(get_db)):
    # Search currency by name
    return utility.get_currency(db, currency_name=currency_name.upper())

@app.get('/currency/value/{currency_name}')
async def get_currency_value(currency_name:str, date:str, db: Session = Depends(get_db)):
    # Search currency by name, if exists, search referencial value by current_id and date.
    db_currency = utility.get_currency(db, currency_name=currency_name.upper())

    if db_currency:
        return utility.get_currency_value(db,date, db_currency.id )
    return {"detail":"Currency not exists"}
