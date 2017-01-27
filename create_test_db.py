import sqlite3
#create a database with different name, dimensin, col letters
def create_db(rows, cols, col_letters, col_letters_list, db_name):
    conn = sqlite3.connect(db_name)
    # From the connection we get a cursor object
    cur = conn.cursor()
    with conn:
        cur.execute("CREATE TABLE metrics(passengers_refused INT, "
                    "passengers_separated INT)")
        cur.execute("INSERT INTO metrics VALUES(?,?)",(1,0))

        cur.execute("CREATE TABLE rows_cols(nrows INT,seats TEXT)")
        cur.execute("INSERT INTO rows_cols VALUES(?,?)", (rows, col_letters))

        cur.execute("CREATE TABLE seating(row INT, seat TEXT, name TEXT,  "
                    "PRIMARY KEY (row, seat))")
        for i in range(rows):
            for j in range(cols):
                cur.execute("INSERT INTO seating VALUES(?,?,?)", (i,
                                                   col_letters_list[j], None))
        print(db_name)
        print("Done")
    conn.close()
# create_db(2, 5, "ABCDE", ["A","B","C","D","E"], "test_2by5.db")
create_db(2000, 10, "ABCDEFGHIJ", ["A","B","C","D","E","F","G","H","I","J"],
          "test_2000by10.db")