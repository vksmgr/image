# may be this will be useful to work with the
# streaming videos
# we will work with some videos


# playing video from the file

def callMe():
    play()
    pass


import numpy as np
import cv2


def play():
    cap = cv2.VideoCapture('/home/hp/PycharmProjects/image/data/video.mp4')
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', gray)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
