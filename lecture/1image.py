# 1. 이미지 불러오기

import cv2 # 패키지 불러오기
img = cv2.imread('data/Dog.jpg')
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# import cv2

# img = cv2.imread('data/Dog.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('image', gray)
# cv2.waitKey()
# cv2.destroyAllWindows()

# import cv2

# img = cv2.imread('data/Dog.jpg')

# cv2.imshow('image', img)
# cv2.waitKey(1000)
# cv2.destroyAllWindows()