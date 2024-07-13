import sys

if len(sys.argv) > 1:
    if len(sys.argv) != 2:
        raise AssertionError("more than one argument is provided")
    number = sys.argv[1]
    has_sign = False  # Check for syntax like "+5" or "-0"
    for char in number:
        if (char not in "+-0123456789") or (char in '+-' and has_sign):
            raise AssertionError("argument is not an integer")
        if char in '+-':
            has_sign = True
    print(f"I'm {'Odd' if int(number) % 2 else 'Even'}.")
