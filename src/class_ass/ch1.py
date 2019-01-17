import cv2
import numpy as np


def callMe():
    # sumaary()
    usingmatplot()
    pass



## Reading an image
def imread(image, mode):
    return cv2.imread("/home/hp/PycharmProjects/image/data/" + image, mode)


# This function will display the images
def imshow(image, name="IMAGE"):
    cv2.imshow(name, image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


# this function simply write the image
def imwrite(image_name, image):
    cv2.imwrite("/home/hp/PycharmProjects/image/data/" + image_name, image)


def sumaary():
    img = imread("dog.jpg", 0)
    imshow(img)
    print("Shape of width : {}".format(img.shape[0]))
    print("Shape of height : {}".format(img.shape[1]))
    key = cv2.waitKey(0) & 0xFF
    if key == 27:
        print("entred")
        cv2.destroyAllWindows()
    elif key == ord('s'):
        imwrite("myimage.png", img)
        cv2.destroyAllWindows()
    pass

# diplaying image through matplot lib
import numpy as np
from matplotlib import  pyplot as plt
def usingmatplot():
    img = imread("image.png", 1)
    plt.imshow(img)
    plt.show()
    pass