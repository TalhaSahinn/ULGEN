Ülgen Taret Projesi 

Bu proje, ROS (Robot Operating System) 1 Noetic ve Gazebo simülasyon ortamı kullanılarak geliştirilmiş, yapay zeka destekli otonom bir taret (Ülgen) sistemidir. Sistem, kamera verilerini işleyerek düşman (kırmızı) hedefleri tespit eder ve otonom kilitlenme sağlar.

Projeyi Çalıştırma

Projeyi ve Gazebo simülasyonunu başlatmak için terminalinizde şu komutu çalıştırmanız yeterlidir:

roslaunch project_ulgen gazebo.launch


Klasör Yapısı ve İçerikleri

Projemiz standart ROS paketi mimarisine uygun olarak düzenlenmiştir. Ana dizinlerimiz ve görevleri şunlardır:

urdf/ (Ülgen'in Kendisi):
Robotun (Ülgen) fiziksel tasarımı, eklemleri, boyutları ve kamera/sensör yerleşimlerini tanımlayan model dosyaları burada bulunur. Ülgen'in iskeleti ve mekanik yapısı bu klasörden yönetilir.

scripts/ (Yapay Zeka ve Yazılım):
Projenin beyni burasıdır. Kameradan gelen görüntüleri işleyen, kırmızı hedefleri (düşman dronları) tespit eden (örn: kirmizi_tespit.py) ve taretin hareketlerini yönlendiren Python kodlarımız bu klasörde yer alır.

launch/ (Başlatıcılar):
Sistemi tek tek elle başlatmak yerine, Gazebo simülasyon ortamını, Ülgen'in URDF modelini ve arkada çalışan Python script'lerini tek bir komutla ayağa kaldırmaya yarayan yapılandırma dosyalarıdır. gazebo.launch dosyası bu klasörden çağrılır.

Ekip Çalışması İçin Not

Projeyi GitHub'dan kendi bilgisayarına çeken (clone) ekip üyelerinin projeyi çalıştırmadan önce catkin_ws dizininde catkin_make ve source devel/setup.bash komutlarını çalıştırması gerekmektedir.
