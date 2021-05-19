#!bin/sh
# launcher.sh
# navigate to project directory, pull from github and run project code
cd /home/pi/Plate\ Recognition
git pull origin main
sudo python3 main.py & > /home/pi/Desktop/log.txt 2>&1
exit 0
