# we will do some image arithmetics using the opencv
import numpy as np
import cv2
import src.class_ass.ch1 as ch1


def callMe():
    arithmetics()
    pass


# simple arithmetic operations using numpy and opencv
def arithmetics():
    # x = np.uint8([210])
    # y = np.uint8([60])
    # # addition using opencv function
    # print(cv2.add(x, y))
    #
    # # addition using numpy
    # print(x + y)

    ## adding two real images
    img1 = ch1.imread("dog2.jpg", 1)
    img2 = ch1.imread("dog3.jpg", 1)
    print(img1.shape)
    print(img2.shape)
    ch1.imshow(img1, "image1")
    ch1.imshow(img2, "image2")
    cv2.waitKey(0)

    # ## adding two images
    # ## to add two images both images should be of same type and depth
    # print("Adding image by open cv")
    # result = cv2.add(img2, img2)
    # ch1.imshow(result, "opencv")   # size should match of the two images
    # print("adding image using numpy")
    # res_numpy = img2+img2
    # ch1.imshow(res_numpy, "numpy")

    # adding image by weight we will add image by specifying image weight in resulting
    # image
    resu = cv2.addWeighted(img2, 0.5, img1, 0.5, 0)
    ch1.imshow(resu, "image add with wight")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass
