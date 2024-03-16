#!/usr/bin/python3

import MySQLdb
from sys import argv

username = argv[1]
password = argv[2]
database = argv[3]
stateName = argv[4]
c = 0

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
Execute function
"""

sql_query = "SELECT cities.name FROM cities \
        inner join states ON \
        states.id = cities.state_id WHERE states.name = %s"

cursor.execute(sql_query, (stateName,))

rows = cursor.fetchall()

for row in rows:
    if c > 0:
        print(", ", end="")
    print(row[0], end="")
    c += 1

print("")
cursor.close()
db.close()
