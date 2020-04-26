#include<Servo.h>   // include servo library
Servo s;                    // create servo object
void setup() 
{
 s.attach(3);              // attach pin 3 to servo object ( used as control pin).
}
void loop() 
{
  s.write(90);            // writes the servo position in degrees to the servo
 
}
