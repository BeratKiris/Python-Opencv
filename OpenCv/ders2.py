import cv2
import numpy as np 
img= cv2.imread("Resimlerr/zeytin.png")

#kernel= np.ones((3,3),np.float32)/9
#blur=cv2.filter2D(img,-1,kernel)          #bulanıklaştırma yaptık

#blur=cv2.blur(img,(5,5))

# kernel= np.array([[-1,-1,-1],            #keskinleştirme 
#                  [-1,9,-1],
#                  [-1,-1,-1]])

# keskinlestirme = cv2.filter2D(img, -1, kernel)

# gaus= cv2.GaussianBlur(img,(5,5),0)    #bulanaklaştırma gene

canny= cv2.Canny(img,10,200)  #keskin kenar belirleme

cv2.imshow("Zeytin fotosu",img)
cv2.imshow("Zeytin fotosu değiştirilmiş",canny)



cv2.waitKey(0)
cv2.destroyAllWindows()