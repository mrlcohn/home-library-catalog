import sqlite3

try:
    sqlite_client = sqlite3.connect('home_library_catalog.db')
    cursor = sqlite_client.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS book (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author_last TEXT NOT NULL,
            author_first TEXT NOT NULL,
            illustrator_last TEXT,
            illustrator_first TEXT,
            isbn INTEGER
        )
    ''')
    sqlite_client.commit()
    cursor.close()
except sqlite3.Error as error:
    print('Error occurred -', error)
finally:
    if sqlite_client:
        sqlite_client.close()
        print('SQLite client closed')