import src.class_ass.ch1 as ch1
import cv2


def callMe():
    thr()
    pass

from matplotlib import pyplot as plt
def thr():
    img = ch1.imread("dog2.jpg", 0)

    # # these are the global threshold of an image
    # _, img_show1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # _, img_show2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    # _, img_show3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
    # _, img_show4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
    #
    # cv2.imshow("orignal", img)
    # cv2.imshow("image1", img_show1)
    # cv2.imshow("image2", img_show2)
    # cv2.imshow("image3", img_show3)
    # cv2.imshow("image4", img_show4)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    ## Adptive threshold
    img = cv2.medianBlur(img, 5)

    ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                                cv2.THRESH_BINARY, 11, 2)
    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                cv2.THRESH_BINARY, 11, 2)

    titles = ['Original Image', 'Global Thresholding (v = 127)',
              'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    images = [img, th1, th2, th3]

    for i in range(4):
        plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()
    pass
