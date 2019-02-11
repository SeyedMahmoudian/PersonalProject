import pyautogui as gui
import time


class fullscreen:
    def __init__(self):
        self.process()

    def process(self):
        time.sleep(4)
        gui.press('f11')
        time.sleep(7)
        gui.press('space')
        time.sleep(8.5)
        gui.click(961,275)
##        gui.click(963,332)
        #gui.click(963, 361)
        time.sleep(2)
        gui.moveTo(1823,304)
