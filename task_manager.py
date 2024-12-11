import json
import tkinter as tk
import task_creator


class TaskManager:

    def __init__(self):
        self.head_FONT = ("adobe caslon pro bold", 13, "normal")
        self.open_head_FONT = ("adobe caslon pro bold", 25, "normal")
        self.input_FONT = ("myriad pro light", 13, "normal")
        self.open_input_FONT = ("myriad pro light", 11, "normal")
        try:
            tasks_id = open(file="task_id.txt", mode="r")
            self.task_id = int(tasks_id.read())
        except FileNotFoundError:
            tasks_id = open(file="task_id.txt", mode="w")
            tasks_id.write("0")
            self.task_id = 0
        finally:
            tasks_id.close()

    def add_task_ui(self,  fm_window):
        # fm_window.destroy()
        viewport = tk.Tk()
        # viewport = tk.Toplevel(root)
        viewport.title("Create Task")
        viewport.config(pady=20, padx=20, background="#FFFFEF")

        title_label = tk.Label(viewport, text="Title:", font=self.input_FONT, background="#FFFFEF")
        title_label.grid(row=0, column=0, pady=5)
        title_entry = tk.Entry(viewport, highlightthickness=3)
        title_entry.grid(row=0, column=1, pady=5)

        desc_label = tk.Label(viewport, text="Description:", font=self.input_FONT, background="#FFFFEF")
        desc_label.grid(row=1, column=0, pady=5)
        desc_entry = tk.Text(viewport, height=5, width=20, highlightthickness=3)
        desc_entry.grid(row=1, column=1, pady=5)

        save_btn = tk.Button(viewport, command=lambda: self.add_task(fm_window, viewport, title_entry, desc_entry))
        save_btn.config(text="Save", font=self.input_FONT, background="#7F7FFF", foreground="#FFFFEF")
        save_btn.grid(row=2, column=0, columnspan=2, pady=5)

        cancel_button = tk.Button(viewport, text="Cancel", command=lambda: self.close_viewport(viewport))
        cancel_button.config(background="red", foreground="white")
        # cancel_button.grid(row=3, column=3, pady=10)
        viewport.mainloop()

    def add_task(self, fm,  viewport, title_entry, desc_entry):
        print(f"task id is {self.task_id}")
        self.task_id += 1
        task = task_creator.Task(title=title_entry.get(), description=desc_entry.get("1.0", tk.END))
        if task.title == "" or task.title == " ":
            task.title = "Nothing"
        if task.description == "\n" or task.description == " \n":
            task.description = "Nothing"
        new_task = {
            self.task_id: {
                "title": task.title,
                "desc": task.description,
                "date": task.date,
                "time": task.time
            }
        }
        try:
            with open(file="tasks.json", mode="r") as task_list:
                tasks = json.load(fp=task_list)
                tasks.update(new_task)
        except FileNotFoundError:
            with open(file="tasks.json", mode="w") as task_list:
                json.dump(obj=new_task, fp=task_list, indent=4)
        else:
            with open(file="tasks.json", mode="w") as task_list:
                json.dump(obj=tasks, fp=task_list, indent=4)
        finally:
            with open(file="tasks.json", mode="r") as task_list:
                tasks = json.load(fp=task_list)
                print(tasks)
            with open(file="task_id.txt", mode="w") as tasks_id:
                tasks_id.write(str(self.task_id))
            print(f"task id after adding is {self.task_id}")
        fm.destroy()
        viewport.destroy()
        self.show_tasks()

    def show_tasks(self):
        viewport = tk.Tk()
        viewport.title("To_Do Manager")
        viewport.config(pady=10, padx=10, background="#FFFFEF")
        b = 1
        try:
            with open(file="tasks.json") as raw_tasks:
                tasks = json.load(fp=raw_tasks)
        except FileNotFoundError:
            pass
        else:
            for num in range(self.task_id):
                title = tasks[str(b)]["title"]
                create_task = tk.Button(text=title, command=lambda t_title=title: self.open_task(viewport, t_title))
                create_task.config(font=self.input_FONT, width=22, height=2)
                create_task.grid(row=b, column=1, pady=5, padx=5)
                b += 1
        user = tk.Label(text="Dear_User", font=self.head_FONT)
        user.config(foreground="#45458B", background="#FFFFEF")
        user.grid(row=0, column=0)
        add_task = tk.Button(text="+add", command=lambda: self.add_task_ui(viewport))
        add_task.config(font=self.input_FONT, background="#7F7FFF", foreground="#FFFFEF")
        add_task.grid(row=b, column=1)
        logout = tk.Label(text="Log Out", font=("small fonts", 13, "normal"))
        logout.config(foreground="#45458B", background="#FFFFEF")
        logout.grid(row=b+1, column=2)
        viewport.mainloop()

    def open_task(self, fm_window, task_title):
        viewport = tk.Tk()
        viewport.title("To_Do Manager")
        viewport.config(pady=18, padx=25, background="#FFFFEF")
        task_num = 0
        with open(file="tasks.json", mode="r") as tasks_file:
            tasks = json.load(fp=tasks_file)
            for key, value in tasks.items():
                print("key is", key)
                print("value is", value)

        for dictn in tasks:
            task_num += 1
            if tasks[dictn]["title"] == task_title:
                task = tasks[dictn]
                break
        page_title = tk.Label(viewport, text=f"/*Task: {task_num}*/", font=self.open_head_FONT)
        page_title.config(background="#FFFFEF", foreground="#45458B")
        page_title.grid(row=0, column=0, columnspan=2, pady=35)

        date_top = tk.Label(viewport, text="Date created", font=self.head_FONT)
        date_top.config(background="#FFFFEF", foreground="#10104E")
        date_top.grid(row=1, column=0, padx=15)
        date = tk.Label(viewport, text=task["date"], font=self.open_input_FONT)
        date.grid(row=2, column=0, padx=5)
        date.config(background="#FFFFEF")
        time_top = tk.Label(viewport, text="Time created", font=self.head_FONT)
        time_top.grid(row=1, column=1, padx=15)
        time_top.config(background="#FFFFEF", foreground="#10104E")
        time = tk.Label(viewport, text=task["time"], font=self.open_input_FONT)
        time.grid(row=2, column=1, padx=5)
        time.config(background="#FFFFEF")

        gap = tk.Label(viewport, text="")
        gap.config(background="#FFFFEF")
        gap.grid(row=3, column=0, pady=8)

        title_top = tk.Label(viewport, text="Title:", font=("kozuka mincho pro h", 15, "normal"))
        title_top.config(background="#FFFFEF", foreground="#10104E")
        title_top.grid(row=4, column=0, columnspan=2)
        desc_top = tk.Label(viewport, text="Description:", font=("kozuka mincho pro h", 15, "normal"))
        desc_top.config(background="#FFFFEF", foreground="#10104E")
        desc_top.grid(row=6, column=0, columnspan=2)
        task_title = tk.Label(viewport, text=task["title"], font=self.open_input_FONT)
        task_title.config(background="#FFFFEF")
        task_title.grid(row=5, column=0, columnspan=2)
        task_desc = tk.Label(viewport, text=task["desc"], font=self.open_input_FONT)
        task_desc.config(background="#FFFFEF")
        task_desc.grid(row=7, column=0, columnspan=2)
        delete_button = tk.Button(viewport, command=lambda: self.delete_task(fm_window, viewport, task_num))
        delete_button.config(background="red", text="Delete", foreground="white")
        delete_button.grid(row=8, column=0, pady=5)
        close_button = tk.Button(viewport, text="Close", command=lambda: self.close_viewport(viewport))
        # close_button.config(background="#7F7FFF", foreground="#FFFFEF")
        close_button.grid(row=8, column=1, pady=5)
        print(f"task num is {task_num}")
        print("this is", type(task["desc"]), "sumn")
        print("the title at", task["desc"], "sumn")
        viewport.mainloop()

    def delete_task(self, fm_window, viewport, task_num):
        key = str(task_num)
        task_id = 0
        new_tasks = {}
        with open(file="tasks.json", mode="r") as tasks_data:
            tasks = json.load(fp=tasks_data)
        tasks.pop(key)
        for key, value in tasks.items():
            task_id += 1
            new_tasks[str(task_id)] = value
        with open(file="tasks.json", mode="w") as tasks_file:
            json.dump(fp=tasks_file, obj=new_tasks, indent=4)
        with open(file="task_id.txt", mode="w") as task_id_file:
            json.dump(fp=task_id_file, obj=task_id)
        self.task_id -= 1
        fm_window.destroy()
        viewport.destroy()
        self.show_tasks()

    @staticmethod
    def close_viewport(viewport):
        viewport.destroy()
