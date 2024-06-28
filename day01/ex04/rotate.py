import numpy as np
from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt
import sys


def ft_rotate(image: np.array) -> np.array:
    print(image)
    return image


if __name__ == "__main__":
    try:
        if (len(sys.argv) == 2):
            array = ft_zoom(ft_load(sys.argv[1]))
            print(f"The shape of the image is: {array.shape} or "
                  f"({array.shape[0]}, {array.shape[1]})")
            print(array)
            ft_rotate(array[:, :])
        else:
            print("Please a valid number of arguments")
    except Exception as e:
        print(f"Error: {e}")
