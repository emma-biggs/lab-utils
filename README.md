

# Research Lab Utilities: Python & PsychoPy

A collection of modular, reusable scripts for behavioral and psychophysiological research. This repository provides standardized tools for hardware-software interfacing, stimulus validation, and diagnostic troubleshooting in research environments (fMRI, EEG, and Psychophysics).

## 📂 Project Structure

### 1. Hardware Control & Calibration
* **`calibration/DS7Calibration.py`**:
    * Implements decreasing Inter-Stimulus Intervals (ISI) for ramping up stimulation.
	* Can be used to calibrate the intensity prior to the start of your experiment.
    * Features a class-based structure for easy integration into larger experiment scripts.

### 2. System Diagnostics
* **`diagnostics/test_parallel_port.py`**:
    * Conducts a systematic "sweep" of Data Pins 2–9.
    * Essential for troubleshooting synchronization issues with fMRI triggers or EEG event markers.
* **`diagnostics/check_image_scaling.py`**:
    * Verifies image aspect ratios and native pixel dimensions.
    * Ensures stimuli are displayed without distortion across different lab monitor resolutions using `height` units.