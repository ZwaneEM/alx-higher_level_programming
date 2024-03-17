#!/usr/bin/python3

"""
list all states with a name starting with 'N'
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ command line arguments """
    username = argv[1]
    password = argv[2]
    database = argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = conn.cursor()

    sql_query = "SELECT * FROM states WHERE states.name \
    LIKE 'N%' ORDER BY states.id ASC"
    cursor.execute(sql_query)

    rows = cursor.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)

    cursor.close()
    conn.close()
