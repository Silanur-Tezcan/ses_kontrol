import cv2
import numpy as np
import pyautogui

cap = cv2.VideoCapture(0)
# Arka plan çıkarıcı
fgbg = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=False)

while True:
    ret, frame = cap.read()
    if not ret: break
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Görüntü işleme
    fgmask = fgbg.apply(frame)
    kernel = np.ones((5,5), np.uint8)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Ekrana bölgeleri belirten çizgiler ve yazılar ekleyelim
    cv2.line(frame, (w//2, 0), (w//2, h), (255, 255, 255), 2) # Orta çizgi
    cv2.putText(frame, "SOL: SES KISMA", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.putText(frame, "SAG: SES ACMA", (w//2 + 10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    if len(contours) > 0:
        largest_contour = max(contours, key=cv2.contourArea)
        if cv2.contourArea(largest_contour) > 3000:
            (x, y, w_box, h_box) = cv2.boundingRect(largest_contour)
            center_x = x + w_box // 2
            center_y = y + h_box // 2
            
            # Elin merkezine bir nokta koyalım
            cv2.circle(frame, (center_x, center_y), 10, (255, 0, 255), -1)

            # --- MANTIK ---
            # 1. Eğer el SAĞ taraftaysa ve YUKARI gidiyorsa (y küçülüyorsa)
            if center_x > w // 2:
                if center_y < h // 2: # Sağ üst bölge
                    pyautogui.press("volumeup")
                    cv2.rectangle(frame, (w//2, 0), (w, h//2), (0, 255, 0), 3) # Aktif bölgeyi parlat
            
            # 2. Eğer el SOL taraftaysa ve AŞAĞI gidiyorsa (y büyüyorsa)
            else:
                if center_y > h // 2: # Sol alt bölge
                    pyautogui.press("volumedown")
                    cv2.rectangle(frame, (0, h//2), (w//2, h), (0, 0, 255), 3) # Aktif bölgeyi parlat

    cv2.imshow("Bolgesel Ses Kontrolu", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()