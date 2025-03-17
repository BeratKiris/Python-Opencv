import cv2
import numpy as np 
img= cv2.imread("Resimlerr/zeytin.png")
imgGri= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Zeytin fotosu",img)
cv2.imshow("Zeytin fotosu GRİ",imgGri)

size_y=img.shape[0] #yükseklik
size_x=img.shape[1] #genişlik
kanal= img.shape[2]   

print("yükseklik:",size_y,"genişlik:",size_x,"kanal sayısı:",kanal)
print(img[100,100])
print(imgGri[100,100]) #x ve y deki 100 noktasındaki  renki


cv2.waitKey(0)
cv2.destroyAllWindows()