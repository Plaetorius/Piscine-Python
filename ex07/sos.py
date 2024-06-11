import sys

def main():
    '''Turns the string passed as a parameter in morse code

    Parameters:
    sys.argv[1] (str): an alphanumeric (+ spaces) string

    Returns:
    None
    '''
    if (len(sys.argv) != 2 or not sys.argv[1].replace(' ', '').isalnum()):
        raise AssertionError("the arguments are bad")
    morse_dict = {
            " ": "/ ",
            "A": ".- ",
            "B": "-... ",
            "C": "-.-. ",
            "D": "-.. ",
            "E": ". ",
            "F": "..-. ",
            "G": "--. ",
            "H": ".... ",
            "I": ".. ",
            "J": ".--- ",
            "K": "-.- ",
            "L": ".-.. ",
            "M": "-- ",
            "N": "-. ",
            "O": "--- ",
            "P": ".--. ",
            "Q": "--.- ",
            "R": ".-. ",
            "S": "... ",
            "T": "- ",
            "U": "..- ",
            "V": "...- ",
            "W": ".-- ",
            "X": "-..- ",
            "Y": "-.-- ",
            "Z": "--.. ",
            "0": "----- ",
            "1": ".---- ",
            "2": "..--- ",
            "3": "...-- ",
            "4": "....- ",
            "5": "..... ",
            "6": "-.... ",
            "7": "--... ",
            "8": "---.. ",
            "9": "----. ",
        }
    print("".join(morse_dict[c.upper()] for c in sys.argv[1]))

if __name__ == "__main__":
    main()