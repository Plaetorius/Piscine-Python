import sys
from ft_filter import ft_filter


def main():
    '''Prints a list of words in S (str) that have a greater
    length than N (int)

    Parameters:
    sys.argv[1] (str): the string to be parsed to get the words
    sys.argv[2] (str): the minimal length for the words

    Returns:
    None
    '''
    if (len(sys.argv) != 3):
        raise AssertionError("the arguments are bad")
    try:
        N = int(sys.argv[2])
        S = sys.argv[1]
        for c in "\t\n\v\f\r":
            S = " ".join(S.split(c))
        print(ft_filter(
            lambda word: len(word) > N,
            S.split()
        ))
    except ValueError:
        raise AssertionError("the arguments are bad")


if __name__ == "__main__":
    main()
