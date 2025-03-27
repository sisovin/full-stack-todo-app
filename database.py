import sqlite3

def create_connection():
    conn = sqlite3.connect('todo.db')
    return conn

def initialize_database():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            deleted INTEGER DEFAULT 0
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            deleted INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def create_task(task):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
    conn.commit()
    conn.close()

def read_tasks():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE deleted=0')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def update_task(task_id, new_task):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET task=? WHERE id=?', (new_task, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET deleted=1 WHERE id=?', (task_id,))
    conn.commit()
    conn.close()

def signup_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

def login_user(username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM users WHERE username=?', (username,))
    result = cursor.fetchone()
    conn.close()
    return result

def soft_delete_user(username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET deleted=1 WHERE username=?', (username,))
    conn.commit()
    conn.close()
