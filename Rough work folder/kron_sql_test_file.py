import sqlite3
#Connect to the database using sqlite2's .connect() method which returns a
#connection object
conn = sqlite3.connect("airline_seating_test.db")
#From the connection we get a cursor object
cur = conn.cursor()

#create a database with different name, dimensin, col letters

def create_db(rows, col_letters):
    cur.execute("CREATE TABLE metrics(passengers_refused INT, "
                "passengers_separated INT)")
    cur.execute("INSERT INTO metrics VALUES(0,0)")

    cur.execute("CREATE TABLE rows_cols(nrows INT,seats TEXT)")
    cur.execute("INSERT INTO rows_cols VALUES(?,?)", (rows, col_letters))

    cur.execute("CREATE TABLE seating(row INT, seat TEXT, name TEXT)")
    cur.execute("INSERT INTO seating VALUES(?,?)", (rows, col_letters))

def print_entries(name):
    # Prints all of the tables
    if name == "tables":
        with conn:
            #Tables names are stored in sqlite_master
            cur.execute("SELECT name FROM sqlite_master WHERE type='table'")

            list_of_tables = cur.fetchall()

            for table1 in list_of_tables:
                print(table1[0])
        #The tables stored in airline_seating.db are: metrics, row_cols and seating
    #print out the info in metrics
    elif name == "metrics":
        with conn:
            cur.execute("SELECT * FROM metrics")

            rows = cur.fetchall()

            for row in rows:
                print(row)
    # print out the info in rows_cols
    elif name == "rows_cols":
        with conn:
            cur.execute("SELECT * FROM rows_cols")

            rows = cur.fetchall()

            for row in rows:
                print(row)
    else:
        # print out the info in seating
        with conn:
            cur.execute("SELECT * FROM seating")

            rows = cur.fetchall()
            print(type(rows[0][0]))
            print(type(rows[0][1]))
            print(type(rows[0][2]))

            # for row in rows:
            #     print(row)
            print(len(rows))
            print(rows)
print_entries("seating")
#60 entries, two seats taken
# 1 A Donald Trump and 1 C Hilary Clinton
print_entries("rows_cols")
# 15*4
# A C D F
# 0 1 2 4
print_entries("metrics")
print_entries("tables")

conn.close()