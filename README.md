# Project Ülgen - Otonom Taret Sistemi

**Project Ülgen**, Robot Programlama dersi kapsamında geliştirilen, ROS 1 (Robot Operating System) ve Gazebo simülasyon ortamı üzerinde çalışan otonom bir taret (savunma sistemi) projesidir. 

Sistem, ortamdaki kamera verisini gerçek zamanlı işleyerek düşman (kırmızı) hedefleri tespit eden görüntü işleme algoritmaları barındırmakta ve tareti bu hedeflere yönlendirmeyi amaçlamaktadır.

## Ekip ve Görev Dağılımı
Bu proje 4 kişilik bir ekip tarafından geliştirilmektedir. Görev dağılımı sistemin farklı modüllerine (Mekanik Tasarım, ROS Haberleşmesi, Motor Kontrolü ve Görüntü İşleme) ayrılmıştır.
* **Görüntü İşleme & Hedef Tespiti:** Muhammed Talha Şahin (OpenCV, Renk Maskeleme, Merkez Koordinat Hesaplama)
* *(Diğer ekip arkadaşlarının isimlerini ve görevlerini buraya yazabilirsiniz)*

## Kullanılan Teknolojiler
* **İşletim Sistemi:** Ubuntu 20.04 (WSL/VirtualBox)
* **Simülasyon & Altyapı:** ROS 1 Noetic, Gazebo
* **Yazılım Dilleri:** Python 3, XML (URDF/XACRO)
* **Görüntü İşleme:** OpenCV, cv_bridge, Numpy

---

## Proje Dizin Yapısı

Proje içerisindeki paket yapısı standart ROS mimarisine uygun olarak düzenlenmiştir:

* **`launch/`**: Simülasyonu başlatan dosyaları içerir. `gazebo.launch` dosyası, Gazebo ortamını açar, haritayı yükler ve Ülgen'i dünyanın içine yerleştirir.
* **`urdf/`**: Ülgen'in fiziksel tasarım dosyalarını barındırır. Robotun şasesi, taretin döner eklemleri (Pan/Tilt joint'leri) ve üzerindeki sensörlerin geometrik yapıları burada tanımlıdır.
* **`scripts/`**: Sistemin yazılım ve yapay zeka/görüntü işleme kısmıdır. Kameradan gelen ROS görüntü verilerini (`sensor_msgs/Image`) işleyen, HSV renk uzayında kırmızı hedefleri tespit eden ve taretin hareketi için gerekli olan X,Y merkez koordinatlarını hesaplayan Python modüllerini barındırır.

---

## Kurulum ve Derleme

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları sırasıyla terminalinizde uygulayın:

**1. ROS Çalışma Alanına Geçin:**
```bash
cd ~/catkin_ws/src
````
**2. Projeyi Klonlayın:**
```bash
git clone [https://github.com/Talhasahinn/ULGEN.git](https://github.com/Talhasahinn/ULGEN.git) project_ulgen
```
**3. Gerekli İzinleri Verin**
```bash
chmod +x ~/catkin_ws/src/project_ulgen/scripts/*.py
```
**4. Projeyi Derleyin**
```bash
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```

**Sistemi Çalıştırma**
```bash
roslaunch project_ulgen gazebo.launch
```
