# OpenCV Color Detector

A foundational Python scripting exercise using OpenCV and Pandas to map image pixels to color names. 

This script opens a user-provided image in a desktop window. When the user double-clicks anywhere on the image, the program extracts the pixel's BGR values, calculates the geometric distance against a CSV dataset of known colors, and displays the closest matching color name and exact RGB values on screen.

## Features
* **Interactive UI:** Utilizes OpenCV mouse callback functions to dynamically update the screen based on user clicks.
* **Vectorized Lookup:** Uses NumPy and Pandas to calculate the Manhattan distance between the target pixel and the color dataset.
* **Dynamic Contrast:** Automatically shifts the UI text color to black when clicking on highly luminous pixels (bright colors) to maintain readability.

## Prerequisites
To run this script, you need Python installed along with the following libraries:
* `opencv-python`
* `pandas`
* `numpy`

You can install them via pip:
`pip install opencv-python pandas numpy`

## How to Run
Run the script via the command line, passing your image file using the `-i` flag:

`python color_detection.py -i your_image.jpg`

3. Double-click anywhere on the image to see the color name and RGB values.
4. Press the `Esc` key to close the window and terminate the program.
