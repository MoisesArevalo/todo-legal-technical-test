## Technical test
For sql database:
* Type: relational
* SqlLite
* Squema that I used.

For web service:
* Language: python
* Framework: fastAPI
* Logic diagram proposed:

## Instructions:
<br>
To migrate sql database, please run the next cli-command:

`python migrate ....`

### Actions enables:
To add new data:
<br>
POST: api/v1/
{
    "value",
    "local-currency",
    "foreign-currency"
}

To get data
<br>
GET: /api/v1/{id}

