test_launcher:
	chmod 755 launcher.sh
	sh launcher.sh


set-launcher:
	sudo u+x launcher.sh  /usr/local/sbin/launcher.sh
	chmod 755 /usr/local/sbin/launcher.sh
	sudo cp launcher.service /etc/systemd/system/launcher.service
	sudo systemctl start mawaqif
	systemctl status mawaqif
	sudo systemctl enable mawaqif


# sudo cp launcher.sh  /etc/init.d/.
# update-rc.d /etc/init.d/launcher.sh defaults
# sudo cp launcher.sh  /etc/network/if-up.d/launcher


check_camera:
	vcgencmd get_camera
