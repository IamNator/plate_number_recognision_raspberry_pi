test_launcher:
	chmod 755 launcher.sh
	sh launcher.sh

set-launcher:
	sudo echo launcher.sh >> here.txt #/etc/rc.local
