init:
	pip install -r requirements.txt

test:
	python tests/simple_tests.py

.PHONY: init test
