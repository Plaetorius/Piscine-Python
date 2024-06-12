import sys

if len(sys.argv) > 1:
	if len(sys.argv) != 2:
		raise AssertionError("more than one argument is provided")
	number = sys.argv[1]
	has_sign = False # Check for syntax like "+5" or "-0"
	for l in number:
		if (not l in "+-0123456789") or (l in '+-' and has_sign):
			raise AssertionError("argument is not an integer")
		if l in '+-':
			has_sign = True
	print(f"I'm {'Odd' if int(number) % 2 else 'Even'}.")