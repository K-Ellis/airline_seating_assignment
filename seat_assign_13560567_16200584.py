import sqlite3
import numpy as np
import sys
import os

# Can run through the command line with:
# python seat_assign_13560567_16200584.py airline_seating.db bookings.csv

# Alternatively can also run the program without specifying a seating
# database and bookings file name initially.


def check_args(command_args):
    # Checks if command line arguments are present, and if not, collects
    # input and output file names. Checks if input files exist.

    # Initialize blank file names list
    file_names = []

    # Loop until there are 2 entries in the file names list (one database and
    # one bookings) or until the user exits.
    while len(file_names) != 2:
        # If there is only 1 command line argument (
        # 'seat_assign_13560567_16200584.py') and no file names:
        if len(command_args) == 1:
            # Ask the user to define database and bookings file names
            question = input('Would you like to define a seating database and '
                             'bookings filename? [y/n]: ').upper()
            # If the user wants to enter file names:
            if question == 'Y':
                # Append database and bookings file names to the file name list
                file_names.append(input("Please enter a seating database file "
                                        "name: "))
                file_names.append(input("Please enter a bookings file name: "))
            # If the user doesn't want to enter file names:
            elif question == 'N':
                # Asks the user if they want to use the default file names
                if input('Is using the default file names ok? [y/n]: '
                         ).upper() == 'Y':
                    # Append default file names to the file name list
                    file_names.append('airline_seating.db')
                    file_names.append('bookings.csv')
                # If not, ask to exit
                else:
                    # If user elects to exit
                    question = input('Would you like to exit? [y/n]: ').upper()
                    if question == 'Y':
                        # Exit
                        exit("User exit. No update to database file.")
                    # If not:
                    elif question == "N":
                        # Restart loop
                        continue
                    else:
                        # Exit
                        exit("Sorry, only [y/n] accepted. Exiting program. No "
                             "update to database file. ")

            # If user answers neither Y or N
            else:
                # If the user wants to try again
                question = input('Looks like an error. Would you like to '
                                 'try again?  [y/n]: ').upper()
                if question == 'Y':
                    # Restart loop
                    continue
                elif question == 'N':
                    exit("User exit. No update to database file.")
                # If the user wants to exit
                else:
                    # Exit
                    exit("Sorry, only [y/n] accepted. Exiting program. No  "
                         "update to database file. ")

        # If 2 command line arguments are given,
        # 'seat_assign_13560567_16200584.py' and another:
        elif len(command_args) == 2:
            # Ask the user to define database and bookings file names
            question = input('Sorry, you need to enter two valid file '
                             'names. '
                             'Would you like to define a seating database and '
                             'bookings filename? [y/n]: ').upper()
            # If the user wants to enter file names:
            if question == 'Y':
                # Append file names to the file name list
                file_names.append(input("Please enter a seating database file "
                                        "name: "))
                file_names.append(input("Please enter a bookings file name: "))
            # If the user doesn't want to enter file names:
            elif question == 'N':
                # Asks the user if they want to use the default file names
                if input('Is using the default file names ok? [y/n]: '
                         ).upper() == 'Y':
                    # Append default file names to the file name list
                    file_names.append('airline_seating.db')
                    file_names.append('bookings.csv')
                # If not, ask to exit
                else:
                    # If user elects to exit
                    question = input('Would you like to exit? [y/n]: ').upper()
                    if question == 'Y':
                        # Exit
                        exit("User exit. No update to database file.")
                    # If not:
                    elif question == "N":
                        # Restart loop
                        continue
                    else:
                        # Exit
                        exit("Sorry, only [y/n] accepted. Exiting program. No "
                             "update to database file. ")
            # If user answers neither Y or N
            else:
                # If the user wants to try again
                question = input('Looks like an error. Would you like to try '
                                 'again?  [y/n]: ').upper()
                if question == 'Y':
                    # Restart loop
                    continue
                elif question == 'N':
                    exit("User exit. No update to database file.")
                # If the user wants to exit
                else:
                    # Exit
                    exit("Sorry, only [y/n] accepted. Exiting program. No "
                         "update to database file. ")
        # If three commands are given, 'seat_assign_13456456_16200584.py',
        # seating database file name, and bookings file name
        elif len(command_args) == 3:
            # Append the given file names to the file names list
            file_names.append(command_args[1])
            file_names.append(command_args[2])
        # In all other circumstances, use first two arguments as file names
        else:
            # Append the given file names to the file names list
            file_names.append(command_args[1])
            file_names.append(command_args[2])

        # Check given file names are real files that can be opened
        if not check_file_exists(file_names[0]):
            # If not, prompt the user to try again
            question = input("I can't find that database file. Would you "
                             "like to try again? [y/n]: ").upper()
            if question == 'Y':
                # Restart loop
                file_names = []
                continue
            # If the user does not want to try again
            elif question == "N":
                # Exit
                exit("User exit. No update to database file.")
            else:
                exit("Sorry, only [y/n] accepted. Exiting program. No "
                     "update to database file. ")
        elif not check_file_exists(file_names[1]):
            # If not, prompt the user to try again
            question = input("I can't find that bookings file. Would you "
                             "like to try again? [y/n]: ").upper()
            if question == 'Y':
                # Restart loop
                file_names = []
                continue
            # If the user does not want to try again
            elif question == "N":
                # Exit
                exit("User exit. No update to database file.")
            else:
                exit("Sorry, only [y/n] accepted. Exiting program. No "
                     "update to database file. ")

        # todo-kieron write function to check that the database file is .db
                # and the bookings file is .csv
        if not check_file_name(file_names):
            question = input("Sorry your file names are either too short or "
                             "not in the correct format. Would you like to "
                             "try  again? [y/n]: ").upper()
            if question == 'Y':
                # Restart loop
                file_names = []
                continue
            # If the user does not want to try again
            elif question == "N":
                # Exit
                exit("User exit. No update to database file.")
            else:
                exit("Sorry, only [y/n] accepted. Exiting program. No "
                     "update to database file. ")

    # Return file names
    return file_names[0], file_names[1]


def check_file_exists(filename):
    # Return True if the file exists in the directory
    return os.path.isfile(filename)


def check_file_name(file_names_list):
    if len(file_names_list[0]) > 3 and len(file_names_list[1]) > 4:
        if file_names_list[0][-3:] == ".db" and file_names_list[1][-4:] ==  \
                ".csv":
            return True
        else:
            return False
    else:
        return False

seating_database, bookings = check_args(sys.argv)
# print(seating_database, bookings)

# Connect to the database using sqlite2's .connect() method which returns a
# connection object.
conn = sqlite3.connect(seating_database)
# From the connection we get a cursor object.
cur = conn.cursor()


def create_zeros_array():
    with conn:
        cur.execute("SELECT * FROM rows_cols")

        rows_cols_list = cur.fetchone()
        no_rows = rows_cols_list[0]
        col_letters = rows_cols_list[1]
    no_cols = 0
    list_of_col_letters = []
    for letter in col_letters:
        no_cols += 1
        list_of_col_letters.append(letter)
    row_col_matrix = np.zeros((no_rows, no_cols))

    # want to return a 1s and zeros matrix
    return row_col_matrix, list_of_col_letters

zeros_array, col_letters_list = create_zeros_array()
# print(zeros_array.shape)


def find_occupied():
    with conn:
        cur.execute("SELECT * FROM seating")

        rows = cur.fetchall()

        for row in rows:
            if row[2] == "":
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

# todo-Kieron change the database file when a booking has been made. Using the
# ones_and_zeros matrix and booking name.

# todo-Remi solve seating.
# When a booking is made, have to store the entries where the the seats are
# allocated so that the database can also be updated. Could create a new
# discardable zeros-only matrix, and update it with 1s too, and use it to
# update the sql database.
# Or store the booking name, row, and column letter in a separate list... and
# append the new bookings onto the end of the list. And use this list to update
# the database. I think this is probably a better idea.


# release the resources
conn.close()
