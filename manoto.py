import subprocess
import pyautogui as gui
import time


class manoto:
    def __init__(self):
        self.process()

    def process(self):
        p = subprocess.Popen(["chromium-browser", "https://www.manototv.com/live"])
        time.sleep(7)
        gui.press('f11')
        time.sleep(7)
        gui.moveTo(1443,503)
        time.sleep(10)
        gui.click(1447,500)
        gui.click(1447, 500)
        gui.click(1447, 500)
        time.sleep(2)
        gui.moveTo(1823,304)
        return p

