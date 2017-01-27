import sqlite3
#Connect to the database using sqlite2's .connect() method which returns a
#connection object


#create a database with different name, dimensin, col letters

def create_db(rows, cols, col_letters, col_letters_list, db_name):
    conn = sqlite3.connect(db_name)
    # From the connection we get a cursor object
    cur = conn.cursor()
    cur.execute("CREATE TABLE metrics(passengers_refused INT, "
                "passengers_separated INT)")
    cur.execute("INSERT INTO metrics VALUES(?,?)",(1,0))

    cur.execute("CREATE TABLE rows_cols(nrows INT,seats TEXT)")
    cur.execute("INSERT INTO rows_cols VALUES(?,?)", (rows, col_letters))

    cur.execute("INSERT INTO rows_cols VALUES(?,?)", (1,"aa"))
    # cur.execute("CREATE TABLE seating(row INT, seat TEXT, name TEXT, PRIMARY KEY (row, seat))")
    # cur.execute("INSERT INTO seating VALUES(?,?,?)", (0, "a", "b"))

    # for i in range(rows):
    #     for j in range(cols):
    #         cur.execute("INSERT INTO seating VALUES(?,?,?)", (i,
    #                                                           col_letters_list[j], "y"))

    print("Done.")
    conn.close()
create_db(2, 5, "ABCDE", ["A","B","C","D","E"], "airline_seating_test.db")

# release the resources
