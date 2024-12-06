import time
import machine
import onewire
import ds18x20
import st7789py as st7789
import neopixel
from utils import setup_display, display_message, read_temperature, check_ldr, update_leds
from bird_image import bird_data

# GPIO Pins Setup
ldr_pin = machine.ADC(26)  # LDR connected to ADC Pin (GP26)
ds_pin = machine.Pin(22)  # DS18B20 Data Pin
led_pin = machine.Pin(14)  # WS2812 LED Data Pin
display_spi = machine.SPI(1, baudrate=40000000, polarity=1, phase=1)

# DS18B20 Sensor Setup
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

# Display Setup
display = st7789.ST7789(display_spi, 240, 240, reset=machine.Pin(20, machine.Pin.OUT), cs=machine.Pin(17, machine.Pin.OUT), dc=machine.Pin(16, machine.Pin.OUT))

# LED Setup
num_leds = 8  # Number of WS2812 LEDs
leds = neopixel.NeoPixel(led_pin, num_leds)

# Constants for Temperature Ranges (in Fahrenheit)
TOO_HOT = 150
WARM = 120
JUST_RIGHT = 90
COOL = 70

# Main Loop
setup_display(display, bird_data)

while True:
    # Check if a drink is on the coaster
    drink_present = check_ldr(ldr_pin)

    if not drink_present:
        display_message(display, "Put a drink on me, human!")
        update_leds(leds, (255, 0, 0))  # Flashing Red
        time.sleep(1)
        continue

    # Check if the temperature sensor is connected
    try:
        temperature = read_temperature(ds_sensor, ds_pin)
    except Exception:
        display_message(display, "Plug in the temperature probe!")
        update_leds(leds, (255, 255, 0))  # Flashing Yellow
        time.sleep(1)
        continue

    # Determine temperature status and update LEDs and display
    if temperature > TOO_HOT:
        display_message(display, f"{temperature:.1f}F: Are you trying to burn your tongue?!")
        update_leds(leds, (255, 0, 0))  # Bright Red
    elif WARM < temperature <= TOO_HOT:
        display_message(display, f"{temperature:.1f}F: This might be sippable, but be careful.")
        update_leds(leds, (255, 165, 0))  # Orange
    elif JUST_RIGHT < temperature <= WARM:
        display_message(display, f"{temperature:.1f}F: Perfect, enjoy it while it lasts.")
        update_leds(leds, (0, 255, 0))  # Green
    elif COOL < temperature <= JUST_RIGHT:
        display_message(display, f"{temperature:.1f}F: Starting to cool down, hurry up!")
        update_leds(leds, (0, 0, 255))  # Blue
    else:
        display_message(display, f"{temperature:.1f}F: This is basically ice-cold at this point!")
        update_leds(leds, (128, 0, 128))  # Purple

    # Small delay before the next loop iteration
    time.sleep(5)