test_launcher:
	chmod 755 launcher.sh
	sh launcher.sh

set-launcher:
	chmod 755 launcher.sh
	mv launcher.sh  /etc/init.d/.

check_camera:
	vcgencmd get_camera
