### Pin Mapping Chart

| Component                        | Function                | RP2040-Zero Pin | Notes                                   |
|----------------------------------|-------------------------|-----------------|-----------------------------------------|
| **Power Supply**                 | 3.7V LiPo Battery       | 5V              | Battery connects to TP4056 BAT+        |
|                                  | GND                    | GND             | Battery ground connects to TP4056 BAT- |
| **TP4056 Charging Module**       | Output (VOUT)          | 5V              | Powers the system via on/off switch     |
|                                  | GND                    | GND             | Common ground for all components        |
| **System On/Off Switch**         | Toggle between TP4056 and RP2040-Zero | Between TP4056 OUT+ and 5V | Controls power to the microcontroller and peripherals |
|                                  | GND                    | GND             | Common ground                           |
| **3.3V Regulated Power**         | Powers peripherals     | 3.3V            | Provided by onboard regulator           |
| **Temperature Sensor (DS18B20)** | Data                   | GPIO13          | Requires 4.7k ohm pull-up resistor      |
|                                  | VCC                    | 3.3V            | Powers the DS18B20                      |
|                                  | GND                    | GND             | Ground connection                       |
| **SSD1306 Display (I2C)**        | SCK                    | GPIO5 (SCL)     | Serial Clock for I2C                    |
|                                  | SDA                    | GPIO4 (SDA)     | Serial Data for I2C                     |
|                                  | VCC                    | 3.3V            | Powers the display                      |
|                                  | GND                    | GND             | Ground connection                       |
| **Custom WS2812 LED Setup**      | Data                   | GPIO12          | Data pin for controlling LEDs           |
|                                  | VCC                    | 5V              | Powered by the TP4056 via the 5V pin    |
|                                  | GND                    | GND             | Common ground                           |
| **Cup Detection Sensor (3DU5C)** | Analog Input           | ADC0 (GPIO26)   | Voltage divider: Emitter → 10k ohm → GND |
|                                  | Collector              | 3.3V            | Connected to power (VCC)                |
|                                  | Emitter                | ADC0 (GPIO26)   | Analog signal read by microcontroller   |
| **Hot/Cold Mode Switch**         | Digital Input          | GPIO11          | External 10k ohm pull-up resistor to 3.3V |
