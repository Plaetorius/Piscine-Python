import numpy as np
from typing import List, Union


# Using Python built-in lists
def give_bmi(
    height: List[Union[int, float]],
    weight: List[Union[int, float]]
) -> List[float]:
    """
    Calculate the Body Mass Index (BMI) for each pair of height and weight.

    Parameters:
    height (List[Union[int, float]]): A list of heights in meters.
    weight (List[Union[int, float]]): A list of weights in kilograms.

    Returns:
    List[float]: A list of BMI values corresponding to each height and weight
    pair.

    Raises:
    ValueError: If the height and weight lists do not have the same size.
    TypeError: If any element in height or weight is not an int or float.
    """
    if len(height) != len(weight):
        raise ValueError("Lists do not have the same size")
    bmis = []
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError(
                "All elements in height and weight must be int or float")
        bmis.append(w / (h ** 2))
    return bmis


def apply_limit(
    bmi: List[Union[int, float]],
    limit: int
) -> List[bool]:
    """
    Apply a limit to a list of BMI values.

    Parameters:
    bmi (List[Union[int, float]]): A list of BMI values.
    limit (int): The limit to compare each BMI value against.

    Returns:
    List[bool]: A list of boolean values indicating whether each BMI value is
    greater than the limit.

    Raises:
    TypeError: If limit is not an integer or if any element in bmi is not an
    int or float.
    """
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer")
    result = []
    for val in bmi:
        if not isinstance(val, (int, float)):
            raise TypeError("All elements in bmi must be int or float")
        result.append(val > limit)
    return result


# Using NumPy arrays
def numpy_give_bmi(
    height: np.ndarray,
    weight: np.ndarray
) -> np.ndarray:
    """
    Calculate the Body Mass Index (BMI) for each pair of height and weight
    using NumPy arrays.

    Parameters:
    height (np.ndarray): A NumPy array of heights in meters.
    weight (np.ndarray): A NumPy array of weights in kilograms.

    Returns:
    np.ndarray: A NumPy array of BMI values corresponding to each height and
    weight pair.

    Raises:
    TypeError: If height or weight is not a NumPy array or if their elements
    are not int or float.
    ValueError: If the height and weight arrays do not have the same size.
    """
    if (not isinstance(height, np.ndarray)
            or not isinstance(weight, np.ndarray)):
        raise TypeError("Arrays must be numpy arrays")
    if height.size != weight.size:
        raise ValueError("Arrays do not have the same size")
    if ((height.dtype.kind not in ('i', 'f'))
            or (weight.dtype.kind not in ('i', 'f'))):
        raise TypeError("Values must be ints or floats")
    return weight / height ** 2


def numpy_apply_limit(
    bmi: np.ndarray,
    limit: int
) -> np.ndarray:
    """
    Apply a limit to a NumPy array of BMI values.

    Parameters:
    bmi (np.ndarray): A NumPy array of BMI values.
    limit (int): The limit to compare each BMI value against.

    Returns:
    np.ndarray: A NumPy array of boolean values indicating whether each BMI
    value is greater than the limit.

    Raises:
    TypeError: If bmi is not a NumPy array or if its elements are not int or
    float.
    """

    if not isinstance(bmi, np.ndarray):
        raise TypeError
    for val in bmi:
        if not isinstance(val, (int, float)):
            raise TypeError("All elements in bmi must be int or float")
    return bmi > limit


def main():
    try:
        print("PYTHON\nTest list different sizes (height)")
        height = [2.71, 1.15, 1.34]
        weight = [165.3, 38.4]
        bmis = give_bmi(height, weight)
        print(bmis)
        if (isinstance(bmis, list)):
            print(apply_limit(bmis, 26))
    except (TypeError, ValueError) as e:
        print(str(e))

    try:
        print("NUMPY\nTest list different sizes (height)")
        height = np.array(height)
        weight = np.array(weight)
        bmis = numpy_give_bmi(height, weight)
        print(bmis)
        if (isinstance(bmis, np.ndarray)):
            print(numpy_apply_limit(bmis, 26))
    except (TypeError, ValueError) as e:
        print(str(e))

    try:
        print("PYTHON\nTest list different sizes (weight)")
        height = [2.71, 1.15]
        weight = [165.3, 38.4, 70.0]
        bmis = give_bmi(height, weight)
        print(bmis)
        if (isinstance(bmis, list)):
            print(apply_limit(bmis, 26))
    except (TypeError, ValueError) as e:
        print(str(e))

    try:
        print("NUMPY\nTest list different sizes (weight)")
        height = np.array(height)
        weight = np.array(weight)
        bmis = numpy_give_bmi(height, weight)
        print(bmis)
        if (isinstance(bmis, np.ndarray)):
            print(numpy_apply_limit(bmis, 26))
    except (TypeError, ValueError) as e:
        print(str(e))

    try:
        print("PYTHON\nTest invalid list element (height)")
        height = [2.71, 1.15, 'str']
        weight = [165.3, 38.4, 40.2]
        bmis = give_bmi(height, weight)
        print(bmis)
        if (isinstance(bmis, list)):
            print(apply_limit(bmis, 26))
    except (TypeError, ValueError) as e:
        print(str(e))

    try:
        print("NUMPY\nTest invalid list element (height)")
        height = np.array(height)
        weight = np.array(weight)
        bmis = numpy_give_bmi(height, weight)
        print(bmis)
        if (isinstance(bmis, np.ndarray)):
            print(numpy_apply_limit(bmis, 26))
    except (TypeError, ValueError) as e:
        print(str(e))

    try:
        print("PYTHON\nTest invalid list element (weight)")
        height = [2.71, 1.15, 1.33]
        weight = [165.3, 38.4, 'str']
        bmis = give_bmi(height, weight)
        print(bmis)
        if (isinstance(bmis, list)):
            print(apply_limit(bmis, 26))
    except (TypeError, ValueError) as e:
        print(str(e))

    try:
        print("NUMPY\nTest invalid list element (weight)")
        height = np.array(height)
        weight = np.array(weight)
        bmis = numpy_give_bmi(height, weight)
        print(bmis)
        if (isinstance(bmis, np.ndarray)):
            print(numpy_apply_limit(bmis, 26))
    except (TypeError, ValueError) as e:
        print(str(e))


if __name__ == "__main__":
    main()
