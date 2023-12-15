import csv
import heapq


# csv modülü ile kodumuza csv dosylarını okuyabilme yeteneği kazandırdık.
# heapq modülü ile küçükten büyüğe sıralı bir kuyruk yapısı kullanarak tır ve gemileri belirli bir sırada işledik.


# Tır nesnesin özelliklerini tanımladık.
class Tir:
    def __init__(self, plaka, ulke, yirmi_ton, otuz_ton, maliyet):
        self.plaka = plaka
        self.ulke = ulke
        self.yirmi_ton = yirmi_ton
        self.otuz_ton = otuz_ton
        self.yuk = yirmi_ton * 20 + otuz_ton * 30
        self.maliyet = maliyet

    # Gelen tırları plakalarına göre sıraya koymak için less than fonksiyonunu kullandık.
    def __lt__(self, other):
        return self.plaka < other.plaka


# Oluşturduğunuz gemi nesnesinin özelliklerini tanımladık.
class Gemi:
    def __init__(self, numara, kapasite, hedef_ulke):
        self.numara = numara
        self.kapasite = kapasite
        self.hedef_ulke = hedef_ulke
        self.yuk = 0
        self.yukleme = False

    # Gelen gemileri numaralarına göre sıraya koymak için less than fonksiyonunu kullandık.
    def __lt__(self, other):
        return self.numara < other.numara


# Liman sınıfının özelliklerini tanımladık.
class Liman:
    def __init__(self):
        self.tir_kuyrugu = []
        self.gemi_kuyrugu = []
        self.istif_alani_1 = []
        self.istif_alani_2 = []
        self.istif_alani_1_kapasite = 750
        self.istif_alani_2_kapasite = 750
        self.istif_alani_1_yuk = 0
        self.istif_alani_2_yuk = 0
        self.vinc = 0
        self.vinc_limit = 20
        self.t = 0

    # olaylar.csv dosyasından tır bilgilerini alarak kuyruğa ekledik
    def tir_bilgisi_okuma(self):
        with open("olaylar.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                plaka = row["tir_plakasi"]
                ulke = row["ulke"]
                yirmi_ton = int(row["20_ton_adet"])
                otuz_ton = int(row["30_ton_adet"])
                maliyet = float(row.get("maliyet", 0))
                tir = Tir(plaka, ulke, yirmi_ton, otuz_ton, maliyet)
                heapq.heappush(self.tir_kuyrugu, tir)

    # gemiler.csv dosyasından tır bilgilerini alarak kuyruğa ekledik
    def gemi_bilgisi_okuma(self):
        with open("gemiler.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                numara = int(row["gemi_adi"])
                kapasite = int(row["kapasite"])
                hedef_ulke = row["gidecek_ulke"]
                gemi = Gemi(numara, kapasite, hedef_ulke)
                heapq.heappush(self.gemi_kuyrugu, gemi)

    # Kuyruğa eklenmiş olan tırları sırasıyla istifl alanına yerleştirdik.
    def tir_yuk_indirme(self):
        while self.tir_kuyrugu:
            tir = heapq.heappop(self.tir_kuyrugu)
            print(f"{self.t}. dakikada {tir.plaka} plakalı tır yükünü indirdi.")
            self.istif_alani_1.append(tir)
            self.istif_alani_1_yuk += tir.yuk
            if self.istif_alani_1_yuk >= self.istif_alani_1_kapasite:
                print(f"1 numaralı istif alanı dolu. ({self.istif_alani_1_yuk} ton)")
            self.t += 1

    # Kuyruğa eklenmiş olan gemilere tırları yükledik ve limandan ayrılan gemileri takip ettik
    def gemi_yuk_yukleme(self):
        while self.gemi_kuyrugu:
            # Gemi kuyruğundan en küçük gemi numarasına sahip gemiyi çıkar
            gemi = heapq.heappop(self.gemi_kuyrugu)
            print(f"{self.t}. dakikada {gemi.numara} numaralı gemi yükleme için hazır.")

            while self.istif_alani_1 or self.istif_alani_2:
                # 1 numaralı istif alanından tır çıkar
                if self.istif_alani_1:
                    tir = self.istif_alani_1.pop()
                    self.istif_alani_1_yuk -= tir.yuk
                    if self.istif_alani_1_yuk == 0:
                        print(f"1 numaralı istif alanı boş. ({self.istif_alani_1_yuk} ton)")

                    # Eğer tırın ülkesi geminin hedef ülkesi ile aynıysa yükleme yap
                    if tir.ulke == gemi.hedef_ulke:
                        gemi.yuk += tir.yuk
                        gemi.yukleme = True
                        print(
                            f"{self.t}. dakikada {gemi.numara} numaralı gemiye {tir.plaka} plakalı tırın yükü yüklendi. ({tir.ulke}) ({tir.maliyet} ₺)")
                    else:
                        # Aynı değilse tırı 2 numaralı istif alanına taşı
                        self.istif_alani_2.append(tir)
                        self.istif_alani_2_yuk += tir.yuk
                        print(
                            f"{self.t}. dakikada {tir.plaka} plakalı tırın yükü 1 numaralı istif alanından 2 numaralı istif alanına taşındı. ({tir.ulke})")
                else:
                    # 2 numaralı istif alanından tır çıkar
                    tir = self.istif_alani_2.pop()
                    self.istif_alani_2_yuk -= tir.yuk
                    if self.istif_alani_2_yuk == 0:
                        print(f"2 numaralı istif alanı boş. ({self.istif_alani_2_yuk} ton)")

                    # Eğer tırın ülkesi geminin hedef ülkesi ile aynıysa yükleme yap
                    if tir.ulke == gemi.hedef_ulke:
                        gemi.yuk += tir.yuk
                        gemi.yukleme = True
                        print(
                            f"{self.t}. dakikada {gemi.numara} numaralı gemiye {tir.plaka} plakalı tırın yükü yüklendi. ({tir.ulke})")
                    else:
                        # Aynı değilse tırın 1 numaralı istif alanına taşı
                        self.istif_alani_1.append(tir)
                        self.istif_alani_1_yuk += tir.yuk
                        print(
                            f"{self.t}. dakikada {tir.plaka} plakalı tırın yükü 2 numaralı istif alanından 1 numaralı istif alanına taşındı. ({tir.ulke})")

                # Gemi yük kapasitesinin %95'ini aştıysa limanı terk eder
                if gemi.yuk >= gemi.kapasite * 0.95:
                    print(f"{self.t}. dakikada {gemi.numara} numaralı gemi limanı terk etti. ({gemi.yuk} ton)")
                    break

            if not gemi.yukleme:
                print(f"{self.t}. dakikada {gemi.numara} numaralı gemi limanı terk etti. ({gemi.yuk} ton)")

            # Vincin durumunu güncelle
            self.vinc += 1
            if self.vinc == self.vinc_limit:
                break


def main():
    liman = Liman()
    liman.tir_bilgisi_okuma()
    liman.gemi_bilgisi_okuma()
    liman.tir_yuk_indirme()
    liman.gemi_yuk_yukleme()


if __name__ == "__main__":
    main()
