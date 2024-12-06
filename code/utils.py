def setup_display(display, bird_data):
    display.fill(st7789.BLACK)
    display.blit_buffer(bird_data, 0, 0, 240, 240)  # Draw the bird image at the beginning
    display.show()

def display_message(display, message):
    display.fill(st7789.BLACK)
    display.text(message, 20, 120)  # Adjust as needed to center text
    display.show()

def read_temperature(ds_sensor, ds_pin):
    ds_sensor.convert_temp()
    time.sleep_ms(750)  # Wait for conversion
    temperature_celsius = ds_sensor.read_temp(ds_pin)
    return (temperature_celsius * 9 / 5) + 32  # Convert to Fahrenheit

def check_ldr(ldr_pin):
    light_value = ldr_pin.read_u16()
    # Threshold to determine if a drink is present (adjust this as needed)
    return light_value < 20000  # Lower values indicate less light, hence a drink present

def update_leds(leds, color):
    leds.fill(color)
    leds.write()