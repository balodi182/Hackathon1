import tkinter as tk
import random
import time
from threading import Thread

# File to read variables from
file_path = "variable_data.txt"

# Initialize variables
setTemp = 0.0
oxygen_percentage = 0.0
temperature1 = 0.0
humidity1 = 0.0
temperature2 = 0.0
humidity2 = 0.0
temperature3 = 0.0
humidity3 = 0.0
gyroX_dps = 0.0
gyroY_dps = 0.0
gyroZ_dps = 0.0
tempC = 0.0
smoke = 0
M1 = 0
M2 = 0
M3 = 0
Buzzer = 3
Dimmer = 4000
Step = 10
Direction = -10
humidifier = 0

# Function to read variables from file
def read_variables():
    global setTemp, oxygen_percentage, temperature1, humidity1, temperature2, humidity2
    global temperature3, humidity3, gyroX_dps, gyroY_dps, gyroZ_dps, tempC, smoke
    global M1, M2, M3, Buzzer, Dimmer, Step, Direction
    while True:
        with open(file_path, "r") as file:
            for line in file:
                if "=" in line:
                    key, value = line.strip().split('=')
                    if key == "setTemp":
                        setTemp = float(value)
                    elif key == "oxygen_percentage":
                        oxygen_percentage = float(value)
                    elif key == "temperature1":
                        temperature1 = float(value)
                    elif key == "humidity1":
                        humidity1 = float(value)
                    elif key == "temperature2":
                        temperature2 = float(value)
                    elif key == "humidity2":
                        humidity2 = float(value)
                    elif key == "temperature3":
                        temperature3 = float(value)
                    elif key == "humidity3":
                        humidity3 = float(value)
                    elif key == "gyroX_dps":
                        gyroX_dps = float(value)
                    elif key == "gyroY_dps":
                        gyroY_dps = float(value)
                    elif key == "gyroZ_dps":
                        gyroZ_dps = float(value)
                    elif key == "tempC":
                        tempC = float(value)
                    elif key == "smoke":
                        smoke = int(value)
                    elif key == "M1":
                        M1 = int(value)
                    elif key == "M2":
                        M2 = int(value)
                    elif key == "M3":
                        M3 = int(value)
                    elif key == "Buzzer":
                        Buzzer = int(value)
                    elif key == "Dimmer":
                        Dimmer = int(value)
                    elif key == "Step":
                        Step = int(value)
        time.sleep(1)

# Function to update the labels with the current values
def update_labels():
    oxygen_label.config(text=f"Oxygen: {oxygen_percentage}")
    temp1_label.config(text=f"T1: {temperature1}")
    hum1_label.config(text=f"H1: {humidity1}")
    tempC_label.config(text=f"TR: {tempC}")
    gyroX_label.config(text=f"GX: {gyroX_dps}")
    gyroY_label.config(text=f"GY: {gyroY_dps}") 
    gyroZ_label.config(text=f"GZ: {gyroZ_dps}")
    root.after(1000, update_labels)  # Schedule the function to run every second

# Functions to handle button clicks
def on_button1_click():
    global Direction, Step
    Direction = -1
    Step = 10
    print("Button1 clicked")
    with open("Set.txt", "w") as Set:
        Set.write(f"SetTemp={setTemp}\nSetHum={humidifier}\nStep={Step}\nDirection={Direction}")


def on_button2_click():
    global Direction, Step
    Direction = 1
    Step = 10
    print("Button2 clicked")
    with open("Set.txt", "w") as Set:
        Set.write(f"SetTemp={setTemp}\nSetHum={humidifier}\nStep={Step}\nDirection={Direction}")


# Function to update setTemp from the scale
def update_set_temp(val):
    global setTemp
    setTemp = float(val)
    write_set_data()

# Function to update setHum from the scale
def update_set_hum(val):
    global humidifier
    humidifier = float(val)
    write_set_data()

# Function to write set values to file
def write_set_data():
    with open("Set.txt", "w") as Set:
        Set.write(f"SetTemp={setTemp}\nSetHum={humidifier}\nStep={Step}\nDirection={Direction}")

# Set up the main application window
root = tk.Tk()
root.title("Sensor Data")

# Create labels to display sensor data
oxygen_label = tk.Label(root, text="Oxygen: 0.0", font=('Helvetica', 16))
oxygen_label.pack()

temp1_label = tk.Label(root, text="T1: 0.0", font=('Helvetica', 16))
temp1_label.pack()

hum1_label = tk.Label(root, text="H1: 0.0", font=('Helvetica', 16))
hum1_label.pack()

tempC_label = tk.Label(root, text="TR: 0.0", font=('Helvetica', 16))
tempC_label.pack()

gyroX_label = tk.Label(root, text="GX: 0.0", font=('Helvetica', 16))
gyroX_label.pack()

gyroY_label = tk.Label(root, text="GY: 0.0", font=('Helvetica', 16))
gyroY_label.pack()

gyroZ_label = tk.Label(root, text="GZ: 0.0", font=('Helvetica', 16))
gyroZ_label.pack()

# Create buttons
button1 = tk.Button(root, text="Button1", command=on_button1_click)
button1.pack(pady=10)

button2 = tk.Button(root, text="Button2", command=on_button2_click)
button2.pack(pady=10)

# Create scales to adjust setTemp and humidifier
set_temp_scale = tk.Scale(root, from_=0, to=100, orient='horizontal', label='SetTemp', command=update_set_temp)
set_temp_scale.pack(pady=10)

set_hum_scale = tk.Scale(root, from_=0, to=100, orient='horizontal', label='SetHum', command=update_set_hum)
set_hum_scale.pack(pady=10)

# Start a separate thread to read variables from the file
thread = Thread(target=read_variables)
thread.daemon = True
thread.start()

# Start updating the labels
update_labels()

# Run the Tkinter event loop
root.mainloop()
