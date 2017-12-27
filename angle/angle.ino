int analogPin = 0;  // Means A0 input.If you use A1,
                    // then analogPin must be 1;

// Initializes serial port.Baudrate is set to 9600.
void setup()
{
  Serial.begin(9600);
}

// The main loop which Arduino runs. 
void loop()
{
  int percent;
  int ang = analogRead( analogPin ); // Reads A0 and gets W.
  percent = map(ang,0,1023,0,300); // percent will range from 0 to 300.
  Serial.println(ang); // Sends the data to serial port.
  Serial.println(percent);
}
