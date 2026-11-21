import serial
import time

# Adjust this to your Arduino COM port and baud rate
SERIAL_PORT = 'COM5'  # or '/dev/ttyUSB0'
BAUD_RATE = 9600

# File to write the sensor values for VHDL simulation to read
INPUT_FILE = 'C:/BNN_FINAL/input.txt'

# Risk mapping function based on sensor value
def map_risk(value):
    # Clamp to avoid unexpected values
    value = max(37, min(value, 1023))

    if value <= 44:
        # High Risk: 37–44 → 100% to 90%
        return int(100 - ((value - 37) / (44 - 37)) * 10)
    elif value <= 800:
        # Moderate Risk: 45–800 → 89% to 11%
        return int(89 - ((value - 45) / (800 - 45)) * 78)
    else:
        # Low Risk: 801–1023 → 10% to 0%
        return int(max(0, 10 - ((value - 801) / (1023 - 801)) * 10))

def main():
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print(f"Connected to Arduino on {SERIAL_PORT} at {BAUD_RATE} baud.")
        time.sleep(2)  # wait for Arduino to reset

        while True:
            line_bytes = ser.readline()
            try:
                line = line_bytes.decode('utf-8').strip()
            except UnicodeDecodeError:
                continue

            if not line:
                continue

            parts = line.split(',')
            if len(parts) != 10:
                print(f"Warning: Expected 10 values, got {len(parts)} - skipping line")
                continue

            try:
                values = [int(x) for x in parts]
                mapped_values = [map_risk(v) for v in values]
            except ValueError:
                print(f"Warning: Could not convert all values to int - skipping line")
                continue

            print(f"Raw values: {values}")
            #print(f"Mapped Risk % values: {mapped_values}")

            with open(INPUT_FILE, 'w') as f:
                f.write(' '.join(str(v) for v in mapped_values))

            time.sleep(0.1)

    except serial.SerialException as e:
        print(f"Serial connection error: {e}")
    except KeyboardInterrupt:
        print("Exiting...")

if __name__ == "__main__":
    main()
