#!/usr/bin/env python3


"""
DS7_calibration.py
-----------------
A utility for electrical stimulation intensity calibration using 
the Digitimer DS7A stimulator via Parallel Port.

The electrical stimulation is a wave that ramps up.
It consists of pulses with decreaseing ISIs.

Author: Emma Biggs
License: MIT
"""

from __future__ import division
from psychopy import visual, core, event, parallel
import logging

# --- Configuration ---
PORT_ADDRESS = 0x0378  # Standard LPT1 address
STIM_PIN = 5           # Specific pin for DS7 trigger
PULSE_WIDTH = 0.002    # 2ms pulse width
TOTAL_TRAIN_DUR = 0.800 # Total duration of the stimulus train

class StimCalibration:
    def __init__(self, port_address, pin):
        """Initializes the parallel port and stimulus parameters."""
        try:
            self.port = parallel.ParallelPort(address=port_address)
            self.pin = pin
            self.port.setData(0)
            logging.info(f"Parallel port initialized at {hex(port_address)}")
        except Exception as e:
            logging.error(f"Could not initialize Parallel Port: {e}")
            raise

    def deliver_train(self, initial_isi=0.250):
        """
        Delivers a train of pulses with a geometrically decreasing 
        Inter-Stimulus Interval (ISI) to reach tetany-like sensations.
        """
        shock_clock = core.Clock()
        current_isi = initial_isi
        
        while shock_clock.getTime() < TOTAL_TRAIN_DUR:
            self.port.setPin(self.pin, 1)
            core.wait(PULSE_WIDTH)
            self.port.setPin(self.pin, 0)
            
            core.wait(current_isi)
            
            # Accelerate the pulse train
            if current_isi > PULSE_WIDTH:
                current_isi /= 1.55
        
        # Ensure pin is low at the end
        self.port.setPin(self.pin, 0)

def main():
    # Setup Window
    win = visual.Window(
        size=(1024, 768), fullscr=True, monitor='testMonitor', 
        color=[0,0,0], colorSpace='rgb', blendMode='avg'
    )
    
    # UI Elements
    fixation = visual.GratingStim(win, color='black', tex=None, mask='circle', size=0.1)
    cue = visual.GratingStim(win, color='blue', tex=None, mask='circle', size=0.1)
    
    # Initialize Stimulator
    stimulator = StimCalibration(PORT_ADDRESS, STIM_PIN)
    
    print("Calibration Started. Press 'RIGHT' to stimulate, 'S' to exit.")
    
    running = True
    while running:
        fixation.draw()
        win.flip()

        keys = event.getKeys()
        if 'right' in keys:
            # Visual Feedback
            cue.draw()
            win.flip()
            
            # Execute Stimulus
            stimulator.deliver_train()
            
            # Brief pause to prevent accidental double-triggers
            core.wait(0.5) 
            
        elif 's' in keys:
            running = False

    win.close()
    core.quit()

if __name__ == "__main__":
    main()