def display_message(oled, message):
    oled.fill(0)  # Clear the display
    oled.text(message, 0, 0)  # Display the text
    oled.show()

def update_leds(leds, color):
    leds.fill(color)
    leds.write()

def read_temperature(sensor_pin):
    import onewire, ds18x20
    ds_sensor = ds18x20.DS18X20(onewire.OneWire(sensor_pin))
    roms = ds_sensor.scan()
    if not roms:
        raise Exception("No DS18B20 found")
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    temperature_c = ds_sensor.read_temp(roms[0])
    return (temperature_c * 9 / 5) + 32  # Convert Celsius to Fahrenheit