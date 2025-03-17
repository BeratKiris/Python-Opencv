import cv2

img= cv2.imread(r"Resimlerr/zeytin.png")  #sonuna 0 koyduğumda gri rengine dönüştürdü

cv2.line(img,(0,0),(200,200),(100,100,100),10)  #bu noktaya çizgi attı //1. kalınlık başlangıç noktası

#//1. kalınlık başlangıç noktası //2.genişlik ve yükseklik

cv2.rectangle(img,(100,100),(300,200),(255,100,0),-1)  #sondakini - yaparsam içi dolu dkdrtgn cizer

cv2.circle(img,(300,300),150,(100,200,200),5) #yuvarlak cizdirir

cv2.putText(img,'OPENCV',(100,200),cv2.FONT_HERSHEY_SIMPLEX,2,(100,100,100),3,cv2.LINE_AA)  #yazı ekler sonuna true yazarsam ters yazar


cv2.imshow("zeytin fotosu",img)
cv2.waitKey(0)
cv2.destroyAllWindows()