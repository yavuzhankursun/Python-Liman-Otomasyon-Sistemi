# Liman Yönetim Sistemi

Bu proje, bir liman yönetim sisteminin basit bir simulasyonunu gerçekleştiren Python kodunu içermektedir. Liman, tırların yük indirmesini ve gemilere yük yükleme işlemlerini simüle eder.

## Kullanılan Modüller

1. `csv`: CSV dosyalarından veri okuma işlemleri için kullanılmıştır.
2. `heapq`: Küçükten büyüğe sıralı bir kuyruk yapısı sağlamak için kullanılmıştır.

## Sınıflar

### 1. Tir Sınıfı
Tır nesnelerinin özelliklerini ve davranışlarını tanımlar.

- `__init__(self, plaka, ulke, yirmi_ton, otuz_ton, maliyet)`: Tır nesnesini başlatır.
- `__lt__(self, other)`: Tırları plakalarına göre sıralamak için kullanılan karşılaştırma metodu.

### 2. Gemi Sınıfı
Gemi nesnelerinin özelliklerini ve davranışlarını tanımlar.

- `__init__(self, numara, kapasite, hedef_ulke)`: Gemi nesnesini başlatır.
- `__lt__(self, other)`: Gemileri numaralarına göre sıralamak için kullanılan karşılaştırma metodu.

### 3. Liman Sınıfı
Limanın özelliklerini ve liman işlemlerini yöneten metotları içerir.

- `__init__(self)`: Liman nesnesini başlatır.
- `tir_bilgisi_okuma(self)`: Olaylar CSV dosyasından tır bilgilerini okur ve kuyruğa ekler.
- `gemi_bilgisi_okuma(self)`: Gemiler CSV dosyasından gemi bilgilerini okur ve kuyruğa ekler.
- `tir_yuk_indirme(self)`: Tırları istif alanına yerleştirir ve yük indirme işlemlerini simüle eder.
- `gemi_yuk_yukleme(self)`: Gemilere tırları yükler ve limandan ayrılan gemileri takip eder.

## Nasıl Kullanılır

1. Proje dosyalarını indirin.
2. Python yüklü değilse, [Python'un resmi web sitesinden](https://www.python.org/downloads/) Python'u indirip yükleyin.
3. Terminal veya komut istemcisinde proje dizinine gidin.
4. `pip install -r requirements.txt` komutu ile gerekli modülleri yükleyin.
5. `python main.py` komutu ile programı çalıştırın.

## Örnek Kullanım

Proje, `olaylar.csv` ve `gemiler.csv` adlı CSV dosyalarındaki verileri kullanarak liman operasyonlarını simüle eder.

```bash
python main.py
