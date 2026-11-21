
# Python Implementation

This directory contains the Python scripts used in the IR Sensor-Based Risk Prediction System.

Python is used for sensor data acquisition, data processing, communication with the VHDL simulation through text files, and visualization of prediction results.

## Files

- **sensor_simulator.py:** Reads sensor data from Arduino through serial communication, processes the values, and writes them into `input.txt`.
- **live_plot.py:** Reads prediction results from `output.txt` and displays them using graphical visualization.
- **test_bnn.py:** Contains an experimental Cocotb testing template for the VHDL design.

## Libraries Used

- PySerial
- Matplotlib
- Cocotb
- Time

## Workflow

Arduino sensor readings → Python processing → `input.txt` → VHDL simulation → `output.txt` → Python visualization.
