.PHONY: clean-pyc install run

clean-pyc:
	find . -name "*.pyc" -type f
	find . -name "*.pyc" -type f -delete

install:
	sudo apt-get install libpcap0.8-dev
	sudo pip install -r requirements.txt
	
run:
	chmod +x sniffer && ./sniffer
