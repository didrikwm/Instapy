# Instapy


## The package instapy 

### Prerequisites
Python (at least 3.8) is installed.

Pytest (at least 6.2.5) is installed. Install with `$ pip install -U pytest`

Numpy (at least 1.20.3) is installed. Install with `$ pip install numpy`

Numba (at least 0.54.0) is installed. Install with `$ pip install numba`

OpenCV is installed. Install with `$ pip install opencv-python`


The package is intended to be installed and run on a Linux computer (more specifically an Ifi machine).

### Notes
The user may experience errors due to different metacharacters for newline on Windows/Linux. In that case, the format of the file giving the error may be converted to the correct Linux format by opening the file in Vim and typing "_:set ff=unix_".

This was an assignment for the course IN3110 at the Department of Informatics at the University of Oslo.

### Functionality
The main functionality of this assignment is to let the user transform an image to grayscale or sepia. This is achieved with the package 'instapy'. The user may select the image to be transformed, the destination for the transformed image, as well as extra functionality such as selecting the implementation (python, numpy or numba) to be used, scaling the image, applying stepless sepia filter and tracking the runtime of the transformation process.

### Missing functionality
There is little to no error handling. This is something I could implement, but since the assignment text does not mention it at all, I figured it was not required. I figured as long as my scripts fulfill the requirements of the assignment, that's satisfactory.

### Installation
The package is installed with `$ pip install <path to directory 'instapy'>`, alternatively `$ pip install .` after navigating to the directory _instapy_.

### Usage
The script can then be called with `$ instapy <arguments>` in any directory. For a full description of all arguments/flags, include the flag **-h** in the call. 

### Testing
Unit tests for all three implementations of both filters are written in _instapy/filters/tests/test_instapy.py_. 
The user may execute these tests simply with `$ pytest` in the top-level directory of the package, or any parent directory. 
