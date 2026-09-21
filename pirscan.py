from machine import Pin
from time import sleep

LED0 = Pin(0, Pin.OUT)
LED25 = Pin(25, Pin.OUT)
PIR_sensor = Pin(15, Pin.IN, Pin.PULL_UP)
LED0.low()
LED25.low()
sleep(3)

while True:
   print(PIR_sensor.value())
   if PIR_sensor.value() == 0:
       print("Motion Detected.-> LED is now ON")
       LED0.high()
       LED25.high()
       sleep(1)
   else:
       print("No motion detected -> LED is OFF")
       LED0.low()
       LED25.low()
       sleep(1)