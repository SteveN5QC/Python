import machine
import time

led = machine.Pin('LED', machine.Pin.OUT) #configure LED as an output pin a

while True:
    led.value(True)  #turn on the LED
    time.sleep(1)  #wait for one second
    led.value(False) #turn off the LED
    time.sleep(1) #wait for one second