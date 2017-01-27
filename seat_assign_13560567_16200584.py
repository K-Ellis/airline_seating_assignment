import sqlite3
import numpy as np
import sys
import os
from operator import itemgetter

# Can run through the command line with:
# python seat_assign_13560567_16200584.py airline_seating.db bookings.csv

# Alternatively can also run the program without specifying a seating
# database and bookings file name initially.


# A function to check that the command line arguments are present, and if
# not, collects input and output file names. Checks if input files exist and
# are valid using check_file_names() and check_files_exist() which are
# defined later.
def check_args(command_args):
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


# A function to check that the files exist in the directory
def check_file_exists(filename):
    # Return True if the file exists in the directory
    return os.path.isfile(filename)


# A function to check that the seating database and bookings file names have
# the correct extensions. Also checks that the file names are greater than
# zero in length (i.e. they are one or more characters long).
def check_file_name(file_names_list):
    if len(file_names_list[0]) > 3 and len(file_names_list[1]) > 4:
        if file_names_list[0][-3:] == ".db" and file_names_list[1][-4:] ==  \
                ".csv":
            return True
        else:
            return False
    else:
        return False


# A function to create an m*n zeros numpy array that has the same dimensions
#  as the airline seating plane.
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


# A function which gets the information from the "metrics" table in the
# database. Returns a list which contains: the number of passengers refused
# and the number of passengers seated away from their party.
def get_metrics():
    with conn:
        cur.execute("SELECT * FROM metrics")
        metrics_list = cur.fetchone()
        no_refused = metrics_list[0]
        no_seated_away = metrics_list[1]
    metrics_list = [no_refused, no_seated_away]
    return metrics_list


# A function to search through the seating table and update the  m*n zeros
# array with 1's where ever a seat is occupied.
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


# A function to update the seating database with the new booking information.
# new_booking must be a list of lists in the form (for two seats):
# [[row number, column letter, name], [row number, column number, name]]
#
# or for one booking/seat:
# [[row number, column letter, name]]
#
# So it has to be a list inside a list!
def update_db(new_booking, new_metrics):
    for i1 in range(len(new_booking)):
        with conn:
            cur.execute("UPDATE seating SET name=? WHERE row=? and seat=?",
                        (next_new_booking[i1][2], next_new_booking[i1][0],
                         next_new_booking[i1][1]))
    with conn:
        cur.execute("UPDATE metrics SET passengers_refused=?, "
                    "passengers_separated=?", (new_metrics[0], new_metrics[1]))


# save the seating database and bookings file names.
seating_database, bookings = check_args(sys.argv)

# Connect to the database using sqlite2's .connect() method which returns a
# connection object.
conn = sqlite3.connect(seating_database)

# From the connection we get a cursor object.
cur = conn.cursor()

# Cave the m*n zeros array and the column letters in a list.
zeros_array, col_letters_list = create_zeros_array()

# Convert the empty zeros array into a ones and zeros array, with ones being
# present where ever a seat is occupied
binary_db = find_occupied()
print(binary_db)
print(type(binary_db))
# get the initial metrics from the database
initial_metrics_list = get_metrics()


# -----------------------------------------------------------------------------
# Testing that the database successfully updates:
next_new_booking = [[1, "A", "Kieron Ellis"], [1, "C", "Remi Paris"]]

# update_db() works for one booking or multiple bookings, eg:
# next_new_booking = [[1, "A", "Celine Dione"]]

# Define a metrics list
new_metrics_list = [0, 0]
# new_metrics_list = [10, 5]

# update the database with the booking info and metric list
update_db(next_new_booking, new_metrics_list)

# Print out the seating database - for testing purposes
with conn:
    cur.execute("SELECT * FROM seating")
    seating_bookings = cur.fetchall()
    print(seating_bookings)

    cur.execute("SELECT * FROM metrics")
    metrics = cur.fetchall()
    print(metrics)


# -----------------------------------------------------------------------------


# When a booking is made, save the entries where the the seats are
# allocated in a list so that the database can also be updated. So store the
# booking name, row, and column letter in a separate list called
# "next_new_booking".
#
# After solving the seating for each line in the csv file,  this list initialises
# again (start with an empty list for each booking) and  the new bookings are appended
# in this format: row number, column letter and booking name. A fresh list
# after every booking makes updating the database easier! :)
#
# The function  "update_db()" will take each entry in this list
# ("next_new_booking") and update the database accordingly.
#
# The column letters are stored in a list called "col_letters_list".For the
# sample database, "airline_seating.db" it is in the form ['A', 'C', 'D', 'F'].
# Use the col_letters_list's indices to convert to and from column numbers and
# column letters in order to store these letters in the list
# "next_new_booking".
#
#  The "new_metrics_list" is incremented after every booking
#  This list is in the form [number of passengers refused,
#  number of passengers seated away from another member# of their party].
#
#
# So the "next_new_booking" list needs to only contain the information from
# the current booking (no information from previous bookings).
#
# And the "new_metrics_list" needs to be a running tally of the metrics
# (have to add on the new metrics to the old metrics).



# Read the Ones and Zeros matrix and convert it into an array composed of  1 row and n columns.
# n represents the total number of seats (binary_db.size)


reshapedplane = binary_db.reshape((1,  binary_db.size))


# Result_list classifies in lists of tuples the number of consecutive available or unavailable seats.
# (0,n) indicates that n seats are available, (1,m) indicates that m seats are occupied
result_list = []
for x in binary_db:

    current = x[0]
    count = 0
    for value in x:
        if value == current:
            count += 1
        else:
            result_list.append((int(current), count))
            current = value
            count = 1

    result_list.append((int(current), count))
print(result_list)
# Read the bookings
import itertools

bookings = np.genfromtxt('bookings.csv', dtype=None, delimiter=',')
new_booking = []
for y in bookings:

    partysize = list(y)
    # We identify the position of consecutive seats available that match the required partysize
    b = next((x for x in result_list if x[0] == 0 and x[1] >= partysize[1]), None)
        # If the number of consecutive avaialable seats is smaller than the partysize...
    if b == None:
        #...And if the partysize can fit into the plane...
        if sum([x[1] for x in result_list if x[0] == 1]) + partysize[1] <= binary_db.size:
            # ...We allocate a seat to each passenger of the party, irrespectively of the party (s)he belongs to.
            #In other words, passengers can be seated away from other member of the party.
            for _ in itertools.repeat(None, partysize[1]):
                #c is the next available seat
                c = next(x for x in result_list if x[0] == 0)

                c_position = result_list.index(c)

                c_sum_position = sum([x[1] for x in result_list[:c_position]])

                #Counts the number of passengers seated away from other member of the party
                new_metrics_list[1] += 1


                new_booking.append([c_sum_position + 1, partysize[0]])
                reshapedplane[0, c_sum_position] = 1

                # The result_list which classifies in lists of tuples the number of consecutive available or unavailable seats has to be updated.
                result_list = []
                reshapedplane = reshapedplane.reshape(binary_db.shape)
                for x in reshapedplane:

                    current = x[0]
                    count = 0
                    for value in x:
                        if value == current:
                            count += 1
                        else:
                            result_list.append((int(current), count))
                            current = value
                            count = 1

                    result_list.append((int(current), count))

                    reshapedplane = reshapedplane.reshape((1,  binary_db.size))


        #This is the case when there are too few seats available. So passengers are refused.
        else:
            new_metrics_list[0] += 1

    #In all other cases, we can allocate enough consecutive seats to match the partysize. So that passengers are seated next to other members of the party.
    else:

        b_position = result_list.index(b)
        b_sum_position = sum([x[1] for x in result_list[:b_position]])


        for k, l in enumerate(range(partysize[1])):
            new_booking.append([b_sum_position + (k + 1), partysize[0]])

        reshapedplane[0, b_sum_position:(b_sum_position + partysize[1])] = 1

    # The result_list which classifies in lists of tuples the number of consecutive available or unavailable seats has to be updated.

    result_list = []
    reshapedplane = reshapedplane.reshape(binary_db.shape)
    for x in reshapedplane:

        current = x[0]
        count = 0
        for value in x:
            if value == current:
                count += 1
            else:
                result_list.append((int(current), count))
                current = value
                count = 1

        result_list.append((int(current), count))

        reshapedplane = reshapedplane.reshape((1,  binary_db.size))

    # We sort the new_booking list by the number of seat
    new_booking = sorted(new_booking, key=itemgetter(0))

#This loop creates None items in the new_booking list to represent the seats which were already asssigned based on the initial database.
for k in range(1, binary_db.size):
    if (next((x for x in new_booking if x[0] == k), None)) == None:
        new_booking.append([k, b'None'])
    new_booking = sorted(new_booking, key=itemgetter(0))

#M_new_booking is used to  transform new_booking  which has the shape [[seat number, name]] into
#next_new_booking  which has the shape [[row number, column letter, name]]
M_new_booking = []


NoneCheckList=list(x[1] for x in new_booking for x in new_booking)
#The test below checks if the plane is full before processing further.
if all(item == b'None' for item in NoneCheckList):
    print('This plane is full')

else:
    phi = 1
    for k in range(1, binary_db.shape[0] + 1):
        for j in range(len(col_letters_list)):


            M_new_booking.append([k, col_letters_list[j], list(x[1] for x in new_booking if x[0] == phi + j)[0].decode('UTF-8')])

        phi += len(col_letters_list)
#next_new_booking eventually includes the name of the passengers asscoiated with their seat number.
next_new_booking = list(x for x in M_new_booking if x[2] != 'None')
print(next_new_booking)
print(new_metrics_list)
update_db(next_new_booking, new_metrics_list)

# release the resources
conn.close()
