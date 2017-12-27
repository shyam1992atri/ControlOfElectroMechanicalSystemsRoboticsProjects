import serial 
ser=serial.serial("/dev/tty/COM10",9600)
i=0
while(i<200):
    i=i+1
    ser.write(int('1'))


    
## Serial . parseint() in arudinoto read values
