import sqlite3


def main():
    con = sqlite3.connect('words.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS movie(title, year, score)')
    res = con.execute("SELECT name FROM sqlite_master")
    print(res)


if __name__ == '__main__':
    main()
