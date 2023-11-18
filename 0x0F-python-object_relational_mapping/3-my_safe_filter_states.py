#!/usr/bin/python3
"""Defines a MySQLdb database connection """

import MySQLdb

from sys import argv

if __name__ == '__main__':

    """Established db connection"""
    connection = MySQLdb.connect(
            host='localhost',
            user=argv[1],
            port=3306,
            password=argv[2],
            database=argv[3]
    )

    """create a cursor object"""
    my_cursor = connection.cursor()

    """Execute an sql query"""
    if argv[4] != "'" or argv[4] != "*":
        my_cursor.execute(
           """SELECT * FROM states WHERE states.name
           LIKE '{}' ORDER BY states.id ASC""".format(argv[4]))

        """Fetch results"""
        my_data = my_cursor.fetchall()

        """print results"""
        for data in my_data:
            print(data)

    """Close cursor and connection"""
    my_cursor.close()
    connection.close()
