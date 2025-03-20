import cv2

# Video kaydetmek için VideoCapture nesnesi oluşturuyoruz
cap = cv2.VideoCapture(0)

# Video kaydediciyi başlatmak için bir codec tanımlıyoruz
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = None
recording = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Video penceresini göster
    cv2.imshow('Video', frame)

    # Kullanıcının tuş basımlarını kontrol et
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):  # 's' tuşuna basıldığında kayda başla
        if not recording:
            out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
            recording = True
            print("Kayda başlandı.")

    if recording:
        # Video kaydediliyorsa frame'leri kaydet
        out.write(frame)

    if key == ord('q'):  # 'q' tuşuna basıldığında kaydı durdur ve çık
        print("Kaydedilen video sonlandırılıyor.")
        break

# Kaynakları serbest bırak
cap.release()
if out:
    out.release()
cv2.destroyAllWindows()
