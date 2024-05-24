import serial
import time
#v=open("IDs.txt",r)
#for i in v:
 #   if i.split("=")[0]=="S":
#        ID=i.split("=")[1][0]
#v.close()


# Initialize serial port
ID="0"
ser = serial.Serial('/dev/ttyUSB'+ID, 9600)  # Replace '/dev/ttyUSB0' with the actual port and 9600 with the baud rate



# File to save variables
file_path = "variable_data.txt"

# Function to save variables to file
def save_variables():
    with open(file_path, "w") as file:
        file.write(f"setTemp={setTemp}\n oxygen_percentage={oxygen_percentage}\n temperature1={temperature1}\n humidity1={humidity1}\n temperature2={temperature2}\n humidity2={humidity2}\n temperature3={temperature3}\n humidity3={humidity3}\n gyroX_dps={gyroX_dps}\n gyroY_dps={gyroY_dps}\n gyroZ_dps={gyroZ_dps}\n tempC={tempC}\n smoke={smoke}\n M1={M1}\n M2={M2}\n M3={M3}\n Buzzer={Buzzer}\n Dimmer={Dimmer}\n Step={Step}\n Direction={Direction}\n humidifier={humidifier}\n")
        file.close()
        
        
# Variables to store sensor data
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
Direction = 1
humidifier = 0

try:
    while True:
        # Read line from serial
        line = ser.readline().decode().strip()

        # Split line into data fields
        data = line.split(': ')

        # Update variables based on data fields
        if data[0] == 'OP':
            oxygen_percentage = float(data[1])
        elif data[0] == 'T1':
            temperature1 = float(data[1])
        elif data[0] == 'H1':
            humidity1 = float(data[1])
        elif data[0] == 'T2':
            temperature2 = float(data[1])
        elif data[0] == 'H2':
            humidity2 = float(data[1])
        elif data[0] == 'T3':
            temperature3 = float(data[1])
        elif data[0] == 'H3':
            humidity3 = float(data[1])
        elif data[0] == 'GX':
            gyroX_dps = float(data[1])
        elif data[0] == 'GY':
            gyroY_dps = float(data[1])
        elif data[0] == 'GZ':
            gyroZ_dps = float(data[1])
        elif data[0] == 'TR':
            tempC = float(data[1])
        elif data[0] == 'S':
            smoke = int(data[1])

        # Print the received data
        setTemp = 50  # Example value, replace it with the actual value
        print(setTemp)
        
        # Save variables to file
        save_variables()

        # Delay for a while to avoid flooding the file with data
        

except KeyboardInterrupt:
    ser.close()
    print("Serial ports closed.")
