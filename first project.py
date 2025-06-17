#first project
#blink leds

from adafruit_circuitplayground import cp
import time

while True:
    cp.red_led = True
    time.sleep(.5)
    cp.red_led = False
    time.sleep(.5)
    #neopixel time!
    cp.pixels[0] = (0, 0, 255) #Blue
    cp.pixels[1] = (255, 255, 255) #White
    time.sleep(.5)
    cp.pixels[0] = (0, 0, 0) #all off
    cp.pixels[1] = (0, 0, 0) #all off
    time.sleep(.5)
