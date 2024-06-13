import subprocess
import sys
import numpy as np
from ex00.give_bmi import give_bmi, apply_limit, numpy_give_bmi, numpy_apply_limit
from ex01.array2D import slice_me_test

def test_ex00():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    # Float to float comparaison, might turn it to STR
    bmis = give_bmi(height, weight)
    assert bmis == [22.507863455018317, 29.0359168241966]
    numpy_bmis = numpy_give_bmi(np.array(height), np.array(weight))
    assert str(numpy_bmis) == "[22.50786346 29.03591682]"
    assert apply_limit(bmis, 26) == [False, True]
    assert str(numpy_apply_limit(numpy_bmis, 26)) == "[False  True]"
    height = [2.71, 1.15]
    weight = [165.3, 38.4, 70]
    

def test_ex01():
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]

    assert slice_me_test(family, 0, 2) == "My shape is: (4, 2)\nMy new shape is: (2, 2)\n[[1.8, 78.4], [2.15, 102.7]]"
    assert slice_me_test(family, 1, -2) == "My shape is: (4, 2)\nMy new shape is: (1, 2)\n[[2.15, 102.7]]"
    try:
        slice_me_test(family, "salut", 2)
    except TypeError as e:
        assert str(e) == "Invalid parameter type"
    try:
        slice_me_test(family, 2, 'e')
    except TypeError as e:
        assert str(e) == "Invalid parameter type"
    try:
        slice_me_test('blabla', 2, 3)
    except TypeError as e:
        assert str(e) == "Invalid parameter type"
    assert slice_me_test([1, 2, 3, 4, 5], 1, -2) == "My shape is: (5,)\nMy new shape is: (2,)\n[2, 3]"


if __name__ == "__main__":
    test_ex00()
