import sqlite3
from password_manager.manager import User

DATABASE_FILE = "password_manager.db"

def create_table():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')

    conn.commit()
    conn.close()

def save_credentials(user):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                   (user.username, user.password))

    conn.commit()
    conn.close()

def credentials_exist():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]

    conn.close()

    return count > 0

def verify_credentials(username, password):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = cursor.fetchone()

    conn.close()

    return result is not None

def encrypt(password):
    ...

def decrypt(password):
    ...