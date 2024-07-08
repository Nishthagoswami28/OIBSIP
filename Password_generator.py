import random as rd
import string
import tkinter as tk
from tkinter import messagebox


def pwd_gen():
    try:
        l = int(entry_length.get())
        if l <= 0:
            messagebox.showerror("Error","Password length must be greater than 0")
        else:
            ch = string.ascii_letters + string.digits + string.punctuation
            res = ''.join(map(lambda _: rd.choice(ch), range(l)))

            result.config(text=f"Generated Password: {res}")

    except ValueError:
        messagebox.showerror("Error","Please enter a numeric value for password length")


def copy_pwd():
    gen_pwd = result.cget("text").split(": ")[1]
    pwd.clipboard_clear()
    pwd.clipboard_append(gen_pwd)
    messagebox.showinfo("Copied", "Password copied to clipboard")


def Reset():
    entry_length.delete(0, tk.END)
    result.config(text="")


pwd = tk.Tk()
pwd.title("Password Generator")
pwd.iconbitmap(r"pwd_gen.ico")
pwd['bg'] = "lightgrey"
pwd.geometry("500x300")

label = tk.Label(pwd, text="PASSWORD GENERATOR", font=("Helvetica", 24),
                 bg="lightgrey")
label.place(x=60, y=20)

label_length = tk.Label(pwd, text="Enter password length: ",
                        font=("Helvetica", 12), bg="lightgrey")
label_length.place(x=20, y=80)
entry_length = tk.Entry(pwd, width=20, font=("Helvetica", 14))
entry_length.place(x=230, y=80)

btn = tk.Button(pwd, text="Generate", command=pwd_gen)
btn.place(x=140, y=120)

btn_copy = tk.Button(pwd, text="Copy", command=copy_pwd)
btn_copy.place(x=200, y=120)

btn_reset = tk.Button(pwd, text="Reset", command=Reset)
btn_reset.place(x=240, y=120)

result = tk.Label(pwd, text="", font=("Helvetica", 14))
result.place(x=50, y=180)

pwd.mainloop()
