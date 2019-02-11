import radiojavan as rj
import bbc as bbc
import manoto as mn
import rjrad as radio
import tvpersia as tvp
from flask import Flask, render_template, request
import subprocess as sub
import manotosd as mnsd
import gem as gem
import time

from logging import FileHandler, WARNING, ERROR

app = Flask(__name__)


# file_handler = FileHandler('/home/pi/Desktop/Home/logs/runTime.log')  # this will log if and only if error happens
# file_handler.setLevel(WARNING)
# app.logger.addHandler(file_handler)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def my_action():
    action = request.form['action']

    if action == 'Radiojavan':
        sub.call(["killall", "chromium-browser"])
        time.sleep(2)
        rj.radiojavan()
        return render_template('index.html')
    elif action == 'ManotoHD':
        sub.call(["killall", "chromium-browser"])
        time.sleep(2)
        mn.manoto()
        return render_template('index.html')
    elif action == 'BBC':
        sub.call(["killall", "chromium-browser"])
        bbc.bbc()
        return render_template('index.html')
    elif action == 'CLOSE':
        sub.call(["killall", "chromium-browser"])
        return render_template('index.html')
    elif action == "RJRADIO":
        sub.call(["killall", "chromium-browser"])
        time.sleep(2)
        radio.rjrad()
        return render_template('index.html')
    elif action == 'TVPERSIA':
        sub.call(["killall", "chromium-browser"])
        time.sleep(2)
        tvp.tvpersia()
        return render_template('index.html')
    elif action == "Manotosd":
        sub.call(["killall", "chromium-browser"])
        time.sleep(2)
        mnsd.manotosd()
        return render_template('index.html')
    elif action == "KODI":
        sub.call(["killall", "chromium-browser"])
        sub.call(["kodi-standalone"])
        return render_template('index.html')
    elif action == "GEM":
        sub.call(["killall", "chromium-browser"])
        time.sleep(2)
        gem.gem()
        return render_template('index.html')
    # utilities section
    if action == "vpnon":
        sub.call(["killall", "chromium-browser"])
        p = sub.Popen(["/home/pi/Desktop/Home/bash_scripts/vpnon.sh"])
        time.sleep(10)
        p = sub.Popen(["chromium-browser", "https://www.google.com/search?q=my+location"])
        return render_template('index.html')
    elif action == "vpnoff":
        sub.call(["killall", "chromium-browser"])
        p = sub.Popen(["/home/pi/Desktop/Home/bash_scripts/vpnoff.sh"])
        time.sleep(10)
        p = sub.Popen(["chromium-browser", "https://www.google.com/search?q=my+location"])
        return render_template('index.html')
    elif action == "reboot":
        sub.call(["./bash_scripts/rpi-rebooter.sh"])
        return render_template('index.html')
    elif action == "wifi":
        sub.call(["./bash_scripts/wifi-rebooter.sh"])
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
