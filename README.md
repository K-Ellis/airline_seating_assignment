Airline Seating Allocation Algorithm
------------------------------------

Synopsis
--------
This is an algorithm to allocate seats when airline passengers make bookings.

For each flight a different plane seating configuration can be used. As
bookings come in, this algorithm will allocate seats to passengers. Each
booking will be for one or more passengers, and naturally bookings of
multiple passengers should be allocated seats together where possible.

The bookings will be provided in a CSV file where each line consists of one
integer representing the number of passengers in the party and one name, the
name of the person making the booking. Seats will be allocated in that name.

Seats will be allocated one booking at a time, in the order they come in. A
.db database file representing the seating plan of the aircraft, the empty
and occupied seats will be updated after each booking. When a booking can be
accommodated, seats will be allocated together if possible, but split up if
necessary. When a booking cannot be accommodated at all, because there are
too few free seats, seats will not be allocated for that booking.

After each booking has been processed (either allocated or refused) two
metrics in the database will be updated:
• a number representing how many passengers have been refused outright (this
is total passengers, not number of bookings that have been refused);
• and a number representing how many passengers are seated away from any
other member of their party.

A sample database and sample bookings file are available:
• airline_seating.db (5 KB) and
• bookings.csv (1.575 KB).

Deployment
----------
Users of this program will run it on the command line by typing:
"python seat_assign_13560567_16200584.py data.db bookings.csv"
where data.db is the name of an SQLite database and bookings.csv is a file
representing the bookings, one per line.

The program will also work with other database and bookings filenames as
given on the command line.

The program can also be run without specifying the database and bookings
filenames in the command line initial as the program will prompt the user to
either specify a database and booking filename or else ask the user if using
the sample database and bookings filenames is acceptable.

Authors
-------
Kieron Ellis and
Remi Paris.