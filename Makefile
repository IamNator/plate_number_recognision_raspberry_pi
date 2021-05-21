test_launcher:
	chmod 755 launcher.sh
	sh launcher.sh

set-launcher:
	chmod 755 launcher.sh
	# sudo cp launcher.sh  /etc/init.d/.
	# update-rc.d /etc/init.d/launcher.sh defaults
	sudo cp launcher.sh  /etc/network/if-up.d/launcher

check_camera:
	vcgencmd get_camera
