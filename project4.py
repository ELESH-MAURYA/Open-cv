import cv2
image=cv2.imread(r'aman.png')
gray_image=cv2.imread(r'aman.png',cv2.IMREAD_GRAYSCALE)

cv2.imshow('colorimage',image)
cv2.imshow('grayimage',gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()