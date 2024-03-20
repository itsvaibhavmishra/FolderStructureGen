import os
import shutil
import time
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import ctypes as ct
import webbrowser

def generate_folder_structure():
    folder_path = folder_entry.get()
    excluded_items = excluded_entry.get().split(",")
    excluded_items = [item.strip() for item in excluded_items]

    if not os.path.exists(folder_path):
        messagebox.showerror("Error", "Folder not found.")
        return

    # Extract folder name from the folder path
    folder_name = os.path.basename(folder_path)

    # Adjust the output file path to be inside the selected folder
    output_file = os.path.join(folder_path, f"{folder_name}_structure.md")

    progress_bar['value'] = 0

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("## Folder Structure Generator\n")
        f.write("### by [Vaibhaw Mishra](https://github.com/itsvaibhavmishra)\n\n")
        f.write("```\n")

        total_items = count_items(folder_path, excluded_items)
        processed_items = 0
        update_progress_bar(processed_items, total_items)

        f.write(f"{folder_path}/\n")
        processed_items = crawl_folder(folder_path, f, 1, processed_items, total_items, excluded_items)

        f.write("```")

    progress_bar['value'] = 100

    messagebox.showinfo("Success", "Script completed.")

def count_items(folder_path, exclude_list=None):
    if exclude_list is None:
        exclude_list = []

    count = 0
    for item in os.listdir(folder_path):
        if item not in exclude_list:
            count += 1
            if os.path.isdir(os.path.join(folder_path, item)):
                count += count_items(os.path.join(folder_path, item), exclude_list)
    return count

def crawl_folder(folder_path, output_file, depth, processed_items, total_items, exclude_list=None):
    if exclude_list is None:
        exclude_list = []

    for item in os.listdir(folder_path):
        if item not in exclude_list:
            processed_items += 1
            update_progress_bar(processed_items, total_items)

            if os.path.isdir(os.path.join(folder_path, item)):
                output_file.write("│   " * (depth-1) + "├── " + item + "/\n")
                processed_items = crawl_folder(os.path.join(folder_path, item), output_file, depth + 1, processed_items, total_items, exclude_list)
            else:
                output_file.write("│   " * (depth-1) + "├── " + item + "\n")
    return processed_items

def update_progress_bar(current, total):
    progress = (current / total) * 100 if total != 0 else 100
    progress_bar['value'] = progress
    progress_label.config(text=f"{int(progress)}%")

def open_folder():
    folder_selected = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_selected)

def reset():
    folder_entry.delete(0, tk.END)
    excluded_entry.delete(0, tk.END)
    progress_bar['value'] = 0
    progress_label.config(text="")

def open_github():
    webbrowser.open_new_tab("https://github.com/itsvaibhavmishra/FolderStructureGen/README.md")

root = tk.Tk()
root.title("Folder Structure Generator by Vaibhaw Mishra")
root.geometry("700x300")  # Set fixed window size

# Disable window resizing
root.resizable(False, False)

# Styling
style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', background='#173b6c', foreground='#fff', font=('Helvetica', 12, 'bold'), borderwidth=0, relief="raised", padding=10, focusthickness=0)
style.map('TButton', background=[('active', '#fff'), ('disabled', '#173b6c')], foreground=[('active', '#000'), ('disabled', '#fff')])
style.configure('TEntry', font=('Helvetica', 12), relief="flat", fieldbackground="white")
style.configure('green.Horizontal.TProgressbar', background='green')  # Set progress bar color to green
style.configure('Main.TFrame', background='#040b14') 

# Main Frame
main_frame = ttk.Frame(root, padding=50, style='Main.TFrame')  # Increased padding
main_frame.grid(row=0, column=0, sticky='nsew')

# Title
title_label = ttk.Label(main_frame, text="Folder Structure Generator by Vaibhaw Mishra", font=('Helvetica', 20, 'bold'), anchor='center', background="#040b14", foreground="#fff")
title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))  # Increased font size and padding

# Folder Entry
folder_label = ttk.Label(main_frame, text="Select Folder:", font=('Helvetica', 12), background="#040b14", foreground="#fff")  # Increased font size
folder_label.grid(row=1, column=0, sticky='w')

folder_entry = ttk.Entry(main_frame, width=40)
folder_entry.grid(row=1, column=1, pady=(0, 10), sticky='w')
folder_button = ttk.Button(main_frame, text="Open", command=open_folder, style='TButton')
folder_button.grid(row=1, column=2, padx=(5, 0))

# Excluded Items Entry
excluded_label = ttk.Label(main_frame, text="Excluded Items:", font=('Helvetica', 12), background="#040b14", foreground="#fff")
excluded_label.grid(row=2, column=0, sticky='w')
excluded_entry = ttk.Entry(main_frame, width=40)
excluded_entry.grid(row=2, column=1, pady=(0, 10), sticky='w')

# Progress Bar
progress_bar = ttk.Progressbar(main_frame, orient='horizontal', length=300, mode='determinate', style='green.Horizontal.TProgressbar')
progress_bar.grid(row=3, column=0, columnspan=3, pady=(0, 10))

# Progress Label
progress_label = ttk.Label(main_frame, text="", font=('Helvetica', 12), background="#040b14", foreground="#fff")
progress_label.grid(row=3, column=2, columnspan=3, pady=(0, 10))

# Buttons
generate_button = ttk.Button(main_frame, text="Generate", command=generate_folder_structure, style='TButton')
generate_button.grid(row=5, column=0, pady=(0, 10), sticky='ww')

reset_button = ttk.Button(main_frame, text="Reset", command=reset, style='TButton')
reset_button.grid(row=5, column=1, pady=(0, 10), sticky='ww')

github_button = ttk.Button(main_frame, text="Readme", command=open_github, style='TButton')
github_button.grid(row=5, column=2, pady=(0, 10), sticky='ww')

root.mainloop()
