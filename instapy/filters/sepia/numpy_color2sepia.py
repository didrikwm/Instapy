import cv2

sepia_matrix = [[0.393, 0.769, 0.189],
                [0.349, 0.686, 0.168],
                [0.272, 0.534, 0.131]]

def numpy_color2sepia(image, amount=None):
    """Transforms an image to a sepia version using Numpy slicing.

    Args:
        image (Numpy Array): A numpy array representing the image to be transformed.

    Returns:
        The sepia version of the initial image.
    """
    b, g, r = image[:,:,0], image[:,:,1], image[:,:,2]

    if amount == None:
        amount = 1

    nb = b + (((r * sepia_matrix[2][0] + g * sepia_matrix[2][1] + b * sepia_matrix[2][2]) - b) * amount)
    ng = g + (((r * sepia_matrix[1][0] + g * sepia_matrix[1][1] + b * sepia_matrix[1][2]) - g) * amount)
    nr = r + (((r * sepia_matrix[0][0] + g * sepia_matrix[0][1] + b * sepia_matrix[0][2]) - r) * amount)

    nr[nr > 255] = 255
    ng[ng > 255] = 255
    nb[nb > 255] = 255

    image[:,:,0] = nb.astype(int)
    image[:,:,1] = ng.astype(int)
    image[:,:,2] = nr.astype(int)

    return image.astype("uint8")