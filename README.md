# Python Algoritmaları ve Fonksiyonları

Bu proje, çeşitli matematiksel ve algoritmik sorunlara çözümler sunan bir Python uygulamasını içermektedir.

## İçerik

1. **k’nıncı En Küçük Elemanı Bulma**
    - `k_kucuk(k, liste)`: Verilen listedeki k'nıncı en küçük elemanı bulan fonksiyon.

2. **En Yakın Çifti Bulma**
    - `en_yakin_cift(hedef, liste)`: Verilen listede, hedef sayıya en yakın çifti bulan fonksiyon.

3. **Bir Listenin Tekrar Eden Elemanlarını Bulma**
    - `tekrar_eden_elemanlar(liste)`: Verilen listedeki tekrar eden elemanları bulan fonksiyon.

4. **Matris Çarpımı**
    - `matris_carpimi(a, b)`: İki matrisin çarpımını bulan fonksiyon.

5. **Bir Metin Dosyasındaki Kelimelerin Frekansını Bulma**
    - `kelime_frekansi(dosya_yolu)`: Verilen metin dosyasındaki kelimelerin frekansını bulan fonksiyon.

6. **Liste İçinde En Küçük Değeri Bulma**
    - `en_kucuk_deger(liste, n=0, kucuk=None)`: Verilen listedeki en küçük değeri bulan fonksiyon.

7. **Karekök Fonksiyonu**
    - `karekok(n, x0=1, tol=1e-10, maxiter=500, iter_count=0)`: Verilen sayının karekökünü hesaplayan fonksiyon.

8. **En Büyük Ortak Bölen Bulma**
    - `eb_ortak_bolen(a, b)`: Verilen iki sayının en büyük ortak bölenini bulan fonksiyon.

9. **Asal Veya Değil olup olmadığını Bulma**
    - `asal_veya_degil(n, bolen=2)`: Verilen sayının asal olup olmadığını kontrol eden fonksiyon.

10. **Daha Hızlı Fibonacci Hesabı**
    - `fibonacci(n)`: Verilen sıradaki Fibonacci sayısını hesaplayan fonksiyon.

## Kullanım

Proje, bir console menüsü aracılığıyla kullanıcıya çeşitli seçenekler sunmaktadır. Ana menüde istediğiniz algoritmayı seçebilir ve gerekli parametreleri girerek sonuçları görebilirsiniz.

## Kurulum

Projeyi çalıştırmak için, Python yüklü olmalıdır. Gerekli bağımlılıkları yüklemek için terminal veya komut istemcisinde aşağıdaki komutu kullanabilirsiniz:

```bash
pip install console-menu
