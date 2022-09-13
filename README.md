## Technical test
For sql database:
* Type: relational
* SqlLite
* Squema that I used.
![alt sql-squema](/docs/sql.png "Sql Squema")

For web service:
* Language: python
* Framework: fastAPI
* Logic diagram proposed:

![alt web service diagram](/docs/WS.png "WS diagram")
## Instructions:
<br>
1. Install all dependencies (I used python 3.10)

`pip install -r requirements.txt`
<br>2. Run service with:

`uvicorn app:app --port 1234 --reload `
### Actions enables:
#### To add new data:
<br>
- currency 

POST: /currency

{
    "name":""
}

- currency value

POST: /currency/value

{
    "date":"",
    "value":"",
    "name":""
}

#### To get data
<br>
- currency

GET: /currency/value/{currency_name}

example: /currency/value/eur

- unique currency value

GET: /currency/value/currency_name?date=dd/mm/yyyy

example: /currency/value/eur?date=09/09/2022{id}

- all currency value

GET: /currency/value/all/currency_name?date=dd/mm/yyyy

example: /currency/value/all/eur?date=09/09/2022{id}

