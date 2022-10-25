import cv2
import os
cam = cv2.VideoCapture(0)
cam.set(3, 640) # Video çözünürlük  genişlik
cam.set(4, 480) # Video çözünürlük yükseklik
face_detector = cv2.CascadeClassifier('Cascades\haarcascade_frontalface_default.xml')
# Her bir kişi için numara verin
face_id = input('\n Kullanıcı id girin ve bir tuşa basın ==>  ')
print("\n [INFO]Kamera fotoğrafınızı çekerken lütfen bekleyin ...")
# Foto sayacı
count = 0
while(True):
    ret, img = cam.read()
    img = cv2.flip(img, -1) # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1
        # Fotografların kaydedileceği dosya
        cv2.imwrite("Cascades/user." + str(face_id) + '.' +  
                    str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('image', img)
    k = cv2.waitKey(100) & 0xff # çıkmak için  'ESC' basın
    if k == 27:
        break
    elif count >= 30: # 30 adet fotograf cekilecek.
         break
# Programı sonlandırın
print("\n [INFO] Çıkış yapılıyor")
cam.release()
cv2.destroyAllWindows()