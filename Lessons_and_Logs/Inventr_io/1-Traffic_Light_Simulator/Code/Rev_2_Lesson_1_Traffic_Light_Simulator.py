# import necessary libraries
import machine
import time

# Define GPIO Pins for the LED's
# p0 = Pin(0, Pin.OUT)    # create output pin on GPIO0

# WAS: red_pin = machine.Pin(0, machine.Pin.OUT)
red_pin = machine.Pin(16, machine.Pin.OUT)    # Red LED is wired to GP16
# WAS:  yellow_pin = machine.Pin(1, machine.Pin.OUT)
yellow_pin = machine.Pin(17, machine.Pin.OUT)    # Yellow LED is wired to GP17
# WAS:  green_pin = machine.Pin(3, machine.Pin.OUT)   # I think this is pin 3 in the diagram I am using
green_pin = machine.Pin(18, machine.Pin.OUT)     # Green Led is wired to GP18


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
    
    
    
# Use a while loop -- Starting with 5 loops
num = 0
while num<5:
    
    # Call the traffic light function
    
    traffic_light()
    
    # increase num
    
    num +=1

