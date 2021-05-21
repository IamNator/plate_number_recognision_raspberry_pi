#!/bin/sh 
#
#
cd /home/pi/Plate\ Recognition 
git pull 
python3 main.py | >> /home/pi/Desktop/log.txt &
