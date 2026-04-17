import sqlite3
import os
import secrets

# FIX 1: Remove hardcoded password (use environment variable)
DB_PASSWORD = os.getenv("DB_PASSWORD")

def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # FIX 2: Prevent SQL Injection (parameterized query)
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))

    return cursor.fetchall()

def generate_token():
    # FIX 3: Use secure random generator
    return str(secrets.randbelow(900000) + 100000)

# FIX 4: remove unused variables (so nothing extra like unused_count)

print(get_user('admin'))
print(generate_token())
