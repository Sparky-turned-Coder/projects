import tkinter as tk

tasks = []


def refresh_tasks():
    # 1. Clear the GUI list
    task_listbox.delete(0, tk.END)

    # 2. Rebuild it from the data
    for task in tasks:
        task_listbox.insert(tk.END, task)  # insert(position, value)


# tk.END is a Tkinter constant meaning "the last position in this widget(or list)"
# from a GUI standpoint, I believe this means it shows it as the most recent entry


def add_task():
    # Update the data ONLY
    tasks.append("New Task")

    # Tell the GUI to redraw itself
    refresh_tasks()


root = tk.Tk()
root.title("TODO App")

task_listbox = tk.Listbox(root, width=40)
task_listbox.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

root.mainloop()
