import sqlite3


def main():
    con = sqlite3.connect('words.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS movie(title, year, score)')

    data = [
        ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
        ("Monty Python's The Meaning of Life", 1983, 7.5),
        ("Monty Python's Life of Brian", 1979, 8.0),
    ]
    cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
    con.commit()
    res = con.execute("SELECT name FROM sqlite_master")
    print(res.fetchone)


if __name__ == '__main__':
    main()
