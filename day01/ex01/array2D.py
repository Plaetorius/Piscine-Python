import numpy as np


def slice_me(family: list, start: int, end: int) -> str:
    """
    Shows the shape of the family, slice it, show its new shape and content.

    Parameters:
    family (list): A list of values, often other lists.
    start (int): The start index for slicing.
    end (int): The end index for slicing.

    Returns:
    list: The sliced array converted back into a list (of lists).

    Raises:
    TypeError: If one parameter doesn't match its expected type.
    """
    if (not isinstance(family, list)
            or not isinstance(start, int)
            or not isinstance(end, int)):
        raise TypeError("Invalid parameter type")
    array = np.array(family)
    print(f"My shape is: {array.shape}")
    array = array[start:end]
    print(f"My new shape is: {array.shape}")
    return array.tolist()


def slice_me_test(family: list, start: int, end: int) -> str:
    """
    Shows the shape of the family, slice it, show its new shape and content.

    Parameters:
    family (list): A list of values, often other lists.
    start (int): The start index for slicing.
    end (int): The end index for slicing.

    Returns:
    str: The output of the function

    Raises:
    TypeError: If one parameter doesn't match its expected type.
    """
    if (not isinstance(family, list)
            or not isinstance(start, int)
            or not isinstance(end, int)):
        raise TypeError("Invalid parameter type")
    array = np.array(family)
    output = f"My shape is: {array.shape}\n"
    array = array[start:end]
    output += f"My new shape is: {array.shape}\n{array.tolist()}"
    return output


def main():
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]

    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
