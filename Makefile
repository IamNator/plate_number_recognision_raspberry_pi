test_launcher:
	chmod 755 launcher.sh
	sh launcher.sh

set-launcher:
	chmod 755 launcher.sh
	sed 's/exit 0$/\ /' /etc/rc.local 
	cat launcher.s h >> /etc/rc.local

check_camera:
	vcgencmd get_camera
