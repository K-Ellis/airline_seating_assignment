import numpy as np
import sqlite3
import sys

#Connect to the database using sqlite2's .connect() method which returns a
#connection object
conn = sqlite3.connect("airline_seating.db")
#From the connection we get a cursor object
cur = conn.cursor()

#Prints all of the tables
with conn:
    #Tables names are stored in sqlite_master
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")

    list_of_tables = cur.fetchall()

    for table1 in list_of_tables:
        print(table1[0])
#The tables stored in airline_seating.db are: metrics, row_cols and seating

print()

#print out the info in metrics
with conn:
    cur.execute("SELECT * FROM metrics")

    rows = cur.fetchall()

    for row in rows:
        print(row)

print()

# print out the info in rows_cols
with conn:
    cur.execute("SELECT * FROM rows_cols")

    rows = cur.fetchall()

    for row in rows:
        print(row)

print()

# print out the info in seating
with conn:
    cur.execute("SELECT * FROM seating")

    rows = cur.fetchall()

    for row in rows:
        print(row)


#release the resources
conn.close()