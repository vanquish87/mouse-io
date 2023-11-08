import time

import pyautogui

pyautogui.FAILSAFE = False

while True:
    time.sleep(20)

    for i in range(30, 100):
        pyautogui.moveTo(500, i * 3)

    for i in range(0, 3):
        pyautogui.press("shift")
