#include<Wire.h>                      //Include Wire Library
const int add=0x68;                    //I2C address of MPU-6050 
int16_t Ax,Ay,Az,Gx,Gy,Gz,T;           //variables for storing values from 3 axis accelerometer,3 axis Gyro and temperature
                                       // can only store a 16 bit integer
void setup() 
{
  Wire.begin();                        //start I2C Communication
  Wire.beginTransmission(add);
  Wire.write(0x6B);                    //write address of internal register
  Wire.write(0);                        //Set value to zero, disable sleep mode
  Wire.endTransmission(true);
  Serial.begin(9600);                 //start serial communication

}

void loop() 
{
  Wire.beginTransmission(add);       //start transmission
  Wire.write(0x3B);                  //write address of starting internal registry(0x3B is X axis of accelerometer)
  Wire.endTransmission(false);
  Wire.requestFrom(add,14,true);      //request 14 registers, 2 register per each value
  Ax=Wire.read()<<8|Wire.read();     
  Ay=Wire.read()<<8|Wire.read();      // reads data from 2 registers and shifts it into 8 bits.
  Az=Wire.read()<<8|Wire.read();      // this is done because most arduino based on 16 bit. 
  T=Wire.read()<<8|Wire.read();       // and if you try to store data of higher bits in 16 bit,
  Gx=Wire.read()<<8|Wire.read();      // it could cause integer overflow
  Gy=Wire.read()<<8|Wire.read();
  Serial.println("Accelerometer X = "); 
  Serial.print(Ax);
  Serial.println("Accelerometer Y = ");  //print the data
  Serial.print(Ay);
  Serial.println("Accelerometer Z = "); 
  Serial.print(Az);
  Serial.println("Gyro X = "); 
  Serial.print(Gx);
  Serial.println("Gyro X = "); 
  Serial.print(Gy);
  Serial.println("Gyro X = "); 
  Serial.print(Gz);
  Serial.println("Temperature = ");
  Serial.print(T);
  delay(500);
  
}
