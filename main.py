import csv
import heapq


class Tir:
    def __init__(self, plaka, ulke, yirmi_ton, otuz_ton, maliyet):
        self.plaka = plaka
        self.ulke = ulke
        self.yirmi_ton = yirmi_ton
        self.otuz_ton = otuz_ton
        self.yuk = yirmi_ton * 20 + otuz_ton * 30
        self.maliyet = maliyet

    def __lt__(self, other):
        return self.plaka < other.plaka

class Gemi:
    def __init__(self, numara, kapasite, gidecek_ulke):
        self.numara = numara
        self.kapasite = kapasite
        self.gidecek_ulke = gidecek_ulke
        self.yuk = 0
        self.yukleme = False

    def __lt__(self, other):
        return self.numara < other.numara

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

    def tir_okuma(self):
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

    def gemi_okuma(self):
        with open("gemiler.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                numara = int(row["gemi_adi"])
                kapasite = int(row["kapasite"])
                gidecek_ulke = row["gidecek_ulke"]
                gemi = Gemi(numara, kapasite, gidecek_ulke)
                heapq.heappush(self.gemi_kuyrugu, gemi)
    def tir_indirme(self):
        while self.tir_kuyrugu:
            tir = heapq.heappop(self.tir_kuyrugu)
            print(f"{self.t}. dakikada {tir.plaka} plakalı TIR yükünü indirdi.")
            self.istif_alani_1.append(tir)
            self.istif_alani_1_yuk += tir.yuk
            if self.istif_alani_1_yuk >= self.istif_alani_1_kapasite:
                print(f"1 numaralı istif alanı dolu. ({self.istif_alani_1_yuk} ton)")
            self.t += 1

    def gemi_yukleme(self):
        while self.gemi_kuyrugu:
            gemi = heapq.heappop(self.gemi_kuyrugu)
            print(f"{self.t}. dakikada {gemi.numara} numaralı gemi yükleme için hazır.")
            while self.istif_alani_1 or self.istif_alani_2:
                if self.istif_alani_1:
                    tir = self.istif_alani_1.pop()
                    self.istif_alani_1_yuk -= tir.yuk
                    if self.istif_alani_1_yuk == 0:
                        print(f"1 numaralı istif alanı boş. ({self.istif_alani_1_yuk} ton)")
                    if tir.ulke == gemi.gidecek_ulke:
                        gemi.yuk += tir.yuk
                        gemi.yukleme = True
                        print(
                            f"{self.t}. dakikada {gemi.numara} numaralı gemiye {tir.plaka} plakalı TIRın yükü yüklendi. ({tir.ulke}) ({tir.maliyet}₺)")
                    else:
                        self.istif_alani_2.append(tir)
                        self.istif_alani_2_yuk += tir.yuk
                        print(
                            f"{self.t}. dakikada {tir.plaka} plakalı TIRın yükü 1 numaralı istif alanından 2 numaralı istif alanına taşındı. ({tir.ulke})")
                else:
                    tir = self.istif_alani_2.pop()
                    self.istif_alani_2_yuk -= tir.yuk
                    if self.istif_alani_2_yuk == 0:
                        print(f"2 numaralı istif alanı boş. ({self.istif_alani_2_yuk} ton)")
                    if tir.ulke == gemi.gidecek_ulke:
                        gemi.yuk += tir.yuk
                        gemi.yukleme = True
                        print(
                            f"{self.t}. dakikada {gemi.numara} numaralı gemiye {tir.plaka} plakalı TIRın yükü yüklendi. ({tir.ulke})")
                    else:
                        self.istif_alani_1.append(tir)
                        self.istif_alani_1_yuk += tir.yuk
                        print(
                            f"{self.t}. dakikada {tir.plaka} plakalı TIRın yükü 2 numaralı istif alanından 1 numaralı istif alanına taşındı. ({tir.ulke})")
                if gemi.yuk >= gemi.kapasite * 0.95:
                    print(f"{self.t}. dakikada {gemi.numara} numaralı gemi limanı terk etti. ({gemi.yuk} ton)")
                    break
            if not gemi.yukleme:
                print(f"{self.t}. dakikada {gemi.numara} numaralı gemi limanı terk etti. ({gemi.yuk} ton)")
            self.vinc += 1
            if self.vinc == self.vinc_limit:
                break


if __name__ == "__main__":
    liman = Liman()
    liman.tir_okuma()
    liman.gemi_okuma()
    liman.tir_indirme()
    liman.gemi_yukleme()