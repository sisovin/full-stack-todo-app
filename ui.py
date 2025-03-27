import flet as ft

class FormUI:
    def __init__(self, page):
        self.page = page
        self.form = ft.Column()
        self.page.add(self.form)

    def add_text_field(self, label, id, password=False):
        text_field = ft.TextField(label=label, id=id, password=password)
        self.form.add(text_field)

    def add_button(self, text, on_click):
        button = ft.Button(text=text, on_click=on_click)
        self.form.add(button)

    def animate_form(self):
        self.form.animate(ft.Animation(duration=500, curve=ft.Curves.ease_in_out))

class TaskUI:
    def __init__(self, page):
        self.page = page
        self.task_list = ft.ListView(id="task_list")
        self.page.add(self.task_list)

    def display_tasks(self, tasks):
        self.task_list.clear()
        for task in tasks:
            self.task_list.add(ft.Text(task))
        self.page.update()

    def handle_task_interaction(self, task_id, action):
        if action == "delete":
            # Call delete task function
            pass
        elif action == "update":
            # Call update task function
            pass
