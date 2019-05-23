.PHONY: clean train train-local interactive actions x

export PYTHONPATH=$(shell pwd)

help:
	@echo "    clean"
	@echo "        Remove python artifacts and build artifacts."
	@echo "    train"
	@echo "        Train nlu and core model in docker container"
	@echo "    train-local"
	@echo "        Train nlu and core model for local development"
	@echo "    run-local"
	@echo "        Run a local server"
	@echo "    interactive"
	@echo "        Start interactive training session"
	@echo "    actions"
	@echo "        Start the server for custom action."
	@echo "    x"
	@echo "        Start rasa x web interface"

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
