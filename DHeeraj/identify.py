import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)
ser2 = serial.Serial('/dev/ttyUSB1', 9600)
ser3 = serial.Serial('/dev/ttyUSB2', 9600)
sensor = -1
dimmer = 5
out=10
f=open("IDs.txt","w")

while dimmer==5 or out==10:
    ser.write("Give ID\n".encode())
    line = ser.readline().decode().strip()
    print(line)
    data = line.split(':')
    
    if len(data) > 0 and data[0].strip() == "ID":
        if len(data) > 1:
            if data[1].strip() == "11":
                dimmer = 0
            elif data[1].strip() == "10":
                sensor = 0
            elif data[1].strip() == "12":
                out = 0
            
    
    # Uncomment the following lines if you want to read from ser2
    ser2.write("Give ID\n".encode())
    line2 = ser2.readline().decode().strip()
    print(line2)
    data2 = line2.split(':')
    
    
    # Further processing based on data from ser2
    
    if len(data2) > 0 and data2[0].strip() == "ID":
        if len(data2) > 1:
            if data2[1].strip() == "11":
                dimmer = 1
            elif data2[1].strip() == "10":
                sensor = 1
            elif data2[1].strip() == "12":
                out = 1
            
    ser3.write("Give ID\n".encode())
    line3 = ser3.readline().decode().strip()
    print(line3)
    data3 = line3.split(':')
    
    
    if len(data3) > 0 and data3[0].strip() == "ID":
        if len(data3) > 1:
            if data3[1].strip() == "11":
                dimmer = 2
            elif data3[1].strip() == "10":
                sensor = 2
            elif data3[1].strip() == "12":
                out = 2
            
    A=[0,1,2]
    A.remove(dimmer)
    A.remove(out)
    sensor=A[0]
    
    
    
    print("Dimmer =", dimmer)
    print("Sensor =", sensor)
    print("Out =", out)
    
f.write(f"D={dimmer}\nS={sensor}\nO={out}")
print("Identification done")