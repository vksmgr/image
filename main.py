import numpy as np
import cv2

# loading color image in grayscale
image = cv2.imread("/home/hp/PycharmProjects/image/data/image.png", 0)

# Writing an image to the disk
# cv2.imwrite("/home/hp/PycharmProjects/image/data/just_image.png", image)

# displaying an image
cv2.imshow('image', image)
print(image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# printing image array
