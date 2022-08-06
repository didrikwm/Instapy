from instapy.filters.sepia.numba_color2sepia import numba_color2sepia
from instapy.filters.sepia.python_color2sepia import python_color2sepia
from instapy.filters.sepia.numpy_color2sepia import numpy_color2sepia
from instapy.filters.grayscale.numba_color2gray import numba_color2gray
from instapy.filters.grayscale.numpy_color2gray import numpy_color2gray
from instapy.filters.grayscale.python_color2gray import python_color2gray
import numpy
from random import randint
import cv2

def test_grayscale():
    array = numpy.random.randint(0, 256, size=(100, 100, 3))
    randIndexH = randint(0, array.shape[0]-1)
    randIndexW = randint(0, array.shape[1]-1)
    refPixel = array[randIndexH, randIndexW] # The random pixel to use as reference.
    refValue = int(0.07 * refPixel[0] + 0.72 * refPixel[1] + 0.21 * refPixel[2]) # Calculates the value we expect for that pixel after grayscale.

    # Python:
    grayArrayPython = python_color2gray(numpy.copy(array))
    assert grayArrayPython[randIndexH, randIndexW, 0] == refValue

    # Numpy:
    grayArrayNumpy = numpy_color2gray(numpy.copy(array))
    assert grayArrayNumpy[randIndexH, randIndexW] == refValue # In the Numpy implementation, only one value is stored in each pixel, so no need for 3 indices.

    # Numba:
    grayArrayNumba = numba_color2gray(numpy.copy(array))
    assert grayArrayNumba[randIndexH, randIndexW, 0] == refValue

def test_sepia():
    sepia_matrix = [[0.393, 0.769, 0.189],
                    [0.349, 0.686, 0.168],
                    [0.272, 0.534, 0.131]]

    array = numpy.random.randint(0, 256, size=(100, 100, 3)).astype("uint8")
    randIndexH = randint(0, array.shape[0]-1)
    randIndexW = randint(0, array.shape[1]-1)
    refPixel = numpy.array(array[randIndexH, randIndexW]) # The random pixel to use as reference.
    r, g, b = refPixel[2], refPixel[1], refPixel[0]
    nr = (r * sepia_matrix[2][0]) + (g * sepia_matrix[2][1]) + (b * sepia_matrix[2][2])
    ng = (r * sepia_matrix[1][0]) + (g * sepia_matrix[1][1]) + (b * sepia_matrix[1][2])
    nb = (r * sepia_matrix[0][0]) + (g * sepia_matrix[0][1]) + (b * sepia_matrix[0][2])
    nr = (nr) if (nr) < 255 else 255
    ng = (ng) if (ng) < 255 else 255
    nb = (nb) if (nb) < 255 else 255
    refValues = numpy.array([nr, ng, nb]).astype("uint8")

    # Python:
    sepiaArrayPython = python_color2sepia(numpy.copy(array))
    assert (sepiaArrayPython[randIndexH, randIndexW] == refValues.astype("uint8")).all()

    # Numpy:
    sepiaArrayNumpy = numpy_color2sepia(numpy.copy(array))
    assert (sepiaArrayNumpy[randIndexH, randIndexW] == refValues.astype("uint8")).all()

    # Numba:
    sepiaArrayNumba = numba_color2sepia(numpy.copy(array))
    assert (sepiaArrayNumba[randIndexH, randIndexW] == refValues.astype("uint8")).all()
