#!/usr/bin/python3

"""
Takes in a name of a state as an argument and
lists all cities of that state
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ Command line arguments """
    username = argv[1]
    password = argv[2]
    database = argv[3]
    stateName = argv[4]

    """ Establish connection with database """
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    """ Cursor creation """
    cursor = conn.cursor()

    sql_query = "SELECT cities.name FROM cities INNER JOIN states ON \
    states.id = cities.state_id WHERE states.name = %s ORDER BY cities.id ASC"

    cursor.execute(sql_query, (stateName,))

    rows = cursor.fetchall()
    for row in range(len(rows)):
        if row > 0:
            print(", ", end="")
        print(rows[row][0], end="")
    print("")

    cursor.close()
    conn.close()
