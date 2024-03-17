#!/usr/bin/python3

"""
Lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ bash arguments """
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

    """ creation of cursor """

    cursor = conn.cursor()

    sql_query = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(sql_query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
