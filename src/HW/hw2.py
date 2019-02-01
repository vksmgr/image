import cv2
import numpy as np
from matplotlib import pyplot as plt

def callMe():
    average_filter()
    pass


# Write a Python function that uses the convolution method to perform spatial filtering on an
# image. Start by padding your image with 5 rows and columns to the border of the image,
# the value of the padding should be 0. Apply an averaging filter and Gaussian filter with a
# kernel size of 5x5 to image given below. Display the filtered image in your report.

# as this assignmet work with the smoothing and filtering

def average_filter():
    img = cv2.imread("/home/hp/PycharmProjects/image/data/hw/hw2.png", 1)
    ## applying the smoothing to the image
    kernel = np.ones((5,5), np.float32) / 25
    dst = cv2.filter2D(img, -1, kernel)
    plt.subplot(121), plt.imshow(img), plt.title("Orignal")
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(dst), plt.title("Average Filter")
    plt.xticks([]), plt.yticks([])
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def gaussian_filter():
    img = cv2.imread("/home/hp/PycharmProjects/image/data/hw/hw2.png")