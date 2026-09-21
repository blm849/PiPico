import sys
sys.path.append('/home/pi/pico')
import machine
#from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

# Display the first message
lcd.clear()
lcd.message("Hello, World!")
sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)

lcd.clear()
lcd.message("Hello, World!")
lcd = LCD(i2c)

# Display the first message
lcd_api.clear()
lcd_api.message("Hello, World!")
