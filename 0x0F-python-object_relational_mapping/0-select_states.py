#!/usr/bin/python3
"""Script that list all states from the db"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """
    connect to server
    """
    database = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )

    cr = database.cursor()

    cr.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cr.fetchall()
    for row in rows:
        print(row)

    cr.close()
    database.close()
