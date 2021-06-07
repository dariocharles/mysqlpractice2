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
        # 1
        # cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'bob';")
# OR CAN DO IT LIKE THIS 
        # 2
        # cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;",
                    #    (23, 'bob'))
        # 3 - use executemany using a tuple
        rows = [(23, 'bob'),
                (24, 'jim'),
                (25, 'fred')]
        cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;",
                           rows)


        connection.commit()
finally:
    connection.close()




# ----------------------------------------------------------

# INSERT Informtation - Can insert a single one not in a tuple
# 
# try:
#     with connection.cursor() as cursor:
#         rows = [("bob", 21, "1990-02-06 23:04:56"),
#                 ("jim", 56, "1955-05-09 13:12:45"),
#                 ("fred", 100, "1911-09-12 01:01:01")]
#         cursor.executemany("INSERT INTO Friends VALUES (%s,%s,%s);", rows)
            # executemany when doing a tuple for updating more than one or else use execute to update one
#         connection.commit()
# finally:
#     connection.close()

# -----------------------------------------------------

# Create Friends table
# 
# try:
#     with connection.cursor() as cursor:
#         cursor.execute("""CREATE TABLE IF NOT EXISTS
#                           Friends(name char(20), age int, DOB datetime);""")
#         # Note that the above will still display a warning (not error) if the
#         # table already exists
# finally:
#     connection.close()