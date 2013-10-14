e2e_tests:
	nosetests -v --nocapture ./test/*_feature.py

unit_tests:
	nosetests -v --nocapture ./test/*_unit.py

test: unit_tests e2e_tests

example:
	rm -rf example
	mkdir example
	echo "Enchytraeus albidus\nHenlea perpusilla\nLumbricillus lineatus" > example/test_input.txt
	./bin/fetch_taxonomy_from_file.py example/test_input.txt
