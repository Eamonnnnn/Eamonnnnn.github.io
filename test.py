import cv2
img=cv2.imread("logo.png")
cv2.imwrite("img_new.png",cv2.cvtColor(img,cv2.COLOR_BGR2GRAY))
img2=cv2.imread("img_new.png")
cv2.imshow("logo",img2)
cv2.waitKey(0)
cv2.destroyAllwindows()

