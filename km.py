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


blocked_keys = [
    # Буквы
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    # Цифры (верхний ряд)
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    # Знаки препинания и символы
    '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', '{', ']', '}', '\\', '|', ';', ':',
    "'", '"', ',', '<', '.', '>', '/', '?', ' ',
]

mouse_control_enabled = False
fast_scroll_enabled = False


def horizontal_scroll(amount):
    # amount > 0 — right, amount < 0 — left
    ctypes.windll.user32.mouse_event(0x01000, 0, 0, amount, 0)  # 0x0800 = MOUSEEVENTF_HWHEEL


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
            elif keyboard.is_pressed('alt+l'):
                horizontal_scroll(scroll)
                time.sleep(0.1)
            elif keyboard.is_pressed('alt+h'):
                horizontal_scroll(-scroll)
                time.sleep(0.1)

            time.sleep(DELAY)
        else:
            time.sleep(0.05)

        if keyboard.is_pressed('alt+f2'):
            print("KM closed")
            break


def switch_mode():
    global mouse_control_enabled, fast_scroll_enabled
    mouse_control_enabled = not mouse_control_enabled
    if mouse_control_enabled:
        block_keys()
    else:
        unblock_keys()
        if fast_scroll_enabled:
            fast_scroll_enabled = False
            print("[INFO] Scroll mode: NORMAL")
    print(f"[INFO] Mouse control mode: {'ON' if mouse_control_enabled else 'OFF'}")


def _o_hook_fn(event):
    if (event.name or '').lower() != 'o':
        return True

    alt_pressed = keyboard.is_pressed('alt')

    if alt_pressed:
        # Alt+O — switch mode and suppress the key so that 'o' is not typed
        if event.event_type == keyboard.KEY_DOWN:
            switch_mode()
        return False

    # Single 'o': suppress when ON, allow when OFF
    return not mouse_control_enabled


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
    keyboard.hook(_o_hook_fn, suppress=True)
    toggle_fast_scroll()
    move_mouse()