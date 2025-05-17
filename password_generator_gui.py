import tkinter as tk
import string
import random
from tkinter import messagebox as mb


root = tk.Tk()
root.title('Password Generator')
root.geometry('450x300')

var = tk.StringVar()
var.set('8')


def generate_password():
    try:
        length = int(entry_len.get())

        letters_upper = string.ascii_uppercase
        letters_lower = string.ascii_lowercase
        numbers = string.digits
        special_chars = string.punctuation

        char_str = letters_upper + numbers + letters_lower + special_chars
        #random.shuffle(password)
        password = ''
        meets_criteria = False
        for _ in range(length):
            new_char = random.choice(char_str)
            password += new_char
        entry_pass.delete(0, 'end')
        entry_pass.insert(0, password)

    except :
        mb.showwarning('Warning', 'Please enter a valid number')

    
def copy_to_clipboard():
    password = entry_pass.get()
    root.clipboard_clear()
    root.clipboard_append(password)


get_frame = tk.LabelFrame(root,text=' How much characters ? ', padx=20, pady=20)
get_frame.place(x=20, y=10)

entry_len = tk.Entry(get_frame, font=('helvetica', 24), relief='groove')
entry_len.pack()
entry_len.insert(0, 8)

entry_pass = tk.Entry(root, font=('helvetica',24))
entry_pass.place(x=40, y=150)

button_generate = tk.Button(root, text='generate strong password', font=('helvetica', 12), bd=2, command=generate_password)
button_generate.place(x=30, y=230)

button_copy = tk.Button(root, text='copy to clipboard', font=('helvetica', 12), bd=2, command=copy_to_clipboard)
button_copy.place(x=280, y=230)

root.mainloop()
