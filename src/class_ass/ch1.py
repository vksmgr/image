import cv2
import numpy as np


def callMe():
    sumaary()
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
    key = cv2.waitKey(0) & 0xFF
    if key == 27:
        print("entred")
        cv2.destroyAllWindows()
    elif key == ord('s'):
        imwrite("myimage.png", img)
        cv2.destroyAllWindows()
    pass
