from PIL import Image
import numpy as np
import sys


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
            return array
    except FileNotFoundError:
        print("File not found!")
        return np.array([])
    except Exception as e:
        print(f"Error: {e}")
        return np.array([])


if __name__ == "__main__":
    try:
        if (len(sys.argv) == 2):
            array = ft_load(sys.argv[1])
            if array == np.array([]):
                raise FileNotFoundError("File not found!")
            print(f"The shape of the image is: {array.shape}")
            print(array)
        else:
            print("Please provide a file path")
    except Exception as e:
        print(f"Error: {e}")

