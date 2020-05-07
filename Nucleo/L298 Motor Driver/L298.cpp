#include "mbed.h"         // include mbed library
                       //defining input pins of L298
DigitalOut in1(PA_2);   //input 1
DigitalOut in2(PA_3);   //input 2
DigitalOut in3(PB_2);   //input 3
DigitalOut in4(PB_3);   //input 4

void right(void)         //fuction to move right
{
    in1=1;
    in2=0;
    in3=1;
    in4=0;
}
void left(void)         //fuction to move left
{
    in1=0;
    in2=1;
    in3=0;
    in4=1;
}
void forward(void)      //fuction to move forward
{
    in1=0;
    in2=1;
    in3=1;
    in4=0;
}
void backward(void)    //fuction to move backward
{
    in1=1;
    in2=0;
    in3=0;
    in4=1;
}
void stop(void)
{
    in1=0;
    in2=0;
    in3=0;
    in4=0;
}

int main() 
{
    while(1)
    {
       forward();           
       wait(1);
       backward();
       wait(1);
       left();
       wait(1);
       right();
       wait(1); 
    }

}
