import machine
import time

# Define GPIO pins for the LED and button -- 5/3/2024 Based on Lesson 4 Circuit
led_pin = machine.Pin(3, machine.Pin.OUT) # WAS 14
button_pin = machine.Pin(8, machine.Pin.IN, machine.Pin.PULL_DOWN) # WAS 15


# Function to measure reaction time
def reaction_time_tester():
    time.sleep(5)
    led_pin.on()  # Turn on the LED
    start_time = time.ticks_ms()  # Get start time in milliseconds

    # Wait for button press
    while True:
        if button_pin.value() == 1:
            end_time = time.ticks_ms()  # Get end time in milliseconds
            reaction_time = end_time - start_time  # Calculate reaction time
            print('Reaction Time:', reaction_time, 'ms')
            break

    led_pin.off()  # Turn off the LED
    
# Call the function to start the reaction time tester
while True:   # Added loop to make it repeat
    reaction_time_tester()