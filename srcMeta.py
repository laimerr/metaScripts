import pyautogui
import time
import psutil
import platform
import keyboard  # Import the keyboard library

# Global variable to control the loop
running = True

# Variable to keep track of whether Chrome has been opened
chrome_opened = False

def is_chrome_running():
    for process in psutil.process_iter(['pid', 'name']):
        if 'chrome' in process.info['name'].lower():
            return True
    return False

def open_chrome():
    # Use the appropriate keyboard shortcut to open Google Chrome based on your operating system
    if platform.system() == 'Darwin':  # macOS
        pyautogui.hotkey('command', 'space')  # Spotlight search
        time.sleep(0.5)
        pyautogui.write('Google Chrome')
        pyautogui.press('return')
    elif platform.system() == 'Linux':  # Linux
        pyautogui.hotkey('ctrl', 'alt', 't')  # Open terminal
        time.sleep(0.5)
        pyautogui.write('google-chrome')
        pyautogui.press('return')
    elif platform.system() == 'Windows':  # Windows
        pyautogui.hotkey('win', 'r')  # Run dialog
        time.sleep(0.5)
        pyautogui.write('chrome')
        pyautogui.press('return')
    else:
        print("Unsupported operating system")

def find_and_type_hello():
    try:
        input_field_x, input_field_y = 740, 460
        transfer_button_x, transfer_button_y = 740, 871.1875   # Replace with the actual coordinates of the transfer button
        market_button_x, market_button_y = 843.9765625, 284.390625
        advence_button_x, advance_button_y = 580, 455.5
        firstgue_input_x, firstgue_input_y = 601, 276.203125
        sectgue_input_x, sectgue_input_y = 581, 397.203125
        save_button_x, save_button_y = 601, 734.703125
        additional_button_x, additional_button_y = 870, 720   # Replace with the actual coordinates of the additional button

        

        pyautogui.moveTo(input_field_x, input_field_y, duration=1)
        pyautogui.click()

        pyautogui.typewrite("0.0001")

        time.sleep(3)


        # Move to the transfer button and click
        pyautogui.moveTo(transfer_button_x, transfer_button_y, duration=1)
        pyautogui.click()

        # Wait for 10 seconds
        time.sleep(5)

        # Move to the market button and click
        pyautogui.moveTo(market_button_x, market_button_y, duration=1)
        pyautogui.click()

        # Wait for 10 seconds
        time.sleep(1)

        # Move to the advance button and click
        pyautogui.moveTo(advence_button_x, advance_button_y, duration=1)
        pyautogui.click()

        # Wait for 10 seconds
        time.sleep(1)

        # Move to the firstgue input, select all text, and type "1"
        pyautogui.moveTo(firstgue_input_x, firstgue_input_y, duration=1)
        pyautogui.click()
        pyautogui.keyDown('shift')  # Hold down the Shift key
        pyautogui.press('end')       # Press the End key to select all text
        pyautogui.keyUp('shift')    # Release the Shift key
        pyautogui.typewrite("1")

        # Wait for 10 seconds
        time.sleep(1)

        # Move to the sectgue input, select all text, and type "1"
        pyautogui.moveTo(sectgue_input_x, sectgue_input_y, duration=1)
        pyautogui.click()
        pyautogui.keyDown('shift')  # Hold down the Shift key
        pyautogui.press('end')       # Press the End key to select all text
        pyautogui.keyUp('shift')    # Release the Shift key
        pyautogui.press('backspace')   # Delete the selected text
        pyautogui.typewrite("1")

        # Wait for 10 seconds
        time.sleep(1)

        # Move to the save button and click
        pyautogui.moveTo(save_button_x, save_button_y, duration=1)
        pyautogui.click()

        # Wait for 10 seconds
        time.sleep(1)

        # Move to the additional button and click
        pyautogui.moveTo(additional_button_x, additional_button_y, duration=1)
        pyautogui.click()

        time.sleep(120)

    except KeyboardInterrupt:
        print("Script stopped by user.")

def coredao_click():
    global running, chrome_opened
    try:
        radius = 50
        center_x, center_y = pyautogui.size().width // 2, pyautogui.size().height // 2
        angle = 0

        while running:
            if not chrome_opened:
                open_chrome()
                chrome_opened = True

            x = int(center_x + radius * (1 - angle))
            y = int(center_y + radius * angle)

            pyautogui.moveTo(x, y, duration=1)

            angle = (angle + 0.01) % (2 * 3.14159)

            time.sleep(3)

            find_and_type_hello()

    except KeyboardInterrupt:
        print("Script stopped by user.")
