
import time
import pyautogui

def SendHelp():
    #Time before bot starts typing
    time.sleep(5)
    #Which text do you want to copy and type from
    text = open("HELP ME.txt")
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press("enter")

def SendWake():
    #Which text do you want to copy and type from
    text = open("WAKE UP.txt")
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press("enter")

#Confirm you want to start bot
username = input("Do you want to start spam bot?: ")
if username.upper() == "Y" or username.upper() == "YES":
    time.sleep(5)
    for x in range(3):
        SendWake()
        pyautogui.press("enter")

#If you want to stop bot
pyautogui.FAILSAFE = True
