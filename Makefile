init:
	pip install -r requirements.txt

test:
	python -m unittest tests.simple_tests

.PHONY: init test
