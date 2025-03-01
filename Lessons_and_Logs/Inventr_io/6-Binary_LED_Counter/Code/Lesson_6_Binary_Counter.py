import machine
import time

# Define GPIO pins for the 4 LEDs
led_pins = [
    machine.Pin(0, machine.Pin.OUT),
    machine.Pin(1, machine.Pin.OUT),
    machine.Pin(2, machine.Pin.OUT),
    machine.Pin(3, machine.Pin.OUT)
]
button_pin = machine.Pin(8, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Initialize LED states for 4 LEDs
led_states = [0] * len(led_pins)

# Function to update LED states
def update_led_states():
    for i, led in enumerate(led_pins):
        if led_states[i] == 1:
            led.on()
        else:
            led.off()
            
            
            
# Function to create a padded binary string
def padded_binary_string(value, length):
    binary_str = bin(value).replace("0b", "")
    while len(binary_str) < length:
        binary_str = '0' + binary_str
    return binary_str

# Function to increment binary counter
def increment_counter():
    # Convert LED states to integer
    binary_value = int(''.join(map(str, led_states)), 2)
    binary_value += 1
    # If value is 16 (10000 in binary), reset to 0
    if binary_value >= 16:
        binary_value = 0
    binary_string = padded_binary_string(binary_value, len(led_pins))

    # Update LED states
    for i, bit in enumerate(binary_string):
        led_states[i] = int(bit)
        
        
# Main loop
while True:
    if button_pin.value() == 1:
        increment_counter()
        update_led_states()
        time.sleep(0.2)  # Button debounce delay

        