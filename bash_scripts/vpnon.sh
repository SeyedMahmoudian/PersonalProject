#!/bin/bash
echo "Runing:" |& tee -a /home/pi/Desktop/Home/logs/vpn_logs.log
cd /home/pi/vpn
sudo openvpn --config *.ovpn |& tee -a /home/pi/Desktop/Home/logs/vpn_logs.log