#!/bin/bash
echo "WIFI REBOOTER ENGAGED ON : " && date|& tee -a /home/pi/Desktop/Home/logs/wifi_logs.log
sudo ifconfig wlan0 down|& tee -a /home/pi/Desktop/Home/logs/wifi_logs.log
sleep 10
sudo ifconfig wlan0 up|& tee -a /home/pi/Desktop/Home/logs/wifi_logs.log