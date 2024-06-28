import numpy as np
from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt
import sys


def ft_rotate(image: np.array) -> np.array:

    return image


if __name__ == "__main__":
    try:
        if (len(sys.argv) == 2):
            ft_rotate(ft_load(sys.argv[1]))
        else:
            print("Please a valid number of arguments")
    except Exception as e:
        print(f"Error: {e}")
