import subprocess
import fullscreen as screen


class tvpersia:
    def __init__(self):
        self.process()

    def process(self):
        p = subprocess.Popen(["chromium-browser", "http://tvmanoto.com/tv-persia/"])
        screen.fullscreen()
        return p
