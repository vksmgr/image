import cv2
import numpy as np
from matplotlib import pyplot as plt


def callMe():
    Q()
    pass


def Q():
    # first i'll read an image
    image = cv2.imread("/home/hp/PycharmProjects/image/data/hw/lena.png", 0)

    # printing the histogram of the image
    printHisto(image,128, [0,256])

    # then i'll display it to show
    cv2.imshow("image", image)
    cv2.waitKey(0)

    ## Applying function to the image and writing back the image
    img = f(image)
    cv2.imwrite("/home/hp/PycharmProjects/image/data/hw/modimg.png", img)

    # printing the modified image
    modimg = cv2.imread("/home/hp/PycharmProjects/image/data/hw/modimg.png", 0)
    cv2.imshow("modimg", modimg)

    printHisto(modimg, 128, [0, 256])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass

## Function for the question 1
## Function to operate on the each pixel in the image
def f(x):
    power = (pow(x / 255, 2.5) * 255)
    y = np.array(power)
    y = y.astype(int)
    return y

# function for the question 2
# writing the function to print the image histogram
# this function will take image, numberofbins and the range of the input int the image
def printHisto(image, bins, range):
    plt.hist(image.ravel(), bins=bins, range=range)
    plt.show()
    pass