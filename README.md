# Keyboard Mouse Control Script

This script allows you to control the mouse using the keyboard. The script uses `pyautogui` for mouse movement, `keyboard` for detecting key presses, and `plyer` for notifications. It enables you to simulate various mouse actions such as moving, clicking, scrolling, and holding mouse buttons with keyboard keys.

## Features

- **Mouse Movement**: Use the `h`, `j`, `k`, `l` moving the mouse like vim
- **Mouse Clicks**: Press `u` for left-click and `i` for right-click.
- **Double Click**: Press `o` to perform a double-click.
- **Mouse Button Hold**: Press `m` to hold the left mouse button, and `n` to release it.
- **Scroll**: Press the **↑** or **↓** arrow keys to scroll the page.
- **Shift Key for Faster Movement**: Hold the `Shift` key for faster mouse movement and scrolling.
- **Ctrl Key for Faster Scrolling**: Hold the `Ctrl` key for faster scrolling speed.
- **Toggle Mouse Control Mode**: Use `Ctrl+F1` to enable or disable mouse control mode. When enabled, keyboard actions control the mouse; when disabled, the script will stop responding to the keyboard keys.

## Requirements

- Python 3.x
- `pyautogui`: For controlling the mouse.
- `keyboard`: For detecting key presses.
- `win10toast`: For showing notifications.

To install the required libraries, run:

```bash
pip install pyautogui keyboard win10toast
```

## Error

WNDPROC return value cannot be converted to LRESULT  
TypeError: WPARAM is simple, so must be an int object (got NoneType)

This is because of the following function in win10toast/\_\_init\_\_.py. Solution:

```python
    def on_destroy(self, hwnd, msg, wparam, lparam):
        """Clean after notification ended.

        :hwnd:
        :msg:
        :wparam:
        :lparam:
        """
        nid = (self.hwnd, 0)
        Shell_NotifyIcon(NIM_DELETE, nid)
        PostQuitMessage(0)

        return None ##<< Error causing line. Replace return None with return 0
```