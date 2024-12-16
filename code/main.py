import time
from machine import Pin, ADC, I2C
import ssd1306
import neopixel
from utils import display_message, update_leds, read_temperature

# GPIO Pin Assignments (updated for RP2040-Zero constraints)
light_sensor = ADC(26)  # 3DU5C phototransistor connected to ADC0 (GPIO26)
temp_sensor = Pin(13)  # DS18B20 temperature sensor data pin
led_pin = Pin(12, Pin.OUT)  # WS2812 LED data pin
mode_switch = Pin(11, Pin.IN)  # Hot/Cold mode switch with external pull-up

# I2C Display Setup
i2c = I2C(0, scl=Pin(5), sda=Pin(4))  # SCL (GPIO5), SDA (GPIO4) for SSD1306
oled = ssd1306.SSD1306_I2C(128, 64, i2c)  # SSD1306 128x64 display

# WS2812 LED Setup
num_leds = 8
leds = neopixel.NeoPixel(led_pin, num_leds)

# Constants for Temperature Ranges (in Fahrenheit)
TOO_HOT = 150
WARM = 120
JUST_RIGHT = 90
COOL = 70
TOO_COLD = 50

# RGB Values for Each Temperature State
COLORS = {
    "too_hot": (255, 0, 0),      # Bright Red
    "warm": (255, 165, 0),      # Orange
    "just_right": (0, 255, 0),  # Green
    "cool": (0, 0, 255),        # Bright Blue
    "too_cold": (0, 255, 255)   # Cyan
}

# Threshold for Light Detection
LIGHT_THRESHOLD = 20000  # Adjust based on testing

def main():
    while True:
        # Read Light Sensor
        light_value = light_sensor.read_u16()
        drink_present = light_value < LIGHT_THRESHOLD

        if not drink_present:
            display_message(oled, "Put a drink on me!")
            update_leds(leds, (255, 0, 0))  # Flashing Red for no drink
            time.sleep(1)
            continue

        # Read Hot/Cold Mode Switch
        is_hot_mode = not mode_switch.value()  # Switch closed (LOW) = Hot Mode, Open (HIGH) = Cold Mode

        # Read Temperature Sensor
        try:
            temperature = read_temperature(temp_sensor)
        except Exception:
            display_message(oled, "Connect temp probe!")
            update_leds(leds, (255, 255, 0))  # Flashing Yellow for missing sensor
            time.sleep(1)
            continue

        # Determine State Based on Mode and Temperature
        if is_hot_mode:
            if temperature > TOO_HOT:
                display_message(oled, f"{temperature}F: Perfectly hot!")
                update_leds(leds, COLORS["too_hot"])
            elif WARM < temperature <= TOO_HOT:
                display_message(oled, f"{temperature}F: Nicely warm.")
                update_leds(leds, COLORS["warm"])
            elif JUST_RIGHT < temperature <= WARM:
                display_message(oled, f"{temperature}F: Cooling down.")
                update_leds(leds, COLORS["just_right"])
            elif COOL < temperature <= JUST_RIGHT:
                display_message(oled, f"{temperature}F: Too cold!")
                update_leds(leds, COLORS["cool"])
            else:
                display_message(oled, f"{temperature}F: Freezing!")
                update_leds(leds, COLORS["too_cold"])
        else:
            if temperature < TOO_COLD:
                display_message(oled, f"{temperature}F: Perfectly cold!")
                update_leds(leds, COLORS["too_cold"])
            elif TOO_COLD <= temperature < COOL:
                display_message(oled, f"{temperature}F: Nicely cool.")
                update_leds(leds, COLORS["cool"])
            elif COOL <= temperature < JUST_RIGHT:
                display_message(oled, f"{temperature}F: Warming up.")
                update_leds(leds, COLORS["just_right"])
            elif JUST_RIGHT <= temperature < WARM:
                display_message(oled, f"{temperature}F: Too warm!")
                update_leds(leds, COLORS["warm"])
            else:
                display_message(oled, f"{temperature}F: Boiling!")
                update_leds(leds, COLORS["too_hot"])

        time.sleep(5)  # Delay before next update

if __name__ == "__main__":
    main()