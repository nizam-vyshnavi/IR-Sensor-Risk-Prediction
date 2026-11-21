# VHDL Implementation

This directory contains the VHDL source files used for the behavioral simulation of the risk prediction system.

The VHDL design processes sensor input data and generates risk prediction outputs using a simplified inference logic.

## Files

- **bnn_core.vhd:** Main VHDL module containing the prediction logic.
- **bnn_tb.vhd:** Testbench used to simulate and verify the VHDL module.
- **bnn_pkg.vhd:** VHDL package containing supporting definitions.
- **bnn_pkg1.vhd:** Additional package file used in the project.

## Simulation

The VHDL modules were simulated using Xilinx Vivado. The design demonstrates the hardware-side processing and prediction workflow.

> Note: This project uses a simplified simulation-based prediction model and does not represent a fully trained Bayesian Neural Network or physical FPGA implementation.
