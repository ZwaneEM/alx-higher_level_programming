#!/usr/bin/python3

from sys import argv
import MySQLdb

if __name__ == "__main__":
    """
    connecting to MySQL
    """

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
        )

    cursor = db.cursor()

    """
    executing queries
    """

    cursor.execute("SELECT * FROM states WHERE \
            name LIKE 'N%' ORDER BY id ASC")

    rows = cursor.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)

    cursor.close()
    db.close()
