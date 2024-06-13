from PIL import Image
import numpy as np
from sys import argv


def ft_load(path: str) -> np.array:
    """
    Load an image, print its shape and its content in RGB format. Compatible
    formats: JPG, JPEG.

    Parameters:
    path (str): the path to the image.

    Returns:
    np.array: The 3D matrice of the image (h * w * rgb). The array is empty
        in case of error

    Raises:
    FileNotFoundError: If the path doesn't lead to any image
    Exception: other exceptions: invalid file...
    """
    try:
        with Image.open(path) as img:
            array = np.array(img)
            print(f"THe shape of the image is: {array.shape}")
            return array
    except FileNotFoundError:
        print("File not found!")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []


if __name__ == "__main__":
    if (len(argv) == 2):
        print(ft_load(argv[1]))
    else:
        print("Please provide a file path")
