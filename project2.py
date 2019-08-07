import cv2
project_image=cv2.imread(r'elu.png')
print(project_image)
print(type(project_image))
print(project_image.shape)
print(project_image.ndim)
b=project_image[:,:,0]
g=project_image[:,:,1]
r=project_image[:,:,2]
print("Blue:{} green:{} Red:{}".format(b,g,r))
cv2.imshow("colorimage",project_image)
cv2.imshow("green",g)
cv2.waitKey(0)
cv2.destroyAllWindows()
