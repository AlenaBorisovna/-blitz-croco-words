import sqlite3


def main():
    # Устанавливаем соединение с базой данных SQLite
    con = sqlite3.connect('words.db')
    # Создаем объект курсора для выполнения SQL-запросов
    cur = con.cursor()
    cur.executemany()
    # Создаем таблицу movie с колонками title, year и score
    cur.execute('CREATE TABLE IF NOT EXISTS movie(title, year, score)')

    # Создаем список данных
    data = [
        ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
        ("Monty Python's The Meaning of Life", 1983, 7.5),
        ("Monty Python's Life of Brian", 1979, 8.0),
    ]
    # Используем executemany для вставки всех данных за один запрос
    cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
    # Сохраняем изменения в базе данных
    con.commit()

def add_data(con: sqlite3.Connection, name: str, data_dict: {str,str}):


if __name__ == '__main__':
    main()
