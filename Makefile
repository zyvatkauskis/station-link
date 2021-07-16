SHELL=/bin/bash

install:
	python3.8 -m venv venv; \
	. venv/bin/activate; \
	python3.8 -m pip install -r requirements.txt; \

run:
	. venv/bin/activate; export PYTHONPATH=.; \
	python3.8 link_station/app.py
