import cv2

def numpy_color2gray(image):
    """Transforms an image to a gray-scale version using Numpy slicing.

    Args:
        image (Numpy Array): A numpy array representing the image to be transformed.

    Returns:
        The gray-scaled version of the initial image.
    """
    b, g, r = image[:,:,0], image[:,:,1], image[:,:,2]
    gray = 0.07 * b + 0.72 * g + 0.21 * r
    return gray.astype("uint8")
