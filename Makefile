.PHONY: clean train train-local interactive actions test test-nlu x

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
	@echo "    test"
	@echo "        Start a test session on the shell"
	@echo "    test-nlu"
	@echo "        Start an nlu test session"
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

test:
	rasa shell --endpoints endpoints_local.yml

test-nlu:
	rasa shell nlu

x:
	rasa x
