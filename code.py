import time
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP13, echo_pin=board.GP14)

while True:
    print((sonar.distance,))
    time.sleep(0.1)
