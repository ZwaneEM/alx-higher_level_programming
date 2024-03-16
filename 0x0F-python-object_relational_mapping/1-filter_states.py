#!/usr/bin/python3

from sys import argv
import MySQLdb

username = argv[1]
password = argv[2]
database = argv[3]

"""
connecting to MySQL
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
executing queries
"""

cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
db.close()
