import tkinter as tk
from tkinter import messagebox
import requests


def weather_report():
    city_name = entry_city.get()
    if city_name:
        try:
            data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=a253d691390c65932dcb3cfae74edfbd&units=metric").json()

            if data["cod"] == 200:
                temp = data["main"]["temp"]
                feels_like = data["main"]["feels_like"]
                w_desc = data["weather"][0]["description"]
                wind_speed = data["wind"]["speed"]
                wind_direction = data["wind"]["deg"]
                result_temp.config(text=f"{temp}°C")
                result.config(text=f"Weather in {city_name}: {w_desc}\nFeels like: {feels_like}°C\nWind Speed: {wind_speed} m/s\nWind Direction: {wind_direction}°")

                weather_icon = data["weather"][0]["icon"]
                icon_url = f"http://openweathermap.org/img/wn/{weather_icon}.png"
                icon_response = requests.get(icon_url, stream=True)
                if icon_response.status_code == 200:
                    icon_image = tk.PhotoImage(data=icon_response.content)
                    weather_icon_label.config(image=icon_image, bg="lightgrey")
                    weather_icon_label.image = icon_image
            else:
                messagebox.showerror("Error", f"City '{city_name}' not found!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showerror("Error", "Please enter a city!")


def Reset():
    entry_city.delete(0, tk.END)
    result_temp.config(text="")
    result.config(text="")
    weather_icon_label.config(image="")


Weather = tk.Tk()
Weather.title("Weather")
Weather.iconbitmap(r"weather.ico")
Weather['bg'] = "lightgrey"
Weather.geometry("450x350")

title = tk.Label(Weather, text="Weather Now", font=("Helvetica", 24),
                 bg="lightgrey")
title.place(x=100, y=20)

label_city = tk.Label(Weather, text="Enter your city:",
                      font=("Helvetica", 18), bg="lightgrey")
label_city.place(x=40, y=80)
entry_city = tk.Entry(Weather, width=18, font=("Helvetica", 14))
entry_city.place(x=220, y=85)

btn = tk.Button(Weather, text="Get Weather", command=weather_report)
btn.place(x=140, y=140)

btn_reset = tk.Button(Weather, text="Reset", command=Reset)
btn_reset.place(x=250, y=140)

result_temp = tk.Label(Weather, font=("Helvetica", 22), justify=tk.CENTER, bg="lightgrey")
result_temp.place(x=130, y=180)

weather_icon_label = tk.Label(Weather, bg="lightgrey")
weather_icon_label.place(x=250, y=180)

result = tk.Label(Weather, font=("Helvetica", 12), bg="lightgrey")
result.place(x=100, y=240)

Weather.mainloop()
