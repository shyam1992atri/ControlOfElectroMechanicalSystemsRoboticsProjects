//Define Variable

int MotorPWM = 11; // ENABLE to digital pin 11
int MotorIN_A = 8;
int MotorIN_B = 12;
int encoder0PinA = 2; //encoder0PinA
int encoder0PinB = 4;  //encoder0pinB
int sensorPin = A0; 
// select the input pin for the potentiometer

/*working variables*/
double PV, Output, Setpoint;
double kp, ki, kd;
volatile unsigned long lastTime;
volatile double errSum, lastErr;
volatile int encoder0Pos = 0;
int sensorValue = 512;

void setup()
{
  pinMode(encoder0PinA, INPUT);
  digitalWrite(encoder0PinA, HIGH); //turn on pullup resistor
  pinMode(encoder0PinB, INPUT);
  digitalWrite(encoder0PinB, HIGH); //turn on pullup resistor
  attachInterrupt(0, doEncoder, CHANGE); //encoder pin on interrupt 0 - pin2

//Controller Parameter
  kp = 0.5;
  ki = 0.0;
  kd = 0.0;

  Serial.begin (9600);
  Serial.println("start");
}
void loop()
{
  sensorValue = analogRead(sensorPin); //read the value
  Setpoint = (double)(sensorValue - 512)*0.35; //Full scale setpoint +/- 180deg
  PV = (double)encoder0Pos*11.25; //360 deg = 32 pulses
  compute(); // Find controller output
  //Send command to DC motor
  if(Output > 0)
    {
      analogWrite(MotorPWM, Output);
      CC();
    }
   else if(Output<-0)
    {
      analogWrite(MotorPWM, -Output);
      CCW();
    }
   else
    {
      STOP();
    }

// display setpoint and measured value

   if(count>50) 
    {
      Serial.print(Setpoint);
      Serial.print('');
      Serial.print(PV);
      Serial.print('');
      Serial.println(Output);
      count= 0;  
    }
  else{count+=1;}
}
//Motor Control Function

void CC()
{
  digitalWrite(MotorIN_A,HIGH);
  digitalWrite(MotorIN_B,LOW);
}
void CCW()
{
  digitalWrite(MotorIN_A,LOW);
  digitalWrite(MotorIN_B,HIGH);
}
void STOP()
{
  analogWrite(MotorPWM, 0);
  digitalWrite(MotorIN_A,LOW);
  digitalWrite(MotorIN_B,LOW);
}
//Compute controller output by PID algorithm
void compute()
{
  
  /*How long since we last calculated*/
  unsigned long now = millis();

  double dT = (double)(now - lastTime); //Our Sampling time
  /*Compute all the working error variables*/
  double error = Setpoint - PV;
  errSum += (error * dT);
  double dErr = (error - lastErr) / dT;
  
  /*Compute PID Output*/
  Output = kp * error + ki * errSum + kd * dErr;
  /*Max 100, Min -100*/
  if(Output>100){Output = 100;}
  else if(Output <-100){Output = -100;}
  else{}
  /*Remember some variables for next time*/
    lastErr = error;
    lastTime = now;
}

//doEncoder function
/* If pinA and pinB are both high or both low, it is spinning
* forward. If they
re different, it
s going backward.*/

if (digitalRead(encoder0PinA) == digitalRead(encoder0PinB))
  {
    encoder0Pos++;
  }
else
  {
    encoder0Pos--;
  }
}
