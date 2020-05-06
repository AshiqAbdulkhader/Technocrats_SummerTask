#include "mbed.h"                     //import mbed library
#include "Servo.h"                    //import servo library
Servo S(PA_5);                        // Set Pin PA_5 as servo pwm pin
int main() 
{
    while(1)
    {
        S=0;                          //write 0 to servo rotating it to 0 degree
        wait(0.5);                    // wait half second
        S=0.5;                        // write 0.5 to servo rotating it to 90 degree
        wait(0.5);                    // wait half second
        S=1;                          / write 1 to servo rotating it to 180 degree
        wait(0.5);                    // wait half second
    }
}
