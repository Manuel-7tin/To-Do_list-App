import tkinter as tk
from tkinter import messagebox
import json
import task_manager

tasks = task_manager.TaskManager()


def on_entry_click(event, entry_widget, default_text):
    print("Clicked on widget:", event.widget)
    if entry_widget.get() == default_text:
        entry_widget.delete(0, tk.END)
        entry_widget.config(fg='black')


def on_entry_leave(event, entry_widget, default_text):
    if entry_widget.get() == "":
        entry_widget.insert(0, default_text)
        entry_widget.config(fg='gray')


def store_info(window, info1_widget, info2_widget, password_placeholder):
    email = info1_widget.get()
    password = info2_widget.get()
    if "@" not in email or "." not in email or len(email) < 5:
        messagebox.showwarning(title="Email Error", message="This email is invalid")
        return
    if password == "" or password == password_placeholder:
        messagebox.showwarning(title="Password Error", message="This password is invalid")
        return
    info = {
        "email": email,
        "password": password,
    }
    with open(file="user_info.json", mode="w") as file:
        json.dump(obj=info, fp=file, indent=4)
    window.destroy()
    tasks.show_tasks()


def verify_user(window, user_input, password):
    if user_input == password:
        window.destroy()
        tasks.show_tasks()
    else:
        messagebox.showerror(title="Wrong Password", message=f"--{user_input}-- is an incorrect password")
        return


class AccessManager:

    def __init__(self):
        self.signing_FONT = ("bristone", 13, "bold")
        self.input_FONT = ("delicious heavy", 13, "normal")

    @staticmethod
    def logged_in():
        try:
            user_info = open(file="user_info.json", mode="r")
        except FileNotFoundError:
            return False
        else:
            user_info.close()
            return True

    def signing(self, signing_: str):
        condition = signing_
        if condition == "in":
            self.sign_in()
        elif condition == "up":
            self.sign_up()
        else:
            raise ValueError("User can only sign in or up")



    # @staticmethod
    def sign_in(self):
        viewport = tk.Tk()
        viewport.title("To_Do Manager")
        # viewport.geometry("350x500")
        viewport.config(pady=50, padx=50, background="#FFFFEF")
        with open(file="user_info.json", mode="r") as user_data:
            user_info = json.load(fp=user_data)

        message = tk.Label(text="Please sign in", font=self.signing_FONT)
        message.config(pady=25, background="#FFFFEF", foreground="#45458B")
        message.grid(row=0, column=0, columnspan=2)
        email_label = tk.Label(text="E-mail: ", font=self.input_FONT, background="#FFFFEF")
        email_label.grid(row=1, column=0, pady=5)
        password_label = tk.Label(text="Password: ", font=self.input_FONT, background="#FFFFEF")
        password_label.grid(row=2, column=0, pady=5)

        email_entry = tk.Entry(highlightthickness=1, highlightbackground="#45458B")
        email_entry.insert(tk.END, string=user_info["email"])
        email_entry.config(width=23)
        # email_entry.bind("<FocusIn>", lambda event: on_entry_click(event, email_entry, "Insert email address"))
        # email_entry.bind("<FocusOut>", lambda event: on_entry_leave(event, email_entry, "Insert email address"))
        email_entry.grid(row=1, column=1)

        password_entry = tk.Entry(highlightthickness=1, highlightbackground="#45458B")
        password_entry.insert(tk.END, string="Insert password")
        password_entry.config(fg='gray', width=23)
        password_entry.bind("<FocusIn>", lambda event: on_entry_click(event, password_entry, "Insert password"))
        password_entry.bind("<FocusOut>", lambda event: on_entry_leave(event, password_entry, "Insert password"))
        password_entry.grid(row=2, column=1)

        signin_button = tk.Button(command=lambda: verify_user(viewport, password_entry.get(), user_info["password"]))
        signin_button.config(text="Sign In", font=self.input_FONT, background="#7F7FFF", foreground="#FFFFEF")
        signin_button.grid(row=3, column=0, columnspan=2, pady=20)
        viewport.mainloop()

    def sign_up(self):
        viewport = tk.Tk()
        viewport.title("Task Manager")
        # viewport.geometry("350x500")
        viewport.config(pady=50, padx=50, background="#FFFFEF")

        message = tk.Label(text="Please sign up", font=self.signing_FONT)
        message.config(pady=25, background="#FFFFEF", foreground="#45458B")
        message.grid(row=0, column=0, columnspan=2)
        email_label = tk.Label(text="E-mail: ", font=self.input_FONT, background="#FFFFEF")
        email_label.grid(row=1, column=0, pady=5)
        password_label = tk.Label(text="Password: ", font=self.input_FONT, background="#FFFFEF")
        password_label.grid(row=2, column=0, pady=5)

        email_entry = tk.Entry(highlightthickness=1, highlightbackground="#45458B")
        email_entry.insert(tk.END, string="Insert email address")
        email_entry.config(fg='gray', width=23)
        email_entry.bind("<FocusIn>", lambda event: on_entry_click(event, email_entry, "Insert email address"))
        email_entry.bind("<FocusOut>", lambda event: on_entry_leave(event, email_entry, "Insert email address"))
        email_entry.grid(row=1, column=1)

        password_entry = tk.Entry(highlightthickness=1, highlightbackground="#45458B")
        password_entry.insert(tk.END, string="Insert password")
        password_entry.config(fg='gray', width=23)
        password_entry.bind("<FocusIn>", lambda event: on_entry_click(event, password_entry, "Insert password"))
        password_entry.bind("<FocusOut>", lambda event: on_entry_leave(event, password_entry, "Insert password"))
        password_entry.grid(row=2, column=1)

        signin_button = tk.Button(command=lambda: store_info(viewport, email_entry, password_entry, "Insert password"))
        signin_button.config(text="Sign Up", font=self.input_FONT, background="#7F7FFF", foreground="#FFFFEF")
        signin_button.grid(row=3, column=0, columnspan=2, pady=20)
        viewport.mainloop()
