import tkinter as tk
from tkinter import filedialog

def save_data():
    # Implement the logic to save data here
    print("Data saved!")

def cancel_action():
    # Implement the logic for cancel action here
    root.destroy()

def browse_file():
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

# Create the main window
root = tk.Tk()
root.title("Tkinter Example")

# Label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10, padx=10, anchor=tk.W)

# RadioButtons
radio_label = tk.Label(root, text="Radio Buttons:")
radio_label.pack(anchor=tk.W, pady=10, padx=10)

radio_var = tk.StringVar()
radio_btn1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1")
radio_btn2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2")
radio_btn1.pack(anchor=tk.W, pady=10, padx=10)
radio_btn2.pack(anchor=tk.W, pady=10, padx=10)

# Checkbuttons
check_label = tk.Label(root, text="Check Buttons:")
check_label.pack(anchor=tk.W, pady=10, padx=10)

check_var1 = tk.IntVar()
check_var2 = tk.IntVar()
check_btn1 = tk.Checkbutton(root, text="Check 1", variable=check_var1)
check_btn2 = tk.Checkbutton(root, text="Check 2", variable=check_var2)
check_btn1.pack(anchor=tk.W, pady=10, padx=10)
check_btn2.pack(anchor=tk.W, pady=10, padx=10)

# TextArea
text_label = tk.Label(root, text="Text Area:")
text_label.pack(anchor=tk.W, pady=10, padx=10)

text_area = tk.Text(root, height=5, width=30)
text_area.pack(pady=10, padx=10)

# Entry
entry_label = tk.Label(root, text="Entry:")
entry_label.pack(anchor=tk.W, pady=10, padx=10)

entry = tk.Entry(root)
entry.pack(pady=10, padx=10)

# Dropdown
dropdown_label = tk.Label(root, text="Dropdown:")
dropdown_label.pack(anchor=tk.W, pady=10, padx=10)

options = ["Option 1", "Option 2", "Option 3"]
dropdown_var = tk.StringVar()
dropdown = tk.OptionMenu(root, dropdown_var, *options)
dropdown.pack(pady=10, padx=10)

# File Upload
file_label = tk.Label(root, text="File Upload:")
file_label.pack(anchor=tk.W, pady=10, padx=10)

file_entry = tk.Entry(root, state="readonly", width=30)
file_entry.pack(pady=10, padx=10)

file_button = tk.Button(root, text="Browse", command=browse_file)
file_button.pack(pady=10, padx=10)

# Buttons
save_button = tk.Button(root, text="Save", command=save_data)
save_button.pack(side=tk.LEFT, pady=10, padx=10)

cancel_button = tk.Button(root, text="Cancel", command=cancel_action)
cancel_button.pack(side=tk.RIGHT, pady=10, padx=10)

# Start the Tkinter event loop
root.mainloop()
