dbfile1 = "airline_seating.db"
dbfile2 = "airline_seating.dba"
bookings1 = "bookings.csv"
bookings2 = "bookings.cs"
dbfile3 = ".db"
bookings3 = ".csv"

example1 = [dbfile1, bookings1]
example2 = [dbfile1, bookings2]
example3 = [dbfile2, bookings1]
example4 = [dbfile2, bookings2]
example5 = [dbfile3, bookings3]

example6 = [bookings1, dbfile1]
example7 = [bookings2, dbfile1]
example8 = [bookings1, dbfile2]
example9 = [bookings2, dbfile2]
example10 = [bookings3, dbfile3]

def check_file_name(filenames_list):
    print(filenames_list)
    if len(filenames_list[0]) > 3 and len(filenames_list[1]) > 4:
        if filenames_list[0][-3:] == ".db" and filenames_list[1][-4:] ==  \
                ".csv" :
            return True
        else:
            return False
    else:
        return False

print(check_file_name(example10))