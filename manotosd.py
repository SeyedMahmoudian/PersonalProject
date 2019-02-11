import subprocess
import fullscreen as screen


class manotosd:
    def __init__(self):
        self.process()

    def process(self):
        p = subprocess.Popen(["chromium-browser", "http://tvmanoto.com/manototv/"])
        screen.fullscreen()
        return p

