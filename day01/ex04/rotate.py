import numpy as np
from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt
import sys


def ft_zoom(image: np.array) -> np.array:
    """
    Zoom into the center of the image and return a black and white version
    of the zoomed region.

    Parameters:
    image (np.array): The input image as a numpy array.

    Returns:
    np.array: The zoomed black and white image resized to the original
    image dimensions.
    The array is empty in case of error.

    Raises:
    Exception: General exception for unexpected errors.
    """
    try:
        height, width = image.shape[:2]
        zoom_factor = 2
        center_x, center_y = width // 2, height // 2
        square_size = min(height, width) // zoom_factor

        top_height = max(center_y - square_size // 2, 0)
        top_width = max(center_x - square_size // 2, 0)

        bottom_height = min(top_height + square_size, height)
        bottom_width = min(top_width + square_size, width)

        zoomed_region = image[top_height:bottom_height,
                              top_width:bottom_width, 0]

        zoomed_image = np.array(Image.fromarray(zoomed_region))
        zoomed_image = np.expand_dims(zoomed_image, axis=-1)

        # Show the original image
        # plt.imshow(Image.fromarray(image, "RGB"))
        # plt.show()
        return zoomed_image
    except Exception as e:
        print(f"Error: {e}")
        return np.array([])


def ft_rotate(image: np.array) -> np.array:
    """
    Rotate the image by 90 degrees.

    Parameters:
    image (np.array): The input image as a numpy array.

    Returns:
    np.array: The rotated image as a numpy array.
    """
    rotated_image = np.zeros((image.shape))
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rotated_image[j, i] = image[i, j]
    return rotated_image


if __name__ == "__main__":
    try:
        if (len(sys.argv) == 2):
            base_image = ft_load(sys.argv[1])
            if base_image == np.array([]):
                raise FileNotFoundError("File not found!")
            array = ft_zoom(base_image)
            print(f"The shape of the image is: {array.shape} or "
                  f"({array.shape[0]}, {array.shape[1]})")
            print(array)
            rotated_array = ft_rotate(array[:, :, 0])
            print(f"New shape after Transpose: {rotated_array.shape}")
            print(rotated_array)
            plt.imshow(rotated_array, cmap='gray')
            plt.show()
        else:
            print("Please a valid number of arguments")
    except Exception as e:
        print(f"Error: {e}")
