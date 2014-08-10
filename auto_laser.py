import datetime, serial

print("Welcome to auto laser!")
print("This program will automatically note down measurements from a total station that is connected via USB.")
print("All measurements taken this execution will be saved in a file named after the time this program was started.")

try:
    with open("{}.txt".format(datetime.datetime.now()), "w+") as file:
        try:
            ser = serial.Serial('/dev/ttyACM0', 9600)
        except:
            print("Unable to open port.")
            exit()
        while True:
            serial_line = ser.readline()
            try:
                file.write(serial_line)
            except:
                print("Unable to wite measurement to file. Make sure file is not open anywhere else.")
            print("Written measurement: {}".format(serial_line))
        ser.close()
except:
    print("Unable to create new file.")
