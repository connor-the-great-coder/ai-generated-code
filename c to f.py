import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert():
    try:
        temperature = float(entry.get())
        precision = int(precision_var.get())
        
        if conversion_type.get() == "C to F":
            result = celsius_to_fahrenheit(temperature)
            result_label.config(text=f"{temperature:.{precision}f}°C is {result:.{precision}f}°F")
        elif conversion_type.get() == "F to C":
            result = fahrenheit_to_celsius(temperature)
            result_label.config(text=f"{temperature:.{precision}f}°F is {result:.{precision}f}°C")
    except ValueError:
        result_label.config(text="Please enter a valid temperature")

def toggle_theme():
    theme_choice = theme_var.get()
    if theme_choice == "light":
        window.tk_setPalette(background='#ffffff', foreground='#000000')
        style.theme_use('clam')
    else:
        window.tk_setPalette(background='#2E2E2E', foreground='#ffffff')
        style.theme_use('clam')

def save_theme():
    theme_choice = theme_var.get()
    with open("settings.txt", "w") as file:
        file.write(theme_choice)

def apply_theme():
    toggle_theme()

# Function to close the settings window
def close_settings_window():
    settings_window.destroy()

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")

# Set default theme to system theme
theme_var = tk.StringVar()

# Check if "settings.txt" file exists
try:
    with open("settings.txt", "r") as file:
        saved_theme = file.read().strip()
        theme_var.set(saved_theme)
except FileNotFoundError:
    theme_var.set(window.tk_getPalette('background'))

# Apply the initial theme
toggle_theme()

# Create input entry
entry = tk.Entry(window, width=10)
entry.grid(row=0, column=0, padx=10, pady=10)

# Create conversion type radio buttons
conversion_type = tk.StringVar(value="C to F")
c_to_f_radio = tk.Radiobutton(window, text="C to F", variable=conversion_type, value="C to F")
f_to_c_radio = tk.Radiobutton(window, text="F to C", variable=conversion_type, value="F to C")
c_to_f_radio.grid(row=0, column=1)
f_to_c_radio.grid(row=0, column=2)

# Create precision setting
precision_label = ttk.Label(window, text="Precision:")
precision_label.grid(row=0, column=3)
precision_var = tk.StringVar(value="2")
precision_spinbox = tk.Spinbox(window, from_=0, to=10, textvariable=precision_var)
precision_spinbox.grid(row=0, column=4)

# Create convert button
convert_button = tk.Button(window, text="Convert", command=convert)
convert_button.grid(row=0, column=5, padx=10, pady=10)

# Create result label
result_label = tk.Label(window, text="")
result_label.grid(row=1, column=0, columnspan=6, pady=10)

# Create open settings button
open_settings_button = tk.Button(window, text="Open Settings", command=lambda: open_settings_window())
open_settings_button.grid(row=2, column=0, columnspan=6, pady=10)

# Create settings window
def open_settings_window():
    global settings_window
    settings_window = tk.Toplevel(window)
    settings_window.title("Settings")

    # Create theme toggle in settings window
    theme_label = ttk.Label(settings_window, text="Theme:")
    theme_label.grid(row=0, column=0, padx=5, pady=5)
    theme_toggle = ttk.Combobox(settings_window, values=["light", "dark"], textvariable=theme_var, state="readonly")
    theme_toggle.grid(row=0, column=1, padx=5, pady=5)

    # Set the default theme in the settings window
    theme_toggle.set(theme_var.get())

    # Create precision setting in settings window
    precision_label = ttk.Label(settings_window, text="Precision:")
    precision_label.grid(row=1, column=0, padx=5, pady=5)
    precision_spinbox = tk.Spinbox(settings_window, from_=0, to=10, textvariable=precision_var)
    precision_spinbox.grid(row=1, column=1, padx=5, pady=5)

    # Create Save, Apply, and Cancel buttons
    save_button = tk.Button(settings_window, text="Save", command=lambda: [save_theme(), apply_theme()])
    apply_button = tk.Button(settings_window, text="Apply", command=apply_theme)
    cancel_button = tk.Button(settings_window, text="Cancel", command=close_settings_window)

    save_button.grid(row=2, column=0, pady=10)
    apply_button.grid(row=2, column=1, pady=10)
    cancel_button.grid(row=2, column=2, pady=10)

# Start the main loop
window.mainloop()
