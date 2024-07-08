import tkinter as tk
from tkinter import messagebox


def Calculate():
    try:
        height = float(entry_height.get()) / 100
        weight = float(entry_weight.get())

        if height <= 0:
            messagebox.showerror("Error", "Height must be greater than 0")
        elif weight <= 0:
            messagebox.showerror("Error", "Weight must be greater than 0")
        else:
            bmi = weight / (height ** 2)
            result.config(text=f"Your Body Mass Index is: {bmi:.2f}. \nYou are {Category(bmi)}")

    except ValueError:
        messagebox.showerror("Error", "Height and Weight must be numeric")


def Category(bmi):
    if bmi > 0:
        if bmi < 16.0:
            return "Severely Underweight"
        elif bmi < 18.5:
            return "Underweight"
        elif bmi < 25.0:
            return "Normal Weight"
        elif bmi < 30.0:
            return "Overweight"
        elif bmi < 35.0:
            return "Moderately Obese"
        elif bmi < 40.0:
            return "Severely Obese"
        else:
            return "Morbidly Obese"
    else:
        return "Height and Weight must be greater than 0"


def Reset():
    entry_height.delete(0, tk.END)
    entry_weight.delete(0, tk.END)
    result.config(text="")


Bmi = tk.Tk()
Bmi.title("BMI Calculator")
Bmi.iconbitmap(r"BMI_icon.ico")
Bmi['bg'] = "lightgrey"
Bmi.geometry("500x350")

title = tk.Label(Bmi, text="BMI CALCULATOR", font=("Helvetica", 24),
                 bg="lightgrey")
title.place(x=100, y=20)

label_height = tk.Label(Bmi, text="Enter your height (in cm):",
                        font=("Helvetica", 14), bg="lightgrey")
label_height.place(x=20, y=80)
entry_height = tk.Entry(Bmi, width=20, font=("Helvetica", 14))
entry_height.place(x=230, y=80)

label_weight = tk.Label(Bmi, text="Enter your weight (in kg):",
                        font=("Helvetica", 14), bg="lightgrey")
label_weight.place(x=20, y=120)
entry_weight = tk.Entry(Bmi, width=20, font=("Helvetica", 14))
entry_weight.place(x=230, y=120)

btn = tk.Button(Bmi, text="Calculate BMI", command=Calculate)
btn.place(x=140, y=180)

btn_reset = tk.Button(Bmi, text="Reset", command=Reset)
btn_reset.place(x=250, y=180)

result = tk.Label(Bmi, text="", font=("Helvetica", 12), bg="lightgrey")
result.place(x=50, y=240)

Bmi.mainloop()
