# Chaotic Coaster

The **Chaotic Coaster** is an interactive and playful smart coaster powered by a Raspberry Pi Pico. It features a snarky crow character that gives you temperature readings of your drink, LED lighting effects, and animated visuals to make every sip entertaining.

## Features
- **Temperature Monitoring**: Displays the temperature of your drink using a thermometer probe.
- **Animated Bird Character**: Displays snarky messages and playful graphics based on drink temperature.
- **RGB LED Effects**: LEDs change colors based on temperature status.

## Hardware Components
- **Raspberry Pi Pico**
- **WS2812 LEDs**
- **TP4056 Charging Module**
- **1.3" SPI Display (240x240)**
- **DS18B20 Temperature Sensor**
- **LDR for Cup Detection**

## Project Structure
- **code/**: Contains all scripts for running the coaster.
- **hardware/**: Hardware schematics, Fritzing files, and pin charts.
- **assets/**: Images, animations, and logos used in the project.
- **docs/**: Documentation files for installation, usage, and contribution.

## Getting Started
1. **Hardware Setup**: Refer to `hardware/fritzing/chaotic_coaster.fzz` for the wiring and component layout.
2. **Software Setup**: Follow the instructions in `docs/INSTALL.md` to set up the Raspberry Pi Pico.
3. **Running the Project**: Upload `code/main.py` to your Pico and power on the device.

## License
This project is licensed under a mixed-license approach - see the `LICENSE` file for details.
