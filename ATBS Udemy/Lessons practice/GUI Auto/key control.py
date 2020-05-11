import pyautogui
pyautogui.position()
pyautogui.click(565, 1064)
pyautogui.click(500,800); pyautogui.typewrite('Hello World!')

pyautogui.click(500, 800); pyautogui.typewrite('Hello World!', interval=0.2)

pyautogui.click(500, 800); pyautogui.typewrite(['a', 's', 'left', 'x', 'Y'], interval=1)

pyautogui.KEYBOARD_KEYS

#to run key combination
pyautogui.hotkey('ctrl', 's')