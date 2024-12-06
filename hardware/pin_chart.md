### Chaotic Coaster Pin Chart

| Component                                     | Function                | Pico Pin            | Notes                                                                         |
| --------------------------------------------- | ----------------------- | ------------------- | ----------------------------------------------------------------------------- |
| **Power Supply**                              | Battery (3.7V LiPo)     | BAT+, BAT- (TP4056) | Battery connects to BAT+ and BAT- on TP4056 to manage charging and protection |
| **Charging Module (TP4056)**                  | Charging Input (5V)     | VBUS, GND           | VBUS (5V from Pico USB) to IN+, GND to IN- of TP4056                          |
|                                               | Power Output            | VSYS, GND           | OUT+ to VSYS, OUT- to GND to power the Pico from battery or USB seamlessly    |
| **Temperature Sensor (DS18B20)**              | Data                    | GP22                | Requires 4.7k ohm pull-up resistor between Data and 3.3V                      |
|                                               | VCC                     | 3V3                 | Powers the DS18B20                                                            |
|                                               | GND                     | GND                 | Ground connection                                                             |
| **3.5mm Jack**                                | Tip (Data)              | GP22                | Same data pin as DS18B20                                                      |
|                                               | Ring (VCC)              | 3V3                 | Supplies power to the sensor                                                  |
|                                               | Sleeve (GND)            | GND                 | Common ground                                                                 |
| **SPI Display (1.3" 240x240)**                | GND                     | GND                 | Ground connection                                                             |
|                                               | VCC                     | 3V3                 | Powers the display                                                            |
|                                               | SCL (SPI Clock)         | GP18                | Serial Clock                                                                  |
|                                               | SDA (SPI Data)          | GP19                | Serial Data (acts as MOSI)                                                    |
|                                               | RES (Reset)             | GP20                | Resets the display                                                            |
|                                               | DC (Data/Command)       | GP16                | Data/Command signal                                                           |
|                                               | BLK (Backlight Control) | GP17                | Controls backlight (optional)                                                 |
| **Custom WS2812 LED Setup**                   | Data                    | GP14                | Data pin for controlling the custom WS2812 LEDs                               |
|                                               | VCC                     | VSYS                | Power supply to all LEDs                                                      |
|                                               | GND                     | GND                 | Ground connection                                                             |
| **Cup Detection Sensor (Light Sensor - LDR)** | Analog Input            | GP26 (ADC)          | Voltage divider with LDR and 10k ohm resistor to detect light level changes   |
|                                               | VCC                     | 3V3                 | Powers the LDR in the voltage divider                                         |
|                                               | GND                     | GND                 | Common ground                                                                 |

### Notes on Changes

- **TP4056 Wiring**: The TP4056 module is powered through the **VBUS** pin from the Pico, which receives **5V** when the USB cable is connected. This allows you to charge the battery through the **Pico's USB port**.
- **Power Supply Adjustments**: The battery connects directly to **BAT+ and BAT-** on the TP4056 for charging. The **OUT+ and OUT-** of the TP4056 are connected to **VSYS** and **GND** on the Pico, respectively, providing power seamlessly from either USB or battery.
- **SPI Display Pin Adjustments**: The pin labels have been updated to match the labels on the display module. **SCL** is used for the SPI clock, and **SDA** is used for the SPI data line. **BLK** is used for backlight control, and **RES** is for the reset function.
- **Light Sensor for Cup Detection**: Added **LDR** (Light Dependent Resistor) as the cup detection sensor, using a voltage divider connected to **GP26** (ADC) to read changes in light levels. This sensor can determine if a drink is placed on the coaster by detecting whether light is blocked.
- **LED Strip Update**: To simplify the setup and minimize components, **WS2812 addressable LEDs** are recommended. These are easy to control using a single data pin, require a lower power supply (3.3V or 5V), and do not require MOSFETs or additional circuitry.
- **Single USB Port**: The **USB port on the Pico** serves for both battery charging and programming, simplifying the design and allowing only one external USB connection.
