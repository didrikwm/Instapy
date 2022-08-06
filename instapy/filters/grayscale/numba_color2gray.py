import cv2
from numba import jit

@jit(nopython=True)
def numba_color2gray(image):
    """Transforms an image to a gray-scale version using solely Python code, and Numba.

    Args:
        image (Numpy Array): A Numpy Array representing the image to be transformed.

    Returns:
        The gray-scaled version of the initial image.
    """
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            graySum = 0
            for k in range(3):
                weight = 0.07 if k == 0 else 0.72 if k == 1 else 0.21
                graySum += image[i,j,k] * weight
            image[i,j] = graySum # Replaces the three pixel values with the one value representing the grayscale
    return image