# Keyboard Mouse Control Script

This script allows you to control the mouse using the keyboard. The script uses `pyautogui` for mouse movement, `keyboard` for detecting key presses, and `plyer` for notifications. It enables you to simulate various mouse actions such as moving, clicking, scrolling, and holding mouse buttons with keyboard keys.

## Features

- **Mouse Movement**: Use the `H`, `J`, `K`, `L` keys to move the mouse in different directions.
- **Mouse Clicks**: Press `U` for left-click and `I` for right-click.
- **Double Click**: Press `O` to perform a double-click.
- **Mouse Button Hold**: Press `M` to hold the left mouse button, and `N` to release it.
- **Scroll**: Press the **up** or **down** arrow keys to scroll the page.
- **Shift Key for Faster Movement**: Hold the `Shift` key for faster mouse movement and scrolling.
- **Ctrl Key for Faster Scrolling**: Hold the `Ctrl` key for faster scrolling speed.
- **Toggle Mouse Control Mode**: Use `Ctrl+F1` to enable or disable mouse control mode. When enabled, keyboard actions control the mouse; when disabled, the script will stop responding to the keyboard keys.

## Requirements

- Python 3.x
- `pyautogui`: For controlling the mouse.
- `keyboard`: For detecting key presses.
- `plyer`: For showing notifications.

To install the required libraries, run:

```bash
pip install pyautogui keyboard plyer
