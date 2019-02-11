import subprocess
import fullscreen as screen


class bbc:
    def __init__(self):
        self.process()


    def process(self):
        p = subprocess.Popen(["chromium-browser", "http://tvmanoto.com/bbc-persian/"])
        screen.fullscreen()
        return p
