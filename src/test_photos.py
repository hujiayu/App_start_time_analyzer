import cv2

im = cv2.imread('/Users/hujiayu/Desktop/report.jpg')

h, w = im.shape[:2]
print h, w

cv2.imwrite('/Users/hujiayu/Documents/picture/test.png',im)