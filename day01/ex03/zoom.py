import numpy as np
from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt
import sys


def ft_zoom(image: np.array) -> np.array:
    try:
        height, width = image.shape[0], image.shape[1]
        # TODO zoom me
        zoomed_image = Image.fromarray(image, 'RGB')
        zoomed_image.save("zoomed.jpg") # TODO maybe remove
        plt.imshow(zoomed_image)
        plt.show()
        return image
    except Exception as e:
        print(f"Error: {e}")
        return np.array([])

if __name__ == "__main__":
    try:
        if (len(sys.argv) == 2):
            array = ft_zoom(ft_load(sys.argv[1]))
            print(f"The shape of the zoomed image is: {array.shape}")
        else:
            print("Please provide an argument")
    except Exception as e:
        print(f"Error: {e}")
