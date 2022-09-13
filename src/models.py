from locale import currency
from sqlalchemy import Column, Float, String, Integer, Date
from sqlalchemy.orm import relationship
from database import Base

# Class to represent currency value in specific date
class CurrencyValue(Base):
    __tablename__='currency_value'
    id = Column(Integer, primary_key= True, index=True)
    date = Column(String(20))
    currency_value = Column(Float)
    currency_id = Column(Integer)

# Class to represent currency
class Currency(Base):
    __tablename__ = 'currency'

    id = Column(Integer, primary_key= True, index=True)
    currency_name = Column(String,unique=True, index=True)


