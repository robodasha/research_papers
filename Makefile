init:
	pip install -r requirements.txt

test:
	python -m unittest tests.test_crossref_resolver

.PHONY: init test
