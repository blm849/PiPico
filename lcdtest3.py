"""
This Raspberry Pi Pico MicroPython code was developed by newbiely.com
This Raspberry Pi Pico code is made available for public use without any restriction
For comprehensive instructions and wiring diagrams, please visit:
https://newbiely.com/tutorials/raspberry-pico/raspberry-pi-pico-lcd-i2c
"""

from machine import I2C, Pin
from DIYables_MicroPython_LCD_I2C import LCD_I2C
import utime, random

# The I2C address of your LCD (Update if different)
I2C_ADDR = 0x27  # Use the address found using the I2C scanner

# Define the number of rows and columns on your LCD
LCD_ROWS = 2
LCD_COLS = 16

# Initialize I2C
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

# Initialize LCD
lcd = LCD_I2C(i2c, I2C_ADDR, LCD_ROWS, LCD_COLS)

# Setup function
lcd.clear()
lcd.backlight_on()

# Main loop function
while True:
    lcd.clear()
    lcd.set_cursor(0, 0) # Move the cursor to column 3, row 0 (first row)
    lcd.print("Starting Test")
    lcd.set_cursor(3,1) # Move the cursor to column 0, row 1 (second row)
    lcd.print("in 2 seconds")
    utime.sleep(2)
    
    lcd.clear()
    lcd.set_cursor(0, 0) # Move to the beginning of the first row
    lcd.print("Random Number:")
    lcd.set_cursor(14,1)
    lcd.print(str(random.randrange(1,100)))  # Print integer
    lcd.set_cursor(1, 3)  # Move to the beginning of the second row
    utime.sleep(2)
    print("sleeping")
