import pyautogui
import keyboard
import time
import ctypes


STEP_NORMAL = 8
STEP_FAST = 110
SCROLL_NORMAL = 100
SCROLL_FAST = 1000
DELAY = 0.02

pyautogui.FAILSAFE = False  # Disabling the emergency exit

mouse_control_enabled = False
fast_scroll_enabled = False
blocked_keys = ['h', 'j', 'k', 'l', 'u', 'i', 'm', ',', 'up', 'down', 'left', 'right']

def horizontal_scroll(amount):
    # amount > 0 — right, amount < 0 — left
    ctypes.windll.user32.mouse_event(0x0800, 0, 0, amount, 0)  # 0x0800 = MOUSEEVENTF_HWHEEL


def block_keys():
    for key in blocked_keys:
        keyboard.block_key(key)

def unblock_keys():
    for key in blocked_keys:
        keyboard.unblock_key(key)

def move_mouse():
    global mouse_control_enabled, fast_scroll_enabled
    print("The script is running. Alt+O - turn on/off the mode. Alt+F2 - exit.")
    while True:
        if mouse_control_enabled:
            step = STEP_FAST if keyboard.is_pressed('shift') else STEP_NORMAL
            scroll = SCROLL_FAST if fast_scroll_enabled else SCROLL_NORMAL

            # Mouse movement is disabled while Alt is held (Alt is used for scrolling)
            if not keyboard.is_pressed('alt'):
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
                elif keyboard.is_pressed('m'):
                    pyautogui.mouseDown(button='left')
                    time.sleep(0.2)
                elif keyboard.is_pressed(','):
                    pyautogui.mouseUp(button='left')
                    time.sleep(0.2)

            # Scroll with Alt + h/j/k/l
            if keyboard.is_pressed('alt+k'):
                pyautogui.scroll(scroll)
                time.sleep(0.1)
            elif keyboard.is_pressed('alt+j'):
                pyautogui.scroll(-scroll)
                time.sleep(0.1)
            elif keyboard.is_pressed('alt+h'):
                horizontal_scroll(scroll)
                time.sleep(0.1)
            elif keyboard.is_pressed('alt+l'):
                horizontal_scroll(-scroll)
                time.sleep(0.1)

            time.sleep(DELAY)
        else:
            time.sleep(0.05)

        if keyboard.is_pressed('alt+f2'):
            print("KM closed")
            break

def toggle_mode():
    def switch():
        global mouse_control_enabled
        mouse_control_enabled = not mouse_control_enabled
        if mouse_control_enabled:
            block_keys()
        else:
            unblock_keys()
            global fast_scroll_enabled
            if fast_scroll_enabled:
                fast_scroll_enabled = False
                print("[INFO] Scroll mode: NORMAL")

        print(f"[INFO] Mouse control mode: {'ON' if mouse_control_enabled else 'OFF'}")

    keyboard.add_hotkey('alt+o', switch, suppress=True)

def toggle_fast_scroll():
    def switch():
        global fast_scroll_enabled
        if not mouse_control_enabled:
            return
        fast_scroll_enabled = not fast_scroll_enabled
        mode = 'FAST' if fast_scroll_enabled else 'NORMAL'
        print(f"[INFO] Scroll mode: {mode}")

    keyboard.add_hotkey('ctrl', switch, suppress=False)
    
if __name__ == "__main__":
    toggle_mode()
    toggle_fast_scroll()
    move_mouse()