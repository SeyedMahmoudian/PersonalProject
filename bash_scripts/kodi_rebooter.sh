#!/usr/bin/env bash

echo "recieved kodi request on" && date|& tee -a /home/pi/Desktop/Home/logs/kodi_logs.log

killall kodi_v7.bin

sleep 10

kodi &