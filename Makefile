.PHONY: clean train train-local interactive actions x

export PYTHONPATH=$(shell pwd)

help:
	@echo "    clean"
	@echo "        Remove python artifacts and build artifacts."
	@echo "    train"
	@echo "        Trains nlu and core model in docker container"
	@echo "    train-local"
	@echo "        Trains nlu and core model for local development"
	@echo "    interactive"
	@echo "        Starts interactive training session"
	@echo "    actions"
	@echo "        Starts the server for custom action."
	@echo "    x"
	@echo "        Starts rasa x web interface"

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
	rm -rf __pycache__

train:
	docker run \
		-v $(shell pwd):/app \
  		aroemelt/ethicbot:rasa \
  		train --fixed-model-name current

train-local:
	rasa train --fixed-model-name current

interactive:
	rasa interactive --endpoints endpoints_local.yml
	
actions:
	rasa run actions --actions actions

x:
	rasa x
