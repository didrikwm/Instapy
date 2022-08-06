import cv2

sepia_matrix = [[0.393, 0.769, 0.189],
                [0.349, 0.686, 0.168],
                [0.272, 0.534, 0.131]]

def python_color2sepia(image, amount=None):
    """Transforms an image to a sepia version using solely Python code.

    Args:
        image (Numpy Array): A numpy array representing the image to be transformed.

    Returns:
        The sepia version of the initial image.
    """
    if amount == None:
        amount = 1

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            r, g, b = image[i,j,2], image[i,j,1], image[i,j,0]

            nb = b + (((r * sepia_matrix[2][0] + g * sepia_matrix[2][1] + b * sepia_matrix[2][2]) - b) * amount)
            ng = g + (((r * sepia_matrix[1][0] + g * sepia_matrix[1][1] + b * sepia_matrix[1][2]) - g) * amount)
            nr = r + (((r * sepia_matrix[0][0] + g * sepia_matrix[0][1] + b * sepia_matrix[0][2]) - r) * amount)

            image[i,j,0] = int(nb) if int(nb) < 255 else 255
            image[i,j,1] = int(ng) if int(ng) < 255 else 255
            image[i,j,2] = int(nr) if int(nr) < 255 else 255

    return image.astype("uint8")
