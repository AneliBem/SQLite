import sqlite3

with sqlite3.connect("saper.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE `users` (
        name TEXT,
        sex INTEGER,
        old INTEGER,
        scope INTEGER
    )""")