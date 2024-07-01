from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import sys

def ft_invert(array: np.array) -> np.array:
    """
    Invert the colors of an RGB image.

    Parameters:
    array (np.array): The input image as a numpy array in RGB format.

    Returns:
    np.array: The color-inverted image.
    """
    return 255 - array

def ft_red(array: np.array) -> np.array:
    """
    Filter the image to keep only the red channel.

    Parameters:
    array (np.array): The input image as a numpy array in RGB format.

    Returns:
    np.array: The image with only the red channel visible, other channels set to 0.
    """
    array[:, :, 1:] = 0
    return array

def ft_green(array: np.array) -> np.array:
    """
    Filter the image to keep only the green channel.

    Parameters:
    array (np.array): The input image as a numpy array in RGB format.

    Returns:
    np.array: The image with only the green channel visible, other channels set to 0.
    """
    array[:, :, ::2] = 0
    return array

def ft_blue(array: np.array) -> np.array:
    """
    Filter the image to keep only the blue channel.

    Parameters:
    array (np.array): The input image as a numpy array in RGB format.

    Returns:
    np.array: The image with only the blue channel visible, other channels set to 0.
    """
    array[:, :, :2] = 0
    return array

def ft_grey(array: np.array) -> np.array:
    """
    Convert the input RGB image array to grayscale using the luminosity method.

    Parameters:
    array (np.array): The input image as a numpy array in RGB format.

    Returns:
    np.array: The grayscale image.
    """
    grey = np.dot(array, [0.2989, 0.5870, 0.1140])
    return np.stack([grey, grey, grey], axis=-1).astype(np.uint8)


if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            functions = {
                "INVERT": ft_invert, 
                "RED": ft_red,
                "GREEN": ft_green,
                "BLUE": ft_blue,
                "GREY": ft_grey
            }
            base_image = ft_load(sys.argv[1])
            for name, function in functions.items():
                print("=" * 10 + name + "=" * 10)
                modified = function(base_image.copy())
                print(f"The shape of the image is: {modified.shape}")
                print(modified)
                plt.imshow(modified)
                plt.show()
    except Exception as e:
        print(f"Error: {e}")
