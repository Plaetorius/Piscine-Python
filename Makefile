no_random:
	pytest -k 'not test_ex00'

all:
	pytest

v:
	pytest -v

v_no_random:
	pytest -v -k 'not test_ex00'

.PHONY: all 