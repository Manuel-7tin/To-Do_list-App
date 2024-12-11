from datetime import datetime


class Task:

    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.date = datetime.today().strftime("%b/%d/%Y")
        self.time = datetime.today().strftime("%H:%M")
