from machine import Pin, ADC
from time import sleep, ticks_ms

# LED pins
led_up = Pin(16, Pin.OUT)    # D1
led_down = Pin(17, Pin.OUT)  # D2
led_left = Pin(18, Pin.OUT)  # D3
led_right = Pin(19, Pin.OUT) # D4

# Joystick inputs
joystick_x = ADC(34)  # X-axis
joystick_y = ADC(35)  # Y-axis
button = ADC(36)      # Button (assuming active low)

# Thresholds
CENTER = 512
THRESHOLD = 150

# Button double-click detection variables
last_press_time = 0
click_count = 0
DOUBLE_CLICK_DELAY = 500  # Max time between clicks in ms

def clear_leds():
    led_up.off()
    led_down.off()
    led_left.off()
    led_right.off()

def all_leds_on():
    led_up.on()
    led_down.on()
    led_left.on()
    led_right.on()

while True:
    # Read joystick values
    x_val = joystick_x.read()
    y_val = joystick_y.read()
    
    # Handle button press (active low)
    if button.read() == 0:  # Button pressed
        current_time = ticks_ms()
        
        # Check if this is the first click or a double click
        if current_time - last_press_time < DOUBLE_CLICK_DELAY:
            click_count += 1
        else:
            click_count = 1
            
        last_press_time = current_time
        
        # Wait for button release (debounce)
        while button.read() == 0:
            sleep(0.01)
        
        # If double click detected
        if click_count == 2:
            all_leds_on()
            sleep(2)
            clear_leds()
            click_count = 0  # Reset counter
            continue
    
    # Normal joystick LED control
    clear_leds()
    
    # X-axis control
    if x_val < CENTER - THRESHOLD:
        led_left.on()
    elif x_val > CENTER + THRESHOLD:
        led_right.on()
    
    # Y-axis control
    if y_val < CENTER - THRESHOLD:
        led_up.on()
    elif y_val > CENTER + THRESHOLD:
        led_down.on()
    
    sleep(0.1)