import pyautogui
import time
time.sleep(1)
count=0
while count<=100:
    pyautogui.typewrite("Hii, I am a bot. This is a test message.") # Message you want to send on WhatsAp
    pyautogui.press("enter")
    count=count+1
