#!/bin/sh 
#
#
cd /home/pi/Plate\ Recognition 
git pull 
python3 /home/pi/Plate\ Recognition/main.py | >> /home/pi/Desktop/log.txt &
