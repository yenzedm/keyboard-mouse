import pyautogui
import keyboard
import time
from win10toast import ToastNotifier


toast = ToastNotifier()

STEP_NORMAL = 5
STEP_FAST = 110
SCROLL_NORMAL = 400
SCROLL_FAST = 950
DELAY = 0.02

pyautogui.FAILSAFE = False  # Disabling the emergency exit

mouse_control_enabled = False
blocked_keys = ['h', 'j', 'k', 'l', 'u', 'i', 'o', 'm', 'n', 'up', 'down']

def block_keys():
    for key in blocked_keys:
        keyboard.block_key(key)

def unblock_keys():
    for key in blocked_keys:
        keyboard.unblock_key(key)

def move_mouse():
    global mouse_control_enabled
    print("The script is running. Ctrl+F1 - turn on/off the mode. Ctrl+F2 - exit.")
    while True:
        if mouse_control_enabled:
            step = STEP_FAST if keyboard.is_pressed('shift') else STEP_NORMAL
            scroll = SCROLL_FAST if keyboard.is_pressed('ctrl') else SCROLL_NORMAL

            if keyboard.is_pressed('h'):
                pyautogui.move(-step, 0)
            elif keyboard.is_pressed('l'):
                pyautogui.move(step, 0)
            elif keyboard.is_pressed('k'):
                pyautogui.move(0, -step)
            elif keyboard.is_pressed('j'):
                pyautogui.move(0, step)
            elif keyboard.is_pressed('u'):
                pyautogui.click(button='left')
                time.sleep(0.2)
            elif keyboard.is_pressed('i'):
                pyautogui.click(button='right')
                time.sleep(0.2)
            elif keyboard.is_pressed('o'):
                pyautogui.doubleClick()
                time.sleep(0.3)
            elif keyboard.is_pressed('m'):
                pyautogui.mouseDown(button='left')
                time.sleep(0.2)
            elif keyboard.is_pressed('n'):
                pyautogui.mouseUp(button='left')
                time.sleep(0.2)
            
            if keyboard.is_pressed('up'):
                pyautogui.scroll(scroll)
                time.sleep(0.1)
            elif keyboard.is_pressed('down'):
                pyautogui.scroll(-scroll)
                time.sleep(0.1)

            time.sleep(DELAY)
        else:
            time.sleep(0.05)

        if keyboard.is_pressed('ctrl+f2'):
            print("KM closed")
            break

def toggle_mode():
    def switch():
        global mouse_control_enabled
        mouse_control_enabled = not mouse_control_enabled
        if mouse_control_enabled:
            block_keys()
            toast.show_toast(title='Keyboard mouse', msg='ON', duration=2)
        else:
            unblock_keys()
            toast.show_toast(title='Keyboard mouse', msg='ON', duration=2)

        print(f"[INFO] Mouse control mode: {'ON' if mouse_control_enabled else 'OFF'}")
    
    keyboard.add_hotkey('ctrl+f1', switch)

if __name__ == "__main__":
    toggle_mode()
    move_mouse()
