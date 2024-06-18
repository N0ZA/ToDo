import tkinter as tk
from tkinter import *

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title('ToDo')
        self.root.geometry("200x300")
        self.root.configure(background='#272727')

        self.task_counter = 0  # To keep track of the rows for Checkbuttons

        self.label = Label(root, text="Here are your Tasks", background='#272727', fg='white')
        self.label.place(x=0, y=0)  # Position the label

        self.button = Button(root, text="Add a new task", command=self.open_new_task)
        self.button.place(x=95, y=260)  # Position the button

        self.task_frame = Frame(root, background='#272727')
        self.task_frame.place(x=0, y=30)  # Position the task frame

    def open_new_task(self):
        new_task = tk.Toplevel(self.root)
        new_task.title("New Window")
        new_task.geometry("250x250")
        new_task.configure(background='#272727')
        label = tk.Label(new_task, text="Enter your task", background='#272727', fg='white')
        label.place(x=10, y=100)
        entry = tk.Entry(new_task)
        entry.place(x=100, y=100)

        def add_task():
            task = entry.get()
            Checkbutton(self.task_frame, text=task, background='#272727', fg='white').grid(row=self.task_counter, sticky=W)
            self.task_counter += 1  # Increment the row counter for next Checkbutton
            new_task.destroy()  # Close the new task window after adding the task

        enter = Button(new_task, text="Add", command=add_task)
        enter.place(x=100, y=150)

if __name__ == "__main__":
    root = Tk()
    app = ToDoApp(root)
    root.mainloop()
