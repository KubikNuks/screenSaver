import os
import pyautogui
import numpy as np
import tkinter as tk
import cv2
import threading

def take_video():
    # Set up the screen size
    SCREEN_SIZE = pyautogui.size()

    # Set up the video writer
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("output.avi", fourcc, 10.0, (SCREEN_SIZE))
   

    while True:
        # Capture the screen
        img = pyautogui.screenshot()

        # Get the cursor position and RGB color
        x, y = pyautogui.position()
        r, g, b = pyautogui.pixel(x, y)
        

        # Convert the image to a numpy array
        frame = np.array(img)

        # Resize the frame to the screen size
        frame = cv2.resize(frame, SCREEN_SIZE)

        cv2.circle(frame, (x, y), 10, (0, 0, 255), -1)
        

        # Write the frame to the video file
        out.write(frame)

        # Exit the loop when the 'q' key is pressed
        if not recording:
            break

    out.release()
    cv2.destroyAllWindows()

def stop_recording():
        global recording
        recording = False
        
def start_recording():
    global recording
    recording = True
    screen_thread = threading.Thread(target=take_video)
    screen_thread.start()
    

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

# Create the add button
add_button = tk.Button(root, text='Dodaj przycisk',command=nowy_prz)
button_list.append(add_button)
add_button.pack()

# Create the remove button
button4 = tk.Button(root, text='Usun przycisk',command=remove_button)
button4.pack()

# Create the video button
button5 = tk.Button(root,text='Nagraj',command=start_recording)
button5.pack()

# Create the "Stop Recording" button
button6 = tk.Button(root,text='Stop Recording',command=stop_recording)
button6.pack()
# Start the GUI loop
root.mainloop()
