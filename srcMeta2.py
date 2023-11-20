import pyautogui
import time
import psutil
import platform
import keyboard  # Import the keyboard library

# Global variable to control the loop
running = True

# Variable to keep track of whether Chrome has been opened
chrome_opened = False

counter = 10

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
    global counter  # Declare counter as a global variable
    try:
        frst_btn_x, frst_btn_y = 280, 402
        sec_btn_x, sec_btn_y = 650, 608.5
        select_btn_x, select_btn_y = 650, 508.5
        chooseBnb_x, chooseBnb_y = 650, 590.5
        btn_conf_x, btn_conf_y = 550, 590.5
        # frst_input_x, frst_input_y = 550, 340.796875
        save_button_x, save_button_y = 550, 800.796875
        slider_x, slider_y = 720.40234375, 401.203125
        saveM_button_x, saveM_button_y = 758, 696.40625
        third_btn_x, third_btn_y = 280, 502
        borrow_btn_x, borrow_btn_y = 642, 215.5
        fourth_btn_x, fourth_btn_x = 280, 302
        deposts_btn_x, deposts_btn_y = 642, 215.5
        max_btn_x, max_btn_y = 720.40234375, 580.5
        deposit_btn_x, deposit_btn_y = 500, 690.5

        newAccount_btn_x, newAccount_btn_y = 1300, 70
        selectAccount_btn_x, selectAccount_btn_y = 1100, 110
        chooseAcc_btn_x, chooseAcc_btn_y = 1100, 250
        closeModal_btn_x, closeModal_btn_y = 900, 200

        appDep_btn_x, appDep_btn_y = 544, 595
        next_btn_x, next_btn_y = 750.40234375, 640.5


        

        pyautogui.moveTo(frst_btn_x, frst_btn_y, duration=1)
        pyautogui.click()

        time.sleep(1)

        pyautogui.moveTo(sec_btn_x, sec_btn_y, duration=1)
        pyautogui.click()

        time.sleep(1)

        pyautogui.moveTo(select_btn_x, select_btn_y, duration=1)
        pyautogui.click()

        time.sleep(1)

        pyautogui.moveTo(chooseBnb_x, chooseBnb_y, duration=1)
        pyautogui.click()

        time.sleep(1)

        pyautogui.moveTo(btn_conf_x, btn_conf_y, duration=1)
        pyautogui.click()

        time.sleep(1)

        pyautogui.moveTo(slider_x, slider_y, duration=1)
        pyautogui.click()

        time.sleep(1)

        pyautogui.moveTo(save_button_x, save_button_y, duration=1)
        pyautogui.click()

        time.sleep(17)

        pyautogui.moveTo(saveM_button_x, saveM_button_y, duration=1)
        pyautogui.click()

        time.sleep(15)

        pyautogui.moveTo(third_btn_x, third_btn_y, duration=1)
        pyautogui.click()

        time.sleep(1)

        pyautogui.moveTo(borrow_btn_x, borrow_btn_y, duration=1)
        pyautogui.click()

        time.sleep(1)

        pyautogui.moveTo(slider_x, slider_y, duration=1)
        pyautogui.click()

        time.sleep(1)

        pyautogui.moveTo(save_button_x, save_button_y, duration=1)
        pyautogui.click()

        time.sleep(16)

        pyautogui.moveTo(saveM_button_x, saveM_button_y, duration=1)
        pyautogui.click()

        time.sleep(12)

        pyautogui.moveTo(fourth_btn_x, fourth_btn_x, duration=1)
        pyautogui.click()
        time.sleep(1)

        pyautogui.moveTo(deposts_btn_x, deposts_btn_y, duration=1)
        pyautogui.click()

        time.sleep(1)

        pyautogui.moveTo(appDep_btn_x, appDep_btn_y, duration=1)
        pyautogui.click()

        time.sleep(7)

        pyautogui.moveTo(next_btn_x, next_btn_y, duration=1)
        pyautogui.click()

        time.sleep(1)

        pyautogui.moveTo(next_btn_x, next_btn_y, duration=1)
        pyautogui.click()

        time.sleep(20)

        pyautogui.moveTo(max_btn_x, max_btn_y, duration=1)
        pyautogui.click()

        time.sleep(1)

        pyautogui.moveTo(deposit_btn_x, deposit_btn_y, duration=1)
        pyautogui.click()

        time.sleep(12)

        pyautogui.moveTo(saveM_button_x, saveM_button_y, duration=1)
        pyautogui.click()

        time.sleep(12)

        pyautogui.moveTo(newAccount_btn_x, newAccount_btn_y, duration=1)
        pyautogui.click()

        time.sleep(5)

        pyautogui.moveTo(selectAccount_btn_x, selectAccount_btn_y, duration=1)
        pyautogui.click()
        time.sleep(5)

        pyautogui.write(str(counter))
        counter += 1
        time.sleep(1)

        pyautogui.moveTo(chooseAcc_btn_x, chooseAcc_btn_y, duration=1)
        pyautogui.click()

        time.sleep(1)

        pyautogui.moveTo(closeModal_btn_x, closeModal_btn_y, duration=1)
        pyautogui.click()

        time.sleep(1)


        # time.sleep(120)

    except KeyboardInterrupt:
        print("Script stopped by user.")

def perform_mouse_actions():
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

def start_stop_script(e):
    global running
    if e.event_type == keyboard.KEY_DOWN:
        if e.name == 's':
            print("Script started.")
            running = True
            perform_mouse_actions()
        elif e.name == 'q':
            print("Script stopped.")
            running = False

if __name__ == "__main__":
    # Register the keybinds
    keyboard.hook(start_stop_script)

    # Keep the main thread running
    keyboard.wait('esc') # You can change 'esc' to another key to exit the script
