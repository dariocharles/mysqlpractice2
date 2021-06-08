import os
import datetime
import pymysql

# Get the username from the Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')
try:
    with connection.cursor() as cursor:
        list_of_names = ['fred', 'fred']
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings), list_of_names)
        connection.commit() 



        # list_of_names = ['fred', 'Fred']
        # format_strings = ','.join(['%s'] * len(list_of_names))
        # cursor.execute(
        #     "DELETE FROM Friends WHERE name in ({});".format(format_strings),
        #     list_of_names)
        # connection.commit()
        
        # DELETE
    # 1.
    # rows = cursor.execute("DELETE FROM Friends WHERE name = 'bob';")
        # connection.commit()
    # 2.
    # rows = cursor.execute("DELETE FROM Friends WHERE name = %s;", 'bob')
        # connection.commit()
    # 3.
    # rows = cursor.executemany("DELETE FROM Friends WHERE name = %s;", ['bob', 'jim'])
        # connection.commit()
    # # 4. 
    #  list_of_names = ['fred', 'Fred']
    #     format_strings = ','.join(['%s'] * len(list_of_names))
    #     cursor.execute(
    #         "DELETE FROM Friends WHERE name in ({});".format(format_strings),
    #         list_of_names)
    #     connection.commit()

# UPDATE
        # 1.
        # cursor.execute("UPDATE Friends SET age = 94 WHERE name = 'jim';")
        # connection.commit
        # 2
        # cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;",
                        # (45, 'fred'))
        # 3 - use executemany using a tuple
        # rows = [(33, 'bob'),
        #         (33, 'jim'),
        #         (33, 'fred')]
        # cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;", rows)
        # connection.commit()

# CREATE

        # cursor.execute("""CREATE TABLE IF NOT EXISTS
                     #   Friends(name char(20), age int, DOB datetime);""")

# INSERT

# 1
        #  row = ("Bob", 21, "1990-02-06 23:04:56")
        # cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        # connection.commit()
# 2
        # rows = [("bob", 21, "1990-02-06 23:04:56"),
        #         ("jim", 56, "1955-05-09 13:12:45"),
        #         ("fred", 100, "1911-09-12 01:01:01")]
        # cursor.executemany("INSERT INTO Friends VALUES (%s,%s,%s);", rows)
        # connection.commit()

finally:
    connection.close()




