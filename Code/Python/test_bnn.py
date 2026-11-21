import cocotb
from cocotb.triggers import Timer
from cocotb.handle import Force
import random

@cocotb.test()
async def run_bnn_test(dut):
    cocotb.log.info("Starting BNN test with cocotb")

    # Example: you would normally drive inputs and observe outputs
    await Timer(100, units="ns")

    # Add your logic here to simulate input sensor values and observe output signals
    # For example, if you have signals like: dut.input0 <= val
