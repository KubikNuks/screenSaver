import os
import pyautogui

filename = 'screenshot.png'

# Check if the file already exists
if os.path.exists(filename):
    # If it does, add a number to the end of the filename to make it unique
    i = 1
    while True:
        new_filename = f'screenshot_{i}.png'
        if not os.path.exists(new_filename):
            break
        i += 1
    filename = new_filename

# Capture the screen
img = pyautogui.screenshot()



# Save the screenshot to a file
img.save(filename)
