#!/bin/bash
echo "Today:" |& tee -a /home/pi/Desktop/Home/logs/start_logs.log
date |& tee -a /home/pi/Desktop/Home/logs/start_logs.log
cd /home/pi/Desktop/Home
echo "Current directory:" |& tee -a /home/pi/Desktop/Home/logs/start_logs.log
pwd |& tee -a /home/pi/Desktop/Home/logs/start_logs.log
echo "Running the server now.....!"
python3 Server.py |& tee -a  /home/pi/Desktop/Home/logs/start_logs.log

