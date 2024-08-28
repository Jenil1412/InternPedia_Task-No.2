
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pickle

# Create the main application window
root = tk.Tk()
root.title("To-Do List")
root.configure(background="#f0f0f0")  # Set background color of the main window

# Set the style for the widgets
style = ttk.Style()
style.theme_use("clam")  # Use the 'clam' theme for better styling
style.configure("TFrame", background="#f0f0f0")
style.configure("TButton", background="#007BFF", foreground="white", font=("Helvetica", 10, "bold"))
style.map("TButton",
          background=[("active", "#0056b3")],  # Change button color on hover
          foreground=[("active", "white")])
style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))

# Create a frame for the listbox and scrollbar
frame = ttk.Frame(root, padding="10")
frame.pack(pady=10)

# Create a listbox to display tasks with a scrollbar
listbox = tk.Listbox(frame, width=50, height=10, selectmode=tk.SINGLE, font=("Helvetica", 12), bg="#ffffff", fg="#333333", bd=0)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = ttk.Scrollbar(frame, orient="vertical", command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)

# Create an entry box to add new tasks
entry = ttk.Entry(root, width=50, font=("Helvetica", 12))
entry.pack(pady=10)

# Define functions for adding and deleting tasks
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def save_tasks():
    tasks = listbox.get(0, listbox.size())
    with open("tasks.pkl", "wb") as f:
        pickle.dump(tasks, f)

def load_tasks():
    try:
        with open("tasks.pkl", "rb") as f:
            tasks = pickle.load(f)
            listbox.delete(0, tk.END)
            for task in tasks:
                listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass

# Create buttons for adding, deleting, saving, and loading tasks
button_frame = ttk.Frame(root, padding="10", style="TFrame")
button_frame.pack(pady=10)

add_button = ttk.Button(button_frame, text="Add Task", command=add_task, style="TButton")
add_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

delete_button = ttk.Button(button_frame, text="Delete Task", command=delete_task, style="TButton")
delete_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

save_button = ttk.Button(button_frame, text="Save Tasks", command=save_tasks, style="TButton")
save_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

load_button = ttk.Button(button_frame, text="Load Tasks", command=load_tasks, style="TButton")
load_button.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Set the grid column weights so buttons expand to fill the frame
button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)

# Load tasks from file when the application starts
load_tasks()

# Run the main application loop
root.mainloop()
