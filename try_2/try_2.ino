#define sensor A0
#define motor 3  //motor is nothing but ur enable in the hbridge code
#define CW 4
#define CCW 5
int dT=300;
int vel=255;
//int now=300;
//int lasttime=0;
double error,lastError,I_error,D_error,output;
float sensorVal;
float setPoint=175;
float kp;
float ki;
float kd;
void setup()
{
  Serial.begin(9600);
  pinMode(sensor,INPUT);
  pinMode(motor,OUTPUT);
  pinMode(CW,OUTPUT);
  pinMode(CCW,OUTPUT);
  kp=10;
  ki=2;
  kd=1;
  digitalWrite(motor,HIGH); // enable is on *
}
// directions from the view of potentiometer head facing the user
//suppose the 360 deg brk point is on the right side at 90 deg.
// 5 v along 360 deg, therefore calculating v for 90 deg is 1.25v
//therefore our perfect vertical position is attained at voltage 1.25

void loop()
{
  do{
  sensorVal = analogRead(sensor);
  //float voltage = sensorVal * (5.0 / 1023.0);
  Serial.println(sensorVal);
  //delay(250);
  if(sensorVal>setPoint)
  {
    compute();
    vel_calc();
    digitalWrite(CW,vel);
    digitalWrite(CCW,LOW);
    delay(50);
  }
  else if(sensorVal<setPoint)
  {
    compute();
    vel_calc();
    digitalWrite(CW,LOW);
    digitalWrite(CCW,vel);
    delay(50);
  }  
  if(sensorVal==setPoint)
  {
    digitalWrite(CW,LOW);
    digitalWrite(CCW,LOW);
    delay(50); 
  }
  sensorVal = analogRead(sensor);
  Serial.println(sensorVal);
 }while(sensorVal!=setPoint);
}
void compute()
{
  //double dT= double(now-lasttime);
    error= setPoint - sensorVal;
    I_error +=(error*dT);
    D_error=(error-lastError)/dT;
    output= kp*error + ki*I_error + kd*D_error;
  //lastError = error;
  //lasttime = now;
}  
void vel_calc()
{
  if(output>100)
  vel=130;
  else 
  vel=255;
}  
