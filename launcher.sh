#!/bin/sh 
#
#
# 
### BEGIN INIT INFO
# Provides:          mawaqif
# Required-Start:    $all
# Required-Stop:     
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: navigate to project directory, pull from github and run project code
### END INIT INFO

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/bin

. /lib/init/vars.sh
. /lib/lsb/init-functions
# If you need to source some other scripts, do it here

case "$1" in
  start)
    log_begin_msg "Starting mawaqif"
# do something
    cd /home/pi/Plate\ Recognition 
    git pull 
    python3 main.py | >> /home/pi/Desktop/log.txt
    log_end_msg $?
    exit 0
    ;;
  stop)
    log_begin_msg "Stopping mawaqif"

    # do something to kill the service or cleanup or nothing
    pgrep -f main > stop_file
    sed -i 's/^/kill /' stop_file
    chmod 777 stop_file
    ./stop_file

    log_end_msg $?
    exit 0
    ;;
  *)
    echo "Usage: /etc/init.d/laucher {start|stop}"
    exit 1
    ;;
esac