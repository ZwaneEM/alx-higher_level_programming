#!/usr/bin/python3
import MySQLdb
from sys import argv

username = argv[1]
password = argv[2]
base = argv[3]

"""
connect to server
"""
database = MySQLdb.connect(
    host='localhost',
    port=3306,
    user=username,
    passwd=password,
    db=base
)

cr = database.cursor()

"""
execute queries
"""

cr.execute("SELECT * FROM states ORDER BY id ASC")

rows = cr.fetchall()
for row in rows:
    print(row)

cr.close()
database.close()
