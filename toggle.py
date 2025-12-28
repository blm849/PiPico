from picozero import LED, Button, pico_led

led = LED(15)
button = Button(14)

pico_led.blink()
button.when_pressed = led.toggle