import cv2
image=cv2.imread(r'aman.png')

image_gray=cv2.imread(r"aman.png",cv2.IMREAD_GRAYSCALE)
face_teacher=cv2.CascadeClassifier(r"E:\image processing\haarcascades\haarcascade_frontalface_default.xml")
face=face_teacher.detectMultiScale(image_gray,1.3,5)
print(face)
for x,y,w,h in face:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

print("face location is " ,face)
print("number of persion is :",len(face))
cv2.imshow("window",image)
#cv2.imshow("gray",image_gray)
cv2.waitKey()
cv2.destroyAllWindows()