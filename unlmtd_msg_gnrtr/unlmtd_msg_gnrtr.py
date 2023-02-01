import pyautogui as gui
import time

message=input("enter the message\n")
number=int(input("enter the number\n"))

time.sleep(3)
for i in range(number):
    gui.typewrite(message)
    gui.press("enter")