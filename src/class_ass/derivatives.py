# we will calculate the darivative of an image

import numpy as np
import cv2
from matplotlib import pyplot as plt


def callMe():
    # der()
    test()
    pass


def der():
    img = cv2.imread("/home/hp/PycharmProjects/image/data/dog2.jpg", 0)
    # cv2.imshow('Image', img)
    print(img.shape)
    print(img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass

# this will give the derivative element for the position
def get_element(input_matx, derivative_mask):
    return np.sum(input_matx * derivative_mask)

def test():
    # a = np.arange(12).reshape(4, 3)
    b = np.array([[255, 255, 255, 255, 255], [255, 255, 255, 255, 255], [255, 255, 255, 255, 255], [255, 255, 255, 255, 255], [255, 255, 255, 255, 255]])
    c = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    # (i, j) = b.shape
    # print(i, j)




    # res = np.sum(b*c)
    # print(res)
    # print(a)
    # c = a.sum()
    # print(c)
    pass
