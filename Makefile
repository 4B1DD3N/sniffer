.PHONY: clean-pyc install run

clean-pyc:
	find . -name "*.pyc" -type f
	find . -name "*.pyc" -type f -delete

install:
	sudo apt-get install libpcap0.8-dev
	sudo pip install pcapy
	sudo pip install termcolor 
	
run:
	chmod +x sniffer && ./sniffer
