test_launcher:
	chmod 755 launcher.sh
	sh launcher.sh

set-launcher:
	chmod 755 launcher.sh
	cat launcher.sh >> /etc/rc.local
