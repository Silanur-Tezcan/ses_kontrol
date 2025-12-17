# 🎥 El Hareketleri ile Ses Kontrolü

Bu proje, web kamera kullanarak el hareketleriyle bilgisayarın ses seviyesini kontrol etmeyi amaçlayan
basit bir görüntü işleme uygulamasıdır.

## 🚀 Projenin Amacı

- Temassız bir şekilde ses kontrolü sağlamak
- OpenCV ile gerçek zamanlı hareket algılamayı öğrenmek
- Bilgisayar etkileşimlerinde görüntü işlemenin kullanımını göstermek

## 🧠 Nasıl Çalışır?

1. Web kameradan anlık görüntü alınır.
2. Arka plan çıkarma (Background Subtraction) yöntemi ile hareketli nesneler tespit edilir.
3. En büyük hareketli alan (el olduğu varsayılan) belirlenir.
4. Elin konumuna göre:
   - **Sağ üst bölgedeyse → Ses artırılır**
   - **Sol alt bölgedeyse → Ses azaltılır**
5. Görsel olarak ekran bölgelere ayrılır ve aktif alan vurgulanır.

## 🛠 Kullanılan Teknolojiler ve Kütüphaneler

- **Python**
- **OpenCV (cv2)**  
  - Kamera erişimi  
  - Görüntü işleme  
  - Kontur ve hareket algılama
- **NumPy**  
  - Matris ve morfolojik işlemler
- **PyAutoGUI**  
  - Sistem ses tuşlarını simüle etmek için

## 📦 Gereksinimler

```bash
pip install opencv-python numpy pyautogui
