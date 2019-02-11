#!/bin/bash
cd /home/pi/Desktop/Home
pwd |& tee -a /home/pi/Desktop/Home/logs/bot_logs.log
echo "Running the bot now.....!"
python telegrambot.py |& tee -a  /home/pi/Desktop/Home/logs/bot_logs.log

