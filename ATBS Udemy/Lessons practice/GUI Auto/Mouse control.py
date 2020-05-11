import pyautogui

pyautogui.size()
w, h = pyautogui.size()

#checks the position of mouse on the screen
pyautogui.position()

#control mouse movement
pyautogui.moveTo(10,10)
pyautogui.moveTo(10,10, duration=2)
pyautogui.moveTo(10,30, duration=3)

#moving to the right
pyautogui.moveRel(20, 10)
pyautogui.moveRel(200, 0)
pyautogui.moveRel(200, 0, duration=2)

#lets try clicking on help
pyautogui.position()
pyautogui.click(1437, 22)
#also have features like rightClick(), doubleClick() etc.