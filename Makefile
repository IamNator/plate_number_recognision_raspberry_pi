test_launcher:
	chmod 755 launcher.sh
	sh launcher.sh


set-launcher:
	sudo cp launcher.sh  /usr/local/sbin/launcher.sh
	sudo chmod 755 /usr/local/sbin/launcher.sh
	sudo cp launcher.service /etc/systemd/system/launcher.service
# sudo systemctl start mawaqif
	sudo systemctl enable launcher
	systemctl status launcher
	


# sudo cp launcher.sh  /etc/init.d/.
# update-rc.d /etc/init.d/launcher.sh defaults
# sudo cp launcher.sh  /etc/network/if-up.d/launcher


check_camera:
	vcgencmd get_camera
