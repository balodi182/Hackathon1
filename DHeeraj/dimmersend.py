import serial
import numpy as np
import time

v=open("IDs.txt","r")
for i in v:
    if i.split("=")[0]=="D":
        ID=i.split("=")[1][0]
v.close()
    

# File to read variables from
file_path = "variable_data.txt"
ser = serial.Serial('/dev/ttyUSB'+ID, 9600)
time.sleep(2)  

# Initialize variables
Dimmer = 4000





def cross():
    pass



# Read variables from file
while True:
    with open(file_path, "r") as file:
        
        for line in file:
            key, value = line.strip().split('=')
            if key == "Dimmer":
                Dimmer = int(4000)
        ser.write(f"Dimmer: {Dimmer}\n".encode())
        
        


           
