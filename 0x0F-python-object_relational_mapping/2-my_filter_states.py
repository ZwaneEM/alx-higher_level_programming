#!/usr/bin/python3

from sys import argv
import MySQLdb

username = argv[1]
password = argv[2]
database = argv[3]
searchName = argv[4]

"""
connecting to MySQL
"""

db = MySQLdb.connect(
    host='localhost',
    port=3306,
    user=username,
    passwd=password,
    db=database)

cursor = db.cursor()

"""
executing queries
"""

sql_query = "SELECT * FROM states WHERE name = '" \
        + searchName + "' ORDER BY id ASC"

cursor.execute(sql_query)

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
db.close()
