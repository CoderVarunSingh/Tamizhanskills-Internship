import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests

# ---------------- CONFIG ----------------
API_KEY = "483d3dbaf542a4d548b0abd6c9d633c2"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# ---------------- FUNCTION ----------------
def get_weather():
    city = city_entry.get()
    if not city or city.strip().lower() == "enter city name":
        messagebox.showwarning("Input Error", "Please enter a valid city name.")
        return

    try:
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", data.get("message", "City not found!"))
            return

        city_name = data["name"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"].capitalize()

        result = (
            f"📍 City: {city_name}\n"
            f"🌡️ Temperature: {temperature}°C\n"
            f"💧 Humidity: {humidity}%\n"
            f"🌈 Weather: {description}"
        )
        result_label.config(text=result)
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# ---------------- UI SETUP ----------------
root = tk.Tk()
root.title("⛅ Stylish Weather App")
root.geometry("500x600")
root.resizable(False, False)

# Load Cloudy Background
bg_image = Image.open("clouds.jpg")
bg_image = bg_image.resize((500, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Transparent Frame
frame = tk.Frame(root, bg="#ffffff", bd=0)
frame.place(relx=0.5, rely=0.5, anchor="center", width=360, height=420)

# Title
title = tk.Label(frame, text="☁️ Weather Info", font=("Segoe UI", 20, "bold"), bg="#ffffff", fg="#2d3436")
title.pack(pady=20)

# City Entry
city_entry = tk.Entry(frame, font=("Segoe UI", 14), justify="center", bg="#ecf0f1", fg="#2c3e50", relief="flat")
city_entry.insert(0, "Enter City Name")
city_entry.pack(ipady=8, ipadx=5, pady=10)

# Get Weather Button
get_button = tk.Button(frame, text="Check Weather", command=get_weather, font=("Segoe UI", 12, "bold"),
                       bg="#6c5ce7", fg="white", activebackground="#5e50d4", relief="flat", bd=0, padx=20, pady=8)
get_button.pack(pady=15)

# Result Label
result_label = tk.Label(frame, text="", font=("Segoe UI", 13), bg="#ffffff", fg="#2c3e50", justify="left", wraplength=300)
result_label.pack(pady=20)

# Exit Button
exit_btn = tk.Button(frame, text="Exit", command=root.destroy, font=("Segoe UI", 11), bg="#d63031", fg="white",
                     activebackground="#c0392b", relief="flat", padx=10, pady=6)
exit_btn.pack(pady=10)

root.mainloop()

