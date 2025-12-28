from machine import Pin, SoftI2C
import ssd1306
from time import sleep

#You can choose any other combination of I2C pins
i2c = SoftI2C(scl=Pin(1), sda=Pin(0))

oled_width = 128
oled_height = 32

oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

#---Turn on the oled---
oled.poweron()
oled.contrast(0)

#---Show Text---
oled.text("...Test Begin...",0,0)
# oled.text("Contrast LV",20,20)
oled.show()
sleep(1)

'''
#---Show Contrast Level---
for contrast_level in range(0,256,1):
    oled.contrast(contrast_level)
    oled.text("LV:{}".format(contrast_level),50,40,1)
    oled.show()
    oled.text("LV:{}".format(contrast_level),50,40,0)
    sleep_us(1)
sleep(1)

#---Fill Screen (clear screen)---
oled.fill(0)
oled.show()
sleep(1)

#---Invert Screen---
oled.text("Color Inverted!",0,5)
oled.invert(1)
oled.show()
sleep(1)
'''
# Scroll Text (Right->Left)
for x in range(0,128):
    oled.fill(0)
    oled.text("Scroll Text", 128 - x, 10)
    oled.show()
    sleep(0.01)

# Scroll Text (Left->Right)
for x in range(0,128):
    oled.fill(0)
    oled.text("Scroll Text",x, 10)
    oled.show()
    sleep(0.01)

#---Draw line---
oled.fill(0)
'''
oled.text("Line",50,10)
oled.hline(0,30,100,1) # Horizontal Line
oled.vline(64,25,60,1) # Vertival Line
oled.show()
sleep(1)


#---Draw a Triangle---
oled.fill(0)
oled.text("Triangle",25,5)
oled.triangle(30, 20, 60, 60, 90, 20, color=1, fill=False) # Outline
oled.show()
sleep(1)
oled.triangle(30, 20, 60, 60, 90, 20, color=1, fill=True) #Filled
oled.show()
sleep(1)

#---Draw a Rectangle---
oled.fill(0)
oled.text("Rectangle",25,5)
oled.rect(3,15,20,20,1,0) # Outline
oled.show()
oled.rect(3,40,20,20,1,1) # Filled
oled.show()
sleep(1)

#---Draw a Round Rectangle---
oled.fill(0)
oled.text("Round Rectangle",5,5)
oled.round_rect(10, 20, 60, 40, 1, filled=False , radius=10) # Outline
oled.show()
sleep(1)
oled.fill(0)
'''
oled.text("...Test End...",0,0)
# oled.text("Contrast LV",20,20)
oled.show()
sleep(1)
oled.fill(0)
oled.show()