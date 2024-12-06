# Usage Instructions for Chaotic Coaster

## Overview

The **Chaotic Coaster** is designed to entertain you with snarky comments while monitoring your drink temperature. Follow the steps below to understand how to interact with it.

## Step-by-Step Usage

1. **Powering On**
   - Use the toggle switch to power on the Chaotic Coaster.
   - The display will show the crow character booting up.

2. **Place a Drink on the Coaster**
   - If no drink is detected, the crow will flap its wings and tell you to place a drink on the coaster.
   - Ensure the drink covers the LDR sensor.

3. **Connect the Temperature Probe**
   - Plug in the DS18B20 temperature probe into the 3.5mm jack.
   - If the probe is not connected, the crow will demand that you plug it in.

4. **Temperature Monitoring**
   - Once a drink is detected and the probe is connected, the crow will read the temperature.
   - Depending on the temperature:
     - **Too Hot** (>150°F): The crow will warn you sarcastically about burning your tongue.
     - **Warm** (120°F - 150°F): It will advise caution while sipping.
     - **Just Right** (90°F - 120°F): The crow will encourage you to enjoy your drink.
     - **Cool** (70°F - 90°F): It will prompt you to hurry up before it gets cold.
     - **Too Cold** (<70°F): It will make a comment about the drink being ice-cold.

5. **LED Feedback**
   - The RGB LEDs will change colors based on the temperature status of the drink:
     - **Bright Red**: Too Hot
     - **Orange**: Warm
     - **Green**: Just Right
     - **Blue**: Cool
     - **Purple**: Too Cold

6. **Turning Off**
   - To turn off the Chaotic Coaster, simply switch off the power using the toggle switch.

## Tips

- **Calibration**: If the LDR is too sensitive or not sensitive enough, adjust the threshold in the `check_ldr()` function in `utils.py`.
- **Customization**: You can modify the snarky messages in `utils.py` to personalize the crow's personality.