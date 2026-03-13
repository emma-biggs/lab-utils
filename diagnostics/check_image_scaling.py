#!/usr/bin/env python3


"""
check_image_scaling.py
------------------------
Utility to verify image scaling and aspect ratios across different 
monitor resolutions. Ensures stimuli are not distorted.

Author: Emma Biggs
"""

from psychopy import visual, core, event

# --- Configuration ---
TEST_IMAGE = 'ContextB.bmp'
DISPLAY_DURATION = 5.0  # Seconds to show image
WIN_SIZE = (1280, 1024)

def check_image():
    # Setup window using 'height' units for scaling consistency
    win = visual.Window(
        size=WIN_SIZE, fullscr=True, monitor='testMonitor', 
        color=[-1,-1,-1], units='height'
    )
    
    # Initialize ImageStim
    # Note: Setting size=None will display the image at its native aspect ratio
    stim = visual.ImageStim(win=win, image=TEST_IMAGE, size=None)
    
    # Calculate aspect ratio for the console
    orig_size = stim.size
    aspect_ratio = orig_size[0] / orig_size[1]
    
    print(f"--- Stimulus Diagnostic ---")
    print(f"Image: {TEST_IMAGE}")
    print(f"Native Size (pixels): {orig_size}")
    print(f"Aspect Ratio: {aspect_ratio:.2f}")
    
    # Instructions for the user
    instr = visual.TextStim(win, text="Press 'SPACE' to exit", pos=(0, -0.4), height=0.03)

    timer = core.Clock()
    while timer.getTime() < DISPLAY_DURATION:
        stim.draw()
        instr.draw()
        win.flip()
        
        if 'space' in event.getKeys():
            break
            
    win.close()
    core.quit()

if __name__ == "__main__":
    check_image()