# import cv2
### webcammmm
# cap = cv2.VideoCapture(0) #webcamsa 0 bilgisayardansa 1-2


# while True:
#     ret, frame = cap.read()
#     frame = cv2.flip(frame, 1)     #görünütüyü istediğimiz eksenlere göre yansıtır
   
#     cv2.imshow("webcam", frame)
#     if cv2.waitKey(1)  % 0xFF == ord("q"):  #büyüttükçe video donuyor 0 olduğunda tek fotoyu alır başta
#         break
    
    
# cap.release()
# cv2.destroyAllWindows()

################################################

import cv2

###### video dosyası

cap = cv2.VideoCapture("video/antalya.mp4") #webcamsa 0 bilgisayardansa 1-2

while True:
    ret, frame = cap.read()
    if ret == 0:
        break
    frame = cv2.flip(frame, 1)     #görünütüyü istediğimiz eksenlere göre yansıtır
   
    cv2.imshow("antalya", frame)
    if cv2.waitKey(10)  % 0xFF == ord("q"):  #büyüttükçe video donuyor 0 olduğunda tek fotoyu alır başta
        break
    
    
cap.release()
cv2.destroyAllWindows()