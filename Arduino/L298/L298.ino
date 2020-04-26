void setup() 
{
 Serial.begin(9600);                    //setting Baud rate for serial communication and establishing connection
 pinMode(12,OUTPUT);                    //setting Pin 12 as input pin for motor 1
 pinMode(11,OUTPUT);                    //setting Pin 11 as input pin for motor 1
 pinMode(10,OUTPUT);                    //setting Pin 10 as input pin for motor 2
 pinMode(9,OUTPUT);                     //setting Pin 9 as input pin for motor 2

}

void loop() 
{
  
 if(Serial.available()>0)               //if connection is available
 {
  char dir=Serial.read();               //read the data and store it in character variable dir 
  if(dir=='W'||dir=='w')              //if the dir is 'W'
  {
    digitalWrite(12,LOW);
    digitalWrite(11,HIGH);           //set pin 11 and 10 to HIGH and other to LOW
    digitalWrite(10,HIGH);           //both motors will rotate forward
    digitalWrite(9,LOW);
  }
  else
  if(dir=='S'||dir=='s')             //if the dir is 'S'
  {
    digitalWrite(12,HIGH);
    digitalWrite(11,LOW);            //set pin 12 and 9 to HIGH and other to LOW
    digitalWrite(10,LOW);            //both motors will rotate backward
    digitalWrite(9,HIGH);
  }
  else
  if(dir=='A'||dir=='a')             //if the dir is 'A'
  {
    digitalWrite(12,LOW);
    digitalWrite(11,HIGH);           //set pin 11 and 9 to HIGH and other to LOW
    digitalWrite(10,LOW);            //the motor on right will rotate forward and the one on the left will rotate backward
    digitalWrite(9,HIGH);
  }
  else
  if(dir=='D'||dir=='D')            //if the dir is 'D'
  {
    digitalWrite(12,HIGH);
    digitalWrite(11,LOW);           //set pin 12 and 10 to HIGH and other to LOW
    digitalWrite(10,HIGH);          //the motor on left will rotate forward and the one on the right will rotate backward
    digitalWrite(9,LOW);
  }
  else
  if(dir=='H'||dir=='h')           //if the dir is 'H'
  {
    digitalWrite(12,LOW);
    digitalWrite(11,LOW);          //set all the pins to LOW
    digitalWrite(10,LOW);          //all the motors will stop
    digitalWrite(9,LOW);
  }
  
 }


}
