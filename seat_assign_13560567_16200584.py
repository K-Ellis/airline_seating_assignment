import sqlite3
import numpy as np
#todo-kieron get seating database name and csv name from the command line.
seating_database = "airline_seating.db"

# Connect to the database using sqlite2's .connect() method which returns a
# connection object.
conn = sqlite3.connect(seating_database)
# From the connection we get a cursor object.
cur = conn.cursor()

def create_zeros_array():
    with conn:
        cur.execute("SELECT * FROM rows_cols")

        rowscols = cur.fetchone()
        no_rows = rowscols[0]
        col_letters = rowscols[1]
    no_cols = 0
    col_letters_list =[]
    for letter in col_letters:
        no_cols += 1
        col_letters_list.append(letter)
    row_col_matrix = np.zeros((no_rows, no_cols))

    #want to return a 1s and zeros matrix
    return row_col_matrix, col_letters_list

zeros_array, col_letters_list = create_zeros_array()
# print(zeros_array.shape)


# todo-kieron fill in the 1s from the database file. Turn the ZerosMatrix into a
# ones_and_zeros matrix.

def find_occupied():
    with conn:
        cur.execute("SELECT * FROM seating")

        rows = cur.fetchall()

        for row in rows:
            if row[2]== "":
                pass
            else:
                for letter in col_letters_list:
                    if row[1] == letter:
                        # print(letter, col_letters_list.index(letter))
                        zeros_array[row[0]-1][col_letters_list.index(letter)] \
                                                                        = 1
                        # print(row[0])
                        # print(row[1])
                        # print(row[2])
    return zeros_array
binary_db = find_occupied()
print(binary_db)

# todo-kieron change the database file when a booking has been made. Using the
# ones_and_zeros matrix and booking name.

# todo-remi solve seating.
# When a booking is made, have to store the entries where the the seats are
# allocated so that the database can also be updated. Could create a new
# discardable zeros-only matrix, and update it with 1s too, and use it to update
# the sql database.
# Or store the booking name, row, and column letter in a separate list... and
# append the new bookings onto the end of the list. And use this list to update
# the database. I think this is probably a better idea.


# release the resources
conn.close()