#!/usr/bin/python3

"""
takes an argument and displays all values in the
states table of the database where name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ command line arguments """
    username = argv[1]
    password = argv[2]
    database = argv[3]
    nameSearch = argv[4]

    """ Establish the connection to database """
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    """ Cursor creation """
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM states WHERE states.name LIKE '{:s}' \
    ORDER BY states.id ASC".format(nameSearch))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
