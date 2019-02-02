import cv2
import numpy as np
from matplotlib import pyplot as plt


def callMe():
    ## reading an image
    img = cv2.imread("/home/hp/PycharmProjects/image/data/hw/hw2.png", 0)
    showImgComp(img, average_filter(img))
    showImgComp(img, gaussian_filter(img))
    pass


def showImgComp(orignal, new):
    plt.subplot(121), plt.imshow(orignal), plt.title("Orignal")
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(new), plt.title("Modified")
    plt.xticks([]), plt.yticks([])
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass


# Write a Python function that uses the convolution method to perform spatial filtering on an
# image. Start by padding your image with 5 rows and columns to the border of the image,
# the value of the padding should be 0. Apply an averaging filter and Gaussian filter with a
# kernel size of 5x5 to image given below. Display the filtered image in your report.

# as this assignment work with the smoothing and filtering
def average_filter(img):
    ## applying the smoothing to the image
    kernel = np.ones((5, 5), np.float32) / 25
    img_out = cv2.filter2D(img, -1, kernel)
    return img_out


## Function for the gaussian filter
def gaussian_filter(img):
    img_out = img.copy()
    height = img.shape[0]
    width = img.shape[1]

    gauss = (1.0 / 273) * np.array(
        [[1, 4, 7, 4, 1],
         [4, 16, 26, 16, 4],
         [7, 26, 41, 26, 7],
         [4, 16, 26, 16, 4],
         [1, 4, 7, 4, 1]])

    # Printing gaussian kernel
    # print(gauss)

    for i in np.arange(2, height - 2):
        for j in np.arange(2, width - 2):
            sum = 0
            for k in np.arange(-2, 3):
                for l in np.arange(-2, 3):
                    a = img.item(i + k, j + l)
                    p = gauss[2 + k, 2 + l]
                    sum = sum + (p * a)
            b = sum
            img_out.itemset((i, j), b)

    return img_out
