import subprocess
import fullscreen as screen

class gem:
    def __init__(self):
        self.process()

    def process(self):
        p = subprocess.Popen(["chromium-browser", "http://tvmanoto.com/gem-tv/"])
        screen.fullscreen()
        return p

