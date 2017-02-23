import sqlite3
conn = sqlite3.connect("airline_seating.db")

# From the connection we get a cursor object.
cur = conn.cursor()

new_metrics_list = [1, 2]
with conn:
    cur.execute("UPDATE metrics SET passengers_refused=?, "
                "passengers_separated=?", (new_metrics_list[0],
                                           new_metrics_list[1]))
# refused = 2
# # with conn:
# #     cur.execute("UPDATE metrics SET passengers_refused=?", (2))
# with conn:
#     cur.execute("UPDATE metrics SET passengers_refused=? WHERE _rowid_=1", (2))