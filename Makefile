.PHONY: help clean-pyc install run tests all
.DEFAULT_GOAL=help
SHELL=/bin/bash

help: ## Show help comments for the targets
	@grep -E '(^[a-zA-Z_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-10s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'

clean-pyc: ## Delete the compiled Python bytecode files
	find . -name "*.pyc" -type f
	find . -name "*.pyc" -type f -delete

install: ## Install the application
	sudo apt-get update
	sudo apt-get install python2.7 python-pip libpcap0.8-dev
	sudo pip install -r requirements.txt
	
run: ## Run the application
	@if [[ -f sniffer && -x sniffer ]]; then\
	    echo "Execution permission check succeeded.";\
	else\
	    echo "Changing execute permission...";\
	    chmod +x sniffer;\
	fi
	echo "Sniffer needs root permission to capture packets."
	sudo ./sniffer

tests: ## Run the unit tests
	python -m unittest discover -s tests -p "*Test.py" -b

all: install run ## Install and run the application
