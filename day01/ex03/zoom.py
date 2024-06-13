import numpy as np
from load_image import ft_load


def ft_zoom(image: np.array) -> np.array:
    try:
        image = Image.fromarray(image[200:200], 'RGB')
        image.save()
    except Exception as e:
        print(f"Error: {e}")