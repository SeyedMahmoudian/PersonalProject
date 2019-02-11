import subprocess
import pyautogui as gui
import time


class rjrad:
    def __init__(self):
        self.process()

    def process(self):
        p = subprocess.Popen(["chromium-browser", "https://www.radiojavan.com/radio/player"])
        time.sleep(7)
        gui.press('f11')
        return p
