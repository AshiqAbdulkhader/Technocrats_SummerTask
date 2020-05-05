## Arduino I2C

I2C is a communication protocol used in electronic circuits which require communication between a master and one or more slaves or between multiple masters. 
It can be easily implemented by using only 2 wires for communication. The number of devices that can be connected to the master depends on the number of bits used for addressing.
2^n devices can be connected to a master which uses an n bit addressing.

The Two Wires are called Serial Clock (SCL) and Serial Data (SDA) . 
The data is transferred in sequences of 8 bits. The I2c follows the following procedure.First the master sends a start condition followed by the address of the slave device. 
The slave device sends an acknowledgement. Then master sends the address of the internal register of the slave device which is followed by transmission of data and then a stop condition.
