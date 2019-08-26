import numpy
import imutils
import cv2
       
img=cv2.imread('11.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh=cv2.threshold(gray,127,255,0)
a=cv2.Canny(gray,170,200)

#ret,thresh=cv2.threshold(gray,127,255,0)
#contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#print("number of contours=" +str(len(contours)))
#print(contours[0])
#cv2.drawContours(a,contours,-15,(0,255,0),1)

cv2.imshow('image',img)
cv2.imshow(' Gray Image',gray)
cv2.imshow('new image',a)

(cnts, _) = cv2.findContours(a.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30]
NumberPlateCnt=None

count=0
for c in cnts:
    d=cv2.arcLength(c,True)
    approx= cv2.approxPolyDP(c,0.02*d,True)
    if len(approx)==4:
        NumberPlateCnt= approx
        break

cv2.drawContours(img,[NumberPlateCnt], -1,(0,255,0),3)
cv2.imshow("Final imagee with Number Plate detected",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
