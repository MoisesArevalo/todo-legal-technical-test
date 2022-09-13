
from locale import currency
from pydantic import BaseModel

# Schema to represent Currency
class Currency(BaseModel):
    name: str

# Schema to represent Currency value
class CurrencyValue(BaseModel):
    date: str 
    value: float
    name: str

    