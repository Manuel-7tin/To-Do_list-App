import task_manager
import access_manager
# import task_creator
# import tkinter
# from PyQt5.QtWidgets import QApplication, QLabel

# tasks = task_manager.TaskManager()
# for num in range(2):
#     task_title = input("What is the title of your task? ")
#     task_description = input("What is th description of your task? ")
#     task_001 = task_creator.Task(task_title, task_description)
#     # print(f"Your task:[{task_001.title}] is described as {task_001.description} and was create at {task_001.date_time}")
#     tasks.add_task(task_001)
# print(f"The number of tasks is {tasks.task_id}")
# print("bye")

# app = QApplication([])
# label = QLabel('Hello World!')
# label.show()
# app.exec_()

# viewport = tkinter.Tk()
# word = tkinter.Label(text="Hello World")
# word.pack()
# viewport.mainloop()

access = access_manager.AccessManager()
tasks = task_manager.TaskManager()
if access.logged_in():
    access.signing("in")
    # tasks.show_tasks()
else:
    access.signing("up")
