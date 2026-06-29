import sqlite3

def create_database():
    with sqlite3.connect("air_users.db") as connection:
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            password TEXT
        )
        """)

def insert_user(name, age, gender, password):
    with sqlite3.connect("air_users.db") as connection:
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO users(name, age, gender, password)
        VALUES (?, ?, ?, ?)
        """, (name, age, gender, password))

def delete_user(user_id):
    with sqlite3.connect("air_users.db") as connection:
        cursor = connection.cursor()

        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))


def getdata_users():
    with sqlite3.connect("air_users.db") as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users")

        return cursor.fetchall()

    
if __name__ == "__main__":
    create_database()
    print(getdata_users())


