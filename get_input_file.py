import sys
import os
# Can run through the command line with:
# python get_input_file.py airline_seating.db bookings.csv

# Alternatively can also run the program without specifying a seating
# database and bookings file name initially.
def check_CM_args(cmArgs):
    # Checks if command line arguments are present, and if not, collects
    # input and output file names. Checks if input files exist.

    # Initialize blank file names list
    file_names = []

    # Loop until there are 2 entries in the file names list (one database and
    # one bookings) or until the user exits.
    while len(file_names) != 2:
        # If there is only 1 command line argument (
        # 'seat_assign_13560567_16200584.py') and no file names:
        if len(cmArgs) == 1:
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
                question = input('Looks like an error. Would you like to try '
                         'again?  [y/n]: ').upper()
                if  question == 'Y':
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
        elif len(cmArgs) == 2:
            # Ask the user to define database and bookings file names
            question = input('Sorry, you have only entered one file name. '
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
        elif len(cmArgs) == 3:
            # Append the given file names to the file names list
            file_names.append(cmArgs[1])
            file_names.append(cmArgs[2])
        # In all other circumstances, use first two arguments as file names
        else:
            # Append the given file names to the file names list
            file_names.append(cmArgs[1])
            file_names.append(cmArgs[2])

        # Check given file names are real files that can be opened
        if not check_file_exists(file_names[0]):
            # If not, prompt the user to try again
            if input("I can't find that file. Would you like to try "
                     "again? [y/n]: ").upper() == 'Y':
                # Restart loop
                file_names = []
                continue
            # If the user does not want to try again
            else:
                # Exit
                exit("User exit. No update to database file.")
        elif not check_file_exists(file_names[1]):
            # If not, prompt the user to try again
            if input("I can't find that file. Would you like to try "
                     "again? [y/n]: ").upper() == 'Y':
                # Restart loop
                file_names = []
                continue
            # If the user does not want to try again
            else:
                # Exit
                exit("User exit. No update to database file.")
    # Return file names
    return file_names[0], file_names[1]

def check_file_exists(filename):
    # Return True if the file exists in the directory
    return os.path.isfile(filename)

seating_database, bookings = check_CM_args(sys.argv)
print(seating_database, bookings)
