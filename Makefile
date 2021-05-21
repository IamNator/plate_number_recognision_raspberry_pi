test_launcher:
	chmod 755 launcher.sh
	sh launcher.sh

set-launcher:
	chmod 755 launcher.sh
	sudo cp launcher.sh  /etc/init.d/.
	update-rc.d /etc/init.d/launcher.sh defaults

check_camera:
	vcgencmd get_camera
