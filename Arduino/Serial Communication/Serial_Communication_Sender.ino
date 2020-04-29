char rb=0;               //character variable fo storing the user inserted data
void setup() 
{
 Serial.begin(9600);     //start serial communication with baud rate 9600

}

void loop() 
{
  if (Serial.available() > 0)  //if serial connection is available
  {    
    rb = Serial.read();       //read character from user
    if(rb=='0'||rb=='1')      //if it the character is 1 or 0
      Serial.write(rb);       // write the value through serial connection
  } 

}
