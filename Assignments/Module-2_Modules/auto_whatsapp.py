import pywhatkit
import pyautogui
import time

number = "+919724799469"

# Open chat once
pywhatkit.sendwhatmsg_instantly(number, "Start")
time.sleep(5)

messages = ["Msg 1", "Msg 2", "Msg 3"]

for msg in messages:
    pyautogui.write(msg)
    pyautogui.press("enter")
    time.sleep(5)