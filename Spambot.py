
import time
import pyautogui

def SendHelp():
    time.sleep(5)

    text = open("HELP ME.txt")
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press("enter")

def SendWake():
    text = open("WAKE UP.txt")
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press("enter")

username = input("Do you want to start spam bot?: ")
if username.upper() == "Y" or username.upper() == "YES":
    time.sleep(5)
    for x in range(3):
        SendWake()
        pyautogui.press("enter")


pyautogui.FAILSAFE = True
