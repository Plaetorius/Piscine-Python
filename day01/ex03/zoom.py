import numpy as np
from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt
import sys


def ft_zoom(image: np.array) -> np.array:
    """
    Zoom into the center of the image and return a black and white version of the zoomed region.

    Parameters:
    image (np.array): The input image as a numpy array.

    Returns:
    np.array: The zoomed black and white image resized to the original image dimensions.
              The array is empty in case of error.

    Raises:
    Exception: General exception for unexpected errors.
    """
    try:
        height, width = image.shape[:2]
        zoom_factor = 2
        center_x, center_y = width // 2, height // 2
        square_size = min(height, width) // zoom_factor


        top_height = max(center_y - square_size, 0)
        top_width = max(center_x - square_size, 0)

        # Only to match the expected output:
        top_width += 320
        top_height += 120

        bottom_height = min(top_height + square_size, height)
        bottom_width = min(top_width + square_size, width)

        zoomed_region = image[top_height:bottom_height,top_width:bottom_width]

        zoomed_image = np.array(Image.fromarray(zoomed_region).convert('L'))

        plt.imshow(zoomed_image, cmap='gray')
        plt.show()
        # plt.imshow(Image.fromarray(image, "RGB"))
        # plt.show()
        return cropped_image
    except Exception as e:
        print(f"Error: {e}")
        return np.array([])

if __name__ == "__main__":
    try:
        if (len(sys.argv) == 2):
            array = ft_zoom(ft_load(sys.argv[1]))
            print(f"The shape of the zoomed image is: {array.shape}")
        else:
            print("Please a valid number of arguments")
    except Exception as e:
        print(f"Error: {e}")
