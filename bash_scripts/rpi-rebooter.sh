#!/bin/bash

echo "recieved reboot request on" && date|& tee -a /home/pi/Desktop/Home/logs/reboot_logs.log

reboot