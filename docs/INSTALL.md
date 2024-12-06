# Installation Instructions for Chaotic Coaster

## Prerequisites

- **Raspberry Pi Pico** with MicroPython installed
- **USB cable** to connect the Raspberry Pi Pico to your computer
- **Fritzing** to view the hardware schematic (optional)
- **Python 3.x** installed on your computer

## Step-by-Step Installation

1. **Clone the Repository**
   
   Clone the Chaotic Coaster project repository from GitHub:
   
   ```sh
   git clone https://github.com/yourusername/chaotic-coaster.git
   cd chaotic-coaster
   ```

2. **Prepare the Raspberry Pi Pico**

   - Ensure that MicroPython is installed on your Pico.
   - Connect your Raspberry Pi Pico to your computer via USB.

3. **Install Dependencies**

   - Navigate to the `code` directory and install the Python dependencies using `requirements.txt`. These are primarily for any local simulation or testing.
   
   ```sh
   cd code
   pip install -r requirements.txt
   ```

4. **Upload Code to Raspberry Pi Pico**

   - Use an IDE like **Thonny** to upload the files to your Pico.
   - Open `main.py` in Thonny, connect to the Raspberry Pi Pico, and save it to the device.
   - Ensure that `utils.py` and `bird_image.py` are also uploaded to the Pico.

5. **Connect Hardware**

   - Follow the wiring diagram in `hardware/fritzing/chaotic_coaster.fzz` to connect all components.

6. **Power On**

   - Once the code is uploaded and hardware is set up, power on the Raspberry Pi Pico using the USB connection or a battery. The Chaotic Coaster should start running.
