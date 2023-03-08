import os
import pyautogui
import numpy as np
import tkinter as tk



def take_screenshot():

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
    img_np = np.array(img)


# Save the screenshot to a file
    img.save(filename)
    print(f'Screenshot saved as {filename}')

def nowy_prz():
    button3 = tk.Button(root, text='Take Screenshot', command=on_click)
    button_list.append(button3)
    button3.pack()
# Create a function to handle button clicks
def on_click():
    take_screenshot()

def remove_button():
    if len(button_list) > 1:
        button = button_list.pop()
        button.destroy()
# Keep track of buttons
button_list = []
# Create the GUI window
root = tk.Tk()
root.title('Screenshot')

# Create the screenshot button
button = tk.Button(root, text='Take Screenshot', command=on_click)
button.pack()

add_button = tk.Button(root, text='Dodaj przycisk',command=nowy_prz)
button_list.append(add_button)
add_button.pack()

button4 = tk.Button(root, text='Usun przycisk',command=remove_button)
button4.pack()
 
# Start the GUI loop
root.mainloop()
