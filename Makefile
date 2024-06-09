no_random:
	pytest -k 'not test_ex00'

all:
	pytest

verbose:
	pytest -v

.PHONY: all 