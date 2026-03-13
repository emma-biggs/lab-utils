#!/usr/bin/env python3


"""
test_parallel_port.py
---------------------
A diagnostic utility to verify Parallel Port communication and 
identify pin mappings for external hardware (e.g., EEG, DS7).

Author: Emma Biggs
"""

from psychopy import parallel, core
import sys

# --- Configuration ---
PORT_ADDRESS = 0x0378 
PULSE_DURATION = 0.5  # Seconds to keep each pin high

def run_diagnostic():
    print(f"--- Starting Parallel Port Diagnostic ---")
    print(f"Target Address: {hex(PORT_ADDRESS)}")
    
    try:
        port = parallel.ParallelPort(address=PORT_ADDRESS)
    except Exception as e:
        print(f"ERROR: Could not open port. Check drivers/address. \n{e}")
        sys.exit()

    print("Success: Port opened. Starting pin sweep (Pins 2-9)...")
    print("Press Ctrl+C to abort.")

    # Reset all pins to low
    port.setData(0)

    # Standard Parallel Ports have 8 Data Pins: 2 through 9
    for pin_index in range(2, 10):
        print(f"Setting Pin {pin_index} HIGH for {PULSE_DURATION}s")
        
        try:
            port.setPin(pin_index, 1)
            core.wait(PULSE_DURATION)
            port.setPin(pin_index, 0)
            core.wait(0.1) # Brief gap between pins
        except Exception as e:
            print(f"Warning: Could not set pin {pin_index}: {e}")

    print("--- Diagnostic Complete: All data pins cycled ---")
    port.setData(0)

if __name__ == "__main__":
    run_diagnostic()