
# IR Sensor-Based Risk Prediction System

A real-time sensor-based risk analysis system integrating Arduino, Python, and VHDL simulation. The project captures IR sensor readings, processes the data using Python, performs simulated inference through VHDL, and visualizes the resulting risk predictions.

## Overview

This project demonstrates hardware-software integration for sensor-based risk monitoring. IR sensor data is acquired through an Arduino and transmitted to Python over serial communication. Python processes and maps the sensor readings into risk values, which are transferred to a VHDL simulation through text files.

The VHDL inference logic processes the input data and generates prediction scores. Python then reads the simulation output and displays the results using graphical visualization.

## System Architecture

```text
IR Sensor
    |
    v
Arduino
    |
    | Serial Communication
    v
Python Sensor Processing
    |
    | Risk Mapping
    v
input.txt
    |
    v
VHDL Inference Simulation
    |
    v
output.txt
    |
    v
Python Visualization
    |
    v
Risk Analysis Graph
```

## Technologies Used

- **Hardware:** Arduino Uno, IR Sensor
- **Programming:** Python
- **Hardware Description Language:** VHDL
- **Simulation:** Xilinx Vivado
- **Python Libraries:** PySerial, Matplotlib
- **Communication:** Serial Communication and File-Based Data Exchange

## Project Workflow

1. The IR sensor measures proximity-related values.
2. Arduino transmits sensor readings through serial communication.
3. Python receives and processes the sensor data.
4. Sensor readings are mapped into risk categories.
5. Python writes processed values into `input.txt`.
6. The VHDL simulation reads the input data and performs simulated inference.
7. Prediction scores are written into `output.txt`.
8. Python reads the generated output and visualizes the results.

## Risk Classification

Sensor readings are categorized into three risk levels:

| Sensor Value | Risk Category | Risk Percentage |
|---|---|---|
| 37–44 | High Risk | 90–100% |
| 45–800 | Moderate Risk | 11–89% |
| 801–1023 | Low Risk | 0–10% |

The risk mapping is based on the sensor value ranges defined in the project implementation.

## VHDL Simulation

The VHDL module implements simplified inference logic involving:

- Input processing
- Arithmetic-based weight generation
- Dropout-like masking
- ReLU activation
- Output score generation

The inference logic is evaluated using Vivado behavioral simulation.

**Note:** This project uses a simplified simulation-based inference model. It is not a fully trained Bayesian Neural Network, and the implementation does not involve FPGA hardware deployment.

## Python Visualization

Python is used to:

- Receive sensor readings through serial communication
- Process and map sensor values
- Exchange data with the VHDL simulation through text files
- Read prediction outputs
- Generate graphical risk-analysis visualizations

## Repository Structure

```text
IR-Sensor-Risk-Prediction/
│
├── Code/
│   ├── Python/
│   │   ├── sensor_simulator.py
│   │   ├── live_plot.py
│   │   └── test_bnn.py
│   │
│   ├── VHDL/
│   │   ├── bnn_core.vhd
│   │   ├── bnn_tb.vhd
│   │   ├── bnn_pkg.vhd
│   │   └── bnn_pkg1.vhd
│   │
│   └── Data/
│       ├── sample_input.txt
│       └── sample_output.txt
│
├── Research/
│   └── BNN_Research_Paper.pdf
│
├── Reports/
│   ├── College_Project_Report.pdf
│   └── BNN_Development_Log.docx
│
├── Results/
│   └── Python_Risk_Analysis/
│
└── README.md
```

## Results

The project demonstrates the integration of real-time sensor acquisition, Python-based data processing, VHDL simulation, and graphical visualization.

Screenshots of the risk-analysis graphs and project outputs are available in the `Results` directory.

## Limitations

- VHDL inference is simulation-based.
- The inference model uses simplified arithmetic and deterministic masking logic.
- No FPGA hardware deployment was performed.
- The model has not been trained using a conventional machine-learning training pipeline.
- The project focuses on demonstrating sensor integration, data processing, simulation, and visualization.

## Future Enhancements

- Implement a properly trained neural network model.
- Introduce genuine probabilistic inference and Monte Carlo sampling.
- Deploy the inference logic on FPGA hardware.
- Improve sensor calibration and risk classification.
- Develop a more advanced real-time monitoring dashboard.
- Integrate multiple physical sensors.

## Author

**N. Vyshnavi**  
Electronics and Communication Engineering

## Project Focus

Embedded Systems | IoT | Sensor Interfacing | Python | VHDL | FPGA Simulation | Hardware-Software Integration
