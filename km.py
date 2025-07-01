import pyautogui
import keyboard
import time
from win10toast import ToastNotifier
import ctypes
import sys
from pathlib import Path


def resource_path(relative_path):
    """ Получает правильный путь к ресурсу после сборки PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        # Если программа запущена из .exe
        base_path = Path(sys._MEIPASS)
    else:
        # Если запущена как скрипт Python
        base_path = Path(__file__).parent
    return str(base_path / relative_path)

# Пример использования:
icon_path = resource_path("km.ico")
print(icon_path)

toast = ToastNotifier()

STEP_NORMAL = 8
STEP_FAST = 110
SCROLL_NORMAL = 400
SCROLL_FAST = 950
DELAY = 0.02

pyautogui.FAILSAFE = False  # Disabling the emergency exit

mouse_control_enabled = False
blocked_keys = ['h', 'j', 'k', 'l', 'u', 'i', 'm', 'n', 'up', 'down', 'left', 'right']

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
            elif keyboard.is_pressed('right'):
                horizontal_scroll(-scroll)
                time.sleep(0.1)
            elif keyboard.is_pressed('left'):
                horizontal_scroll(scroll)
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
            toast.show_toast(title='Keyboard mouse', msg='ON', icon_path=icon_path, duration=2)
        else:
            unblock_keys()
            toast.show_toast(title='Keyboard mouse', msg='OFF', icon_path=icon_path, duration=2)

        print(f"[INFO] Mouse control mode: {'ON' if mouse_control_enabled else 'OFF'}")
    
    keyboard.add_hotkey('ctrl+f1', switch)

if __name__ == "__main__":
    toggle_mode()
    move_mouse()
