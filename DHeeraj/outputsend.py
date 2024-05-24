import serial
import numpy as np
import time

v=open("IDs.txt","r")
for i in v:
    if i.split("=")[0]=="O":
        ID=i.split("=")[1][0]
v.close()
    

# File to read variables from
ID="1"
file_path = "Set.txt"
ser = serial.Serial('/dev/ttyUSB'+ID, 9600)
time.sleep(2)  

# Initialize variables






def cross():
    pass


Step=0
Direction=0
M1=0
M2=0
M3=0
Buzzer=1
Humidity=0


# Read variables from file
while True:
    s=time.time()
    with open(file_path, "r") as file:
        
        for line in file:
            if "=" in line:
                key, value = line.strip().split('=')
            else:
                key,value="",0
            if key == "Step":
                Step = int(value)
            elif key == "Direction":
                Direction = int(value)
            elif key == "M1":
                M1 = int(value)
            elif key == "M2":
                M2 = int(value)
            elif key == "M3":
                M3 = int(value)
            elif key == "Humidiy":
                Humidity = int(value)
            elif key == "Buzzer":
                Buzzer = int(value)

   
            
            
            
            
            
                
        ser.write(f"Step: {Step},Direction: {Direction},M1: {M1}\nM2: {M2},M3: {M3},Humidity: {Humidity},Buzzer: {Buzzer}\n".encode())
        print(f"Step: {Step}\nDirection: {Direction}\nM1: {M1}\nM2: {M2}\nM3: {M3}\nHumidity: {Humidity}\nBuzzer: {Buzzer}")

    s2=time.time()
    print(f"Time={s2-s}")

        


           
