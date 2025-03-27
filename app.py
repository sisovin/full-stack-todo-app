import flet as ft
import sqlite3
import jwt
import argon2
import redis
from datetime import datetime, timedelta

class ToDoApp:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.cursor = self.conn.cursor()
        self.ph = argon2.PasswordHasher()
        self.redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
        self.jwt_secret = 'your_jwt_secret_key'
        self.init_ui()

    def init_ui(self):
        self.page = ft.Page()
        self.page.title = "To-Do Application"
        self.page.add(ft.Text("Welcome to the To-Do Application"))
        self.page.add(ft.TextField(label="Username", id="username"))
        self.page.add(ft.TextField(label="Password", id="password", password=True))
        self.page.add(ft.Button(text="Login", on_click=self.login))
        self.page.add(ft.Button(text="Signup", on_click=self.signup))
        self.page.add(ft.Button(text="Create Task", on_click=self.create_task))
        self.page.add(ft.Button(text="Read Tasks", on_click=self.read_tasks))
        self.page.add(ft.Button(text="Update Task", on_click=self.update_task))
        self.page.add(ft.Button(text="Delete Task", on_click=self.delete_task))
        self.page.add(ft.ListView(id="task_list"))
        self.page.update()

    def login(self, e):
        username = self.page.get_element("username").value
        password = self.page.get_element("password").value
        self.cursor.execute("SELECT password FROM users WHERE username=?", (username,))
        result = self.cursor.fetchone()
        if result and self.ph.verify(result[0], password):
            token = jwt.encode({'username': username, 'exp': datetime.utcnow() + timedelta(hours=1)}, self.jwt_secret, algorithm='HS256')
            self.redis_client.set(token, username)
            self.page.add(ft.Text(f"Login successful! Token: {token}"))
        else:
            self.page.add(ft.Text("Invalid username or password"))
        self.page.update()

    def signup(self, e):
        username = self.page.get_element("username").value
        password = self.page.get_element("password").value
        hashed_password = self.ph.hash(password)
        self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        self.conn.commit()
        self.page.add(ft.Text("Signup successful!"))
        self.page.update()

    def create_task(self, e):
        task = self.page.get_element("task").value
        self.cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        self.conn.commit()
        self.page.add(ft.Text("Task created!"))
        self.page.update()

    def read_tasks(self, e):
        self.cursor.execute("SELECT * FROM tasks WHERE deleted=0")
        tasks = self.cursor.fetchall()
        task_list = self.page.get_element("task_list")
        task_list.clear()
        for task in tasks:
            task_list.add(ft.Text(task[1]))
        self.page.update()

    def update_task(self, e):
        task_id = self.page.get_element("task_id").value
        new_task = self.page.get_element("new_task").value
        self.cursor.execute("UPDATE tasks SET task=? WHERE id=?", (new_task, task_id))
        self.conn.commit()
        self.page.add(ft.Text("Task updated!"))
        self.page.update()

    def delete_task(self, e):
        task_id = self.page.get_element("task_id").value
        self.cursor.execute("UPDATE tasks SET deleted=1 WHERE id=?", (task_id,))
        self.conn.commit()
        self.page.add(ft.Text("Task deleted!"))
        self.page.update()

if __name__ == "__main__":
    app = ToDoApp()
    ft.app(target=app.init_ui)
