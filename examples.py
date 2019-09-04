# author: Adrian Rosebrock
# date: 14 January 2014
# website: http://www.pyimagesearch.com

# import the necessary packages
import cv2

# load the image and show it
image = cv2.imread("demoimage.jpg")
#cv2.imshow("original", image)
#cv2.waitKey(0)

# print the dimensions of the image
print image.shape

# we need to keep in mind aspect ratio so the image does
# not look skewed or distorted -- therefore, we calculate
# the ratio of the new image to the old image
r = 100.0 / image.shape[1]
dim = (100, int(image.shape[0] * r))

# perform the actual resizing of the image and show it
#resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
#cv2.imwrite("resized.jpg", resized)
#cv2.waitKey(0)

# grab the dimensions of the image and calculate the center
# of the image
(h, w) = image.shape[:2]
center = (w / 2, h / 2)


print(center)
# rotate the image by 180 degrees
"""
M = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("rotated", rotated)
cv2.waitKey(0)
"""

# crop the image using array slices -- it's a NumPy array
# after all!




cropped = image[409:619, 413:1027]
cv2.imwrite("cropped.jpg", cropped)

cropped2 = image[0:409, 400:1027]
cv2.imwrite("cropped2.jpg", cropped2)



#cv2.waitKey(0)

# write the cropped image to disk in PNG format
#cv2.imwrite("thumbnail.png", cropped)