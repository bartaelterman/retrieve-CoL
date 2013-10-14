e2e_tests:
	nosetests -v --nocapture ./test/*_feature.py

unit_tests:
	nosetests -v --nocapture ./test/*_unit.py

test: unit_tests e2e_tests
