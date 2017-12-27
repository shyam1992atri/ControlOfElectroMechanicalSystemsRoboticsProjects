import serial  
ser = serial.Serial('COM5',9600)
b=0
#ser.write(chr(b))

while True:
    print ser.readline()
    ser.write(b)
##'1 hello world!\r\n'
##'2 hello world!\r\n'
##'3 hello world!\r\n'

    
## Serial . parseint() in arudinoto read values
