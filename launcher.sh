#!/bin/sh 
#
#cd into project directory, pull from github  and run the pi code
# 
cd /home/pi/Plate\ Recognition 
git pull 
python3 main.py | >> /home/pi/Desktop/log.txt
