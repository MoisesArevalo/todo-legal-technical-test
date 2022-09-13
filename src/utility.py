from sqlalchemy.orm import Session
import models, schema
"""
Function to get currency from database
    - db: enable session db
    - currency_name: Name of currency to search
    return: Currency object.
"""
def get_currency(db:Session, currency_name:str):
    print('++',currency_name)
    return db.query(models.Currency).filter(models.Currency.currency_name==currency_name).first()

"""
Function to get last currencyvalue from database
first time simulate a external consult
    - db: enable session db
    - date: date to filter currency value
    - currency_id: id of currency to search
    return: CurrencyValue object.
"""
def get_currency_value(db:Session, date:str, currency_id):
    # Simulation to external webhook
    import requests, os
    from dotenv import load_dotenv
    load_dotenv()
    # get url from enviroment file
    url= os.getenv('WEBHOOK')
    data = {
        'local':'USD',
        'foreign':'EUR',
        'date':'13-09-2022',
        'value':1233
    }
    # get info using get method
    response = requests.get(('%s/local=%s&foreign=%s&date=%s&value=%i'%(url,data['local'],data['foreign'], data['date'],data['value'])))
    if response.status_code==200:
        print('response Ok with get')
    # get info using post method
    response = requests.post(url,data)
    if response.status_code==200:
        print('response Ok with post')
    # return value from database 
    return db.query(models.CurrencyValue).filter(models.CurrencyValue.currency_id==currency_id, models.CurrencyValue.date == date).first()

"""
Function to get all currencyvalue from database 
    - db: enable session db
    - date: date to filter currency value
    - currency_id: id of currency to search
    return: CurrencyValue object.
"""
def get_all_currency_value(db:Session, date:str, currency_id):
    
    return db.query(models.CurrencyValue).filter(models.CurrencyValue.currency_id==currency_id, models.CurrencyValue.date == date).all()

"""
Function to create_currency from database
    - db: enable session db
    - currency: Currency object schema to insert.
    return: Currency model.
"""
def create_currency(db: Session, currency: schema.Currency):
    new_currency = models.Currency(currency_name=currency.name)
    print('++'*20)
    db.add(new_currency)
    db.commit()
    db.refresh(new_currency)
    return new_currency

"""
Function to create_currency from database
    - db: enable session db
    - currency: CurrencyValue object schema to insert.
    - currency_id: id of currency to relation.
    return: CurrencyValue model.
"""
def create_currency_value(db: Session, currency: schema.CurrencyValue, currency_id: int):
    db_currency = models.CurrencyValue(date= currency.date , currency_value=currency.value, currency_id=currency_id )
    db.add(db_currency)
    db.commit()
    db.refresh(db_currency)
    return db_currency