import webbrowser
import pyautogui as gui
import time


class radiojavan:
    def __init__(self):
        self.process()

    def process(self):
        webbrowser.open('https://www.radiojavan.com/tv', new=1)
        time.sleep(7)
        gui.press('f11')
        time.sleep(7)
        gui.click(1525, 936) #make stream full screen
