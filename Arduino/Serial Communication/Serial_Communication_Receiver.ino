char a;                      //character variable to store the inserted character
void setup() 
{
  Serial.begin(9600);        // start serial communication with baud rate 9600
  pinMode(13,OUTPUT);        //Set Pin 13 for LED as output
}

void loop() 
{
 while(Serial.available() > 0)  //if connection is available
 {
  a=Serial.read();              //read the character received
  if(a=='1')               
  digitalWrite(13,HIGH);        //if it is 1, set pin 13 to HIGH , lighting the led
  else
  if(a=='0')
  digitalWrite(13,LOW);         //if it is 0, set the pin 13 to LOW, turning off the led 
 }
}
