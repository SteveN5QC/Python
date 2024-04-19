import machine
import time

led = machine.Pin('LED', machine.Pin.OUT) #configure LED as an output pin a

while True:
    led.value(True)  #turn on the LED
    time.sleep(0.5)  #wait for one second -- Changed to 0.5 sec -- Shorter time on
    led.value(False) #turn off the LED
    time.sleep(0.5) #wait for one second -- Changed to 0.5 sec -- Shorter time off