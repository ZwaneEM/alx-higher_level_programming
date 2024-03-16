#!/usr/bin/python3
"""Script that list all states from the db"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
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
        db=base,
        charset="utf8"
    )

    cr = database.cursor()

    cr.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cr.fetchall()
    for row in rows:
        print(row)

    cr.close()
    database.close()
