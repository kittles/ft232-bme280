#from pyftdi.ftdi import Ftdi
#import pyftdi.gpio as gp
#import time
#usleep = lambda x: time.sleep(x/1000000.0)
#Ftdi.show_devices()





from time import sleep
from pyftdi.spi import SpiController
from bme280 import Bme280spi
ctrl = SpiController()
# NOTE you gotta make sure your connecting to the right usb device
ctrl.configure('ftdi://ftdi:232h/1')  # Assuming there is only one FT232H.
spi = ctrl.get_port(0)  # Assuming D3 is used for chip select.
spi.set_frequency(1000000)
bme280 = Bme280spi(spi)

while True:
    print('reading:')
    print(bme280.read())
    # put it in the db
    sleep(5)







#gpio = gp.GpioAsyncController()
#gpio.configure('ftdi:///1', direction=0xFF)
#
#def step ():
#    gpio.write(0b00000000)
#    usleep(1)
#    gpio.write(0b00000001)
#    usleep(1)
#    gpio.write(0b00000000)
#    usleep(1)
#
#while 1:
#    step()


## all output set low
#gpio.write(0x00)
#print(bin(gpio.read()))
## all output set high
#gpio.write(0x76)
#print(bin(gpio.read()))
## all output set high, apply direction mask
#gpio.write(0xFF & gpio.direction)
## all output forced to high, writing to input pins is illegal
#gpio.write(0xFF)  # raises an IOError
#gpio.close()
