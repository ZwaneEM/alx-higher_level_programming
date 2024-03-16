#!/usr/bin/python3

import MySQLdb
from sys import argv

username = argv[1]
password = argv[2]
database = argv[3]


"""
Connect to the database
"""

db = MySQLdb.connect(
    host='localhost',
    port=3306,
    user=username,
    passwd=password,
    db=database
    )

cursor = db.cursor()

"""
Execute queries
"""

sql_query = "select cities.id, cities.name, \
        states.name from cities \
        inner join states on cities.state_id = states.id;"

cursor.execute(sql_query)

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
db.close()
