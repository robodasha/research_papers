init:
	pip install -r requirements.txt

test:
	python -m unittest tests.test_crossref_resolver tests.test_mendeley_resolver tests.test_pdf_extractor tests.test_parscit_extractor

.PHONY: init test
