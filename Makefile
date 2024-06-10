no_random:
	pytest -k 'not test_ex00'

all:
	pytest

v:
	pytest -v

v_no_random:
	pytest -v -k 'not test_ex00'

vv:
	pytest -vv

vv_no_random:
	pytest -vv -k 'not test_ex00'


.PHONY: all 