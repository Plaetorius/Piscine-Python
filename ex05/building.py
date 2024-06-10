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
        elif c.islower():
            data['LOWER'] += 1
        elif c in "!\"#$%&')*+,-./:;<=>?@[\\]^_`{|}~":
            data['PUNCT'] += 1
        elif c in "\t\n\v\f\r ":
            data['SPACES'] += 1
        elif c in "0123456789":
            data['DIGITS'] += 1
    return data


def print_data(data: dict) -> None:
    """
    Prints the characters data contained in the dictionary.
    
    Parameters:
    data (dict): A dictionary containing information on the characters of a string.
    
    Returns:
    str: The result of applying param_fun to n.
    """
    total_characters = sum(data.values())
    print(f"The text contains {total_characters} characters:\n"
          f"{data['UPPER']} upper letters\n"
          f"{data['LOWER']} lower letters\n"
          f"{data['PUNCT']} punctuation marks\n"
          f"{data['SPACES']} spaces\n"
          f"{data['DIGITS']} digits")


def main():
    if (len(sys.argv) > 2):
        raise AssertionError("usage: python3 building.py <string>")
    if (len(sys.argv) < 2):
        print("What is the text to count?")
        string = sys.stdin.readline()
    else:
        string = sys.argv[1]
    print_data(parser(string))


if __name__ == "__main__":
    main()
