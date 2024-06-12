import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import requests
from PIL import Image, ImageTk

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def show_weather():
    location = location_entry.get()
    data = get_weather(api_key, location)
    
    if data:
        weather_info = f"Weather in {location}:\n"
        weather_info += f"Temperature: {data['main']['temp']}°C\n"
        weather_info += f"Humidity: {data['main']['humidity']}%\n"
        weather_info += f"Condition: {data['weather'][0]['description']}"
        weather_label.config(text=weather_info)
    else:
        messagebox.showerror("Error", "Could not retrieve weather data. Please check your input.")

api_key = 'b9445551782d8329f5f061bdd51c716a'

root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")
root.configure(bg="#cce0ff")  # Set background color for the root window

# Add logo at the top
logo_image = Image.open("logo.png")
logo_image = logo_image.resize((100, 100), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(root, image=logo_photo, bg="#cce0ff")  # Match background color
logo_label.pack(pady=10)

# Main frame
style = ttk.Style()
style.theme_use("clam")  # Set the theme to "clam" to enable style configuration
style.configure("Main.TFrame", background="#cce0ff")  # Set background color for the main frame
main_frame = ttk.Frame(root, padding="10", style="Main.TFrame")
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Title
title_label = ttk.Label(main_frame, text="Weather App", font=("Helvetica", 16), background="#cce0ff")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Location input
location_label = ttk.Label(main_frame, text="Enter the city name or ZIP code:", background="#cce0ff")
location_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
location_entry = ttk.Entry(main_frame)
location_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
main_frame.columnconfigure(1, weight=1)

# Get Weather button
style.configure("GetWeatherButton.TButton", background="#4CAF50", foreground="white", font=("Helvetica", 12, "bold"))
get_weather_button = ttk.Button(main_frame, text="Get Weather", command=show_weather, style="GetWeatherButton.TButton")
get_weather_button.grid(row=2, column=0, columnspan=2, pady=10)

# Weather info display
weather_frame = ttk.Frame(main_frame)
weather_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky="nsew")
# Remove the background color configuration for the weather frame
weather_label = ttk.Label(weather_frame, text="", font=("Helvetica", 12), wraplength=300)
weather_label.pack(pady=20, padx=10)

# Configure root window resizing
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

main_frame.rowconfigure(3, weight=1)

root.mainloop()
