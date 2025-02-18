import sqlite3

with sqlite3.connect("saper.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS `users` (
        name TEXT,
        sex INTEGER,
        old INTEGER,
        scope INTEGER
    )""")

    # cur.execute("INSERT INTO users VALUES ('John', 1, 26, 243)")

    cur.execute("SELECT * FROM users")
    print(cur.fetchall())


    con.commit()