import sys


def parser(string: str) -> dict:
    data = {
        'UPPER': 0,
        'LOWER': 0,
        'PUNCT': 0,
        'SPACES': 0,
        'DIGITS': 0,
    }
    for c in string:
        if c.isupper():
            data['UPPER'] += 1
        if c.islower():
            data['LOWER'] += 1
        if c in "!\"#$%&')*+,-./:;<=>?@[\\]^_`{|}~":
            data['PUNCT'] += 1
        if c in "\t\n\v\f\r ":
            data['SPACES'] += 1
        if c in "0123456789":
            data['DIGITS'] += 1
    return data


def print_data(data: dict) -> None:
    print(f"The text contains {sum(data.values())} characters:\n\
{data['UPPER']} upper letters\n\
{data['LOWER']} lower letters\n\
{data['PUNCT']} punctuation marks\n\
{data['SPACES']} spaces\n\
{data['DIGITS']} digits")


def main():
    if (len(sys.argv) > 2):
        raise AssertionError("usage: python3 building.py <string>")
    if (len(sys.argv) < 2):
        string = input("What is the text to count?\n")
    else:
        string = sys.argv[1]
    print_data(parser(string))


if __name__ == "__main__":
    main()
