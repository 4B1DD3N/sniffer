.PHONY: help clean-pyc install run
.DEFAULT_GOAL=help

help: ## Show help comments for the targets
	@grep -E '(^[a-zA-Z_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-10s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'

clean-pyc: ## Delete the compiled Python bytecode files
	find . -name "*.pyc" -type f
	find . -name "*.pyc" -type f -delete

install: ## Install the required Python packages
	sudo apt-get install libpcap0.8-dev
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
