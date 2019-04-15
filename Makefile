.PHONY: clean train-nlu train-core train-nlu-local train-core-local train-interactive action-server

TEST_PATH=./

help:
	@echo "    clean"
	@echo "        Remove python artifacts and build artifacts."
	@echo "    train-nlu"
	@echo "        Trains a new nlu model using the projects Rasa NLU config"
	@echo "    train-core"
	@echo "        Trains a new dialogue model using the story training data"
	@echo "    train-nlu-local"
	@echo "        Trains a new nlu model locally"
	@echo "    train-core-local"
	@echo "        Trains a new dialogue model locally"
	@echo "    train-interactive"
	@echo "        Starts interactive training session"
	@echo "    action-server"
	@echo "        Starts the server for custom action."

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
	rm -rf __pycache__

train-nlu:
	docker run \
		-v $(shell pwd):/app/project \
		-v $(shell pwd)/../models/rasa_nlu:/app/models \
		-v $(shell pwd)/config:/app/config \
		-v $(shell pwd)/components:/app/components \
		-v $(shell pwd)/modules:/app/modules \
		aroemelt/ethicbot:nlu \
		run \
		python -m rasa_nlu.train \
		-c config/nlu_config.yml \
		-d project/data/nlu.md \
		-o models \
		--project current

train-core:
	docker run \
		-v $(shell pwd):/app/project \
		-v $(shell pwd)/../models/rasa_core:/app/models \
		-v $(shell pwd)/config:/app/config \
		aroemelt/ethicbot:core \
		run \
		python -m rasa_core.train \
		-d project/domain.yml \
		-s project/data/stories.md \
		-o models \
		-c config/policies.yml

train-nlu-local:
	python -m rasa_nlu.train -c config/nlu_config.yml --data data/nlu.md -o ../models --fixed_model_name nlu --project current

train-core-local:
	python -m rasa_core.train -d domain.yml -s data/stories.md -o ../models/current/dialogue -c policies.yml

train-interactive:
	python -m rasa_core.train interactive -o ../models/current/dialogue -d domain.yml -c config/policies.yml -s data/stories.md \
  		--nlu ../models/current/nlu --endpoints config/endpoints_local.yml
	
action-server:
	python -m rasa_core_sdk.endpoint --actions actions.actions

