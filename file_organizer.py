import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Core Logic
def organize_files(folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            if os.path.isdir(file_path):
                continue

            _, ext = os.path.splitext(filename)
            ext = ext[1:].lower() or 'no_extension'

            dest_folder = os.path.join(folder_path, ext)
            os.makedirs(dest_folder, exist_ok=True)

            shutil.move(file_path, os.path.join(dest_folder, filename))
        messagebox.showinfo("Success", "Files organized successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# GUI Setup
def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path.set(folder_selected)

def run_organizer():
    path = folder_path.get()
    if not path:
        messagebox.showwarning("No Folder", "Please select a folder first.")
        return
    organize_files(path)

# GUI Layout
root = tk.Tk()
root.title("File Organizer")

folder_path = tk.StringVar()

tk.Label(root, text="Select Folder to Organize:").pack(pady=10)
tk.Entry(root, textvariable=folder_path, width=50).pack(padx=10)
tk.Button(root, text="Browse", command=browse_folder).pack(pady=5)
tk.Button(root, text="Organize Files", command=run_organizer).pack(pady=20)

root.mainloop()
