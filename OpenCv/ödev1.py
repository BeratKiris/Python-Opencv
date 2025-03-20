import cv2

cap = cv2.VideoCapture(0)

photo_counter = 1  # Fotoğraf numaralandırma için sayaç oluş

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow("webcam live", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):  # 's' tuşuna bas foto alır kaydederiz
        photo_filename = f"C:\\Users\\BT\\Desktop\\Visual Studio code\\OpenCv\\photo_{photo_counter}.jpg"
        cv2.imwrite(photo_filename, frame)
        print(f"Fotoğraf kaydedildi: {photo_filename}")
        photo_counter += 1  # Fotoğraf numarasını artırır birden fazla foto alırsak mesela

    elif key == ord('q'):  # 'q' tuşuna basıldığında çıkar ekran kapanır
        break


cap.release()
cv2.destroyAllWindows()
