from machine import I2C, Pin
from DIYables_MicroPython_LCD_I2C import LCD_I2C
import os
import sys
import requests
import time
from time import sleep
import network
from picozero import pico_led
import gc

pico_led.blink()

# Define the LCD I2C address and dimensions
I2C_ADDR = 0x27
LCD_ROWS = 2
LCD_COLS = 16
delay =2

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

# Initialize LCD
lcd = LCD_I2C(i2c, I2C_ADDR, LCD_ROWS, LCD_COLS)
lcd.set_cursor(0,0)
lcd.print("starting..")

def scroll_message(message):
    # Add spaces to the beginning of the message to make it appear from the right
    message = " " * LCD_COLS + message + " "

    # Scroll through the message
    for i in range(len(message) - LCD_COLS + 1):
        j = i+LCD_COLS
        submessage = message[i:j]
        #lcd.set_cursor(1, i + LCD_COLS)
        lcd.set_cursor(0,0)
        lcd.print(submessage)
        sleep(.5)

def wifi_connect():
    # Wi-Fi credentials
    ssid = 'Teksavvy095z'
    password = 'yell0w123'

    # Connect to network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    lcd.set_cursor(0,0)
    # Connect to your network
    wlan.connect(ssid, password)
    lcd.print("starting...")
    
def get_weather_info():
    print ('Do GC')
    gc.collect()
    print ('get weather info')
    URI="https://api.openweathermap.org/data/3.0/onecall?lat=43.70011&lon=-79.4163&exclude=hourly,minutely,alerts&appid=83af286b5f2f718f49082643a87d4539"
    try:
        response = requests.get(URI)
        print (response)
        data = response.json()
        print (data)
        lcd.set_cursor(0,0)
        lcd.print("starting....")
    except Exception as e:
        print (e)
        return "cannot get weather data"
    
    if response.status_code == 200:
        name = data["timezone"].split("/",1)[1]
        offset = int(data["timezone_offset"]/(60*60))
        sunrise = data["current"]["sunrise"]
        srh = str(time.gmtime(sunrise)[3] + offset)
        srm = str(time.gmtime(sunrise)[3])
        if len(srm) == 1: srm = "0" + srm
        sunset = data["current"]["sunset"]
        ssh = str(time.gmtime(sunset)[3] + offset)
        ssm = str(time.gmtime(sunset)[4])
        if len(ssm) == 1: ssm = "0" + ssm
        temp = int(data["current"]["temp"] - 273.15)
        feels_like = int(data["current"]["feels_like"] - 273.15)
        latest_summary = len(data["daily"]) - 1
        summary = data["daily"][latest_summary]["summary"]

        the_weather = "The temperature is currently " + str(temp) + ". It feels like " + str(feels_like) + "." 
        the_weather = the_weather + " " + summary + ". " 
        the_weather = the_weather + "Sunrise time " + srh + ":" + srm + " and "
        the_weather = the_weather + "Sunset time " + ssh + ":" + ssm
        current_time = str(time.localtime()[3]) + ":"+ str(time.localtime()[4])
        message_scroll = "This is the weather as of " + current_time + " ... " + the_weather
        print ("Test >", message_scroll)
        return message_scroll
    else:
        lcd.set_cursor(0,0)
        lcd.print("cannot get weather data")
        return "cannot get the weather data"

# Start

try:
    wifi_connect()
    lcd.set_cursor(0,0)
    lcd.print("Weather scroll!")
    sleep(2)

    # Define the message to be scrolled
    # message_scroll = "This is a scrolling message with more than 16 characters"
    
    while True:
        print ('get message')
        message_scroll = get_weather_info()
        print ('got message')
        # Scroll the message on the LCD for 10 minutes
        # Assume scroll message = 1 minute long
        lcd.clear()
        for loopcount in range(10):
            scroll_message(message_scroll)
            print ('repeat message')

except KeyboardInterrupt:
    # Turn off the display when the code is interrupted by the user
    print("Keyboard interrupt")
    lcd.backlight_off()
    lcd.display_off()
