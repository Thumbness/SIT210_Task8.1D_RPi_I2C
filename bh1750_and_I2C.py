
import smbus
import time
 
# Define some constants from the datasheet
DEVICE     = 0x23 # Default device I2C address
POWER_DOWN = 0x00 # No active state
POWER_ON   = 0x01 # Power on
RESET      = 0x07 # Reset data register value
ONE_TIME_HIGH_RES_MODE = 0x20
 
bus = smbus.SMBus(1)  # Rev 2 Pi uses 1
 
def convertToNumber(data):
  # Simple function to convert 2 bytes of data
  # into a decimal number
    return ((data[1] + (256 * data[0])) / 1.2)
 
def readLight(addr=DEVICE):
    data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE)
    return convertToNumber(data)

while True:
    light = readLight()
    time.sleep(0.5)
    
    if(light <=10):
        print("Too Dark")
    elif(light>20 and light <= 70):
        print("Dark")
    elif(light >70 and light <= 200):
        print("Medium")
    elif(light > 200 and light < 500):
        print("Bright")
    elif(light > 500):
        print("Too Bright")
 
