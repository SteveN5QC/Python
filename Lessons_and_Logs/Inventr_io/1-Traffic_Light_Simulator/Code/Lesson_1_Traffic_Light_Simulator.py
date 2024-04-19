# import necessary libraries
import machine
import time

# Define GPIO Pins for the LED's
red_pin = machine.Pin(0, machine.Pin.OUT)
yellow_pin = machine.Pin(1, machine.Pin.OUT)
green_pin = machine.Pin(3, machine.Pin.OUT)   # I think this is pin 3 in the diagram I am using

# Function to turn the LED's on in a specific sequence
def traffic_light():
    red_pin.on()
    time.sleep(2)  #Wait 2 seconds
    red_pin.off()
    green_pin.on()
    time.sleep(2)  #Wait 2 seconds
    green_pin.off()
    yellow_pin.on()
    time.sleep(1)  #Wait 1 second
    yellow_pin.off()
    
# Call the traffic light function
traffic_light()
