import sqlite3
import numpy as np
# todo-kieron turn a sql database into an array

def sql_to_array(database):
    # Connect to the database using sqlite2's .connect() method which returns a
    # connection object
    conn = sqlite3.connect(database)
    # From the connection we get a cursor object
    cur = conn.cursor()
    with conn:
        cur.execute("SELECT * FROM rows_cols")

        rowscols = cur.fetchone()
        no_rows = rowscols[0]
        col_letters = rowscols[1]

    # release the resources
    no_cols = 0
    for letter in col_letters:
        no_cols += 1
    row_col_matrix = np.zeros((no_rows, no_cols))


    conn.close()
    #want to return a 1s and zeros matrix
    return row_col_matrix
row_col_matrix = sql_to_array("airline_seating.db")
print(row_col_matrix.shape)


# todo-remi solve seating


