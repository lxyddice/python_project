from pynput.keyboard import Controller
import pyautogui
import time

while True:
    text = input("请输入文本: ")
    text += "喵"
    keyboard = Controller()
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    keyboard.type(text)
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
