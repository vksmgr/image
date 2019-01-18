# in this module we will learn how to process image using opencv
import cv2
import numpy as np


def callMe():
    object_tracking()
    pass


def object_tracking():
    cap = cv2.VideoCapture('/home/hp/PycharmProjects/image/data/dog.mp4')
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # hsv = frame
            ## Processing the frame
            # defining the range of the blue color in the HSV
            lower_blue = np.array([0, 0, 0])
            upper_blue = np.array([0, 0, 255])

            # thresold the image to get only blue color
            mask = cv2.inRange(hsv, lower_blue, upper_blue)

            # now bitwise add the orignal image and mask
            res = cv2.bitwise_and(frame, frame, mask=mask)

            cv2.imshow('frame', res)
            # cv2.imshow('frame', hsv)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
    pass
