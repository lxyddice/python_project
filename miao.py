from pynput.keyboard import Controller
import pyautogui
import time

while True:
    text = input("请输入文本: ")
    if text.endswith('！') or text.endswith('~') or text.endswith('？'):
        suffix = text[-1]
        text = text[:-1]
    else:
        suffix = ''
    text += "喵" + suffix
    
    keyboard = Controller()
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    keyboard.type(text)
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
