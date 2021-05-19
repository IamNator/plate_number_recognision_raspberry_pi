test_launcher:
	chmod 755 launcher.sh
	sh launcher.sh

set-launcher:
	sudo echo launcher.sh >> /etc/rc.local
