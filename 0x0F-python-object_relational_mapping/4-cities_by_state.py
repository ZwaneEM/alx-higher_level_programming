#!/usr/bin/python3

"""
lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ command line arguments """
    username = argv[1]
    password = argv[2]
    database = argv[3]

    """connect to the database """
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    """ creating a cursor """
    cursor = conn.cursor()

    sql_query = ("SELECT cities.id, cities.name, states.name \
    FROM cities INNER JOIN\
     states ON states.id = cities.state_id ORDER BY cities.id ASC")

    cursor.execute(sql_query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
