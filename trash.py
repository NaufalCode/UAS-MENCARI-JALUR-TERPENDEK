import os
import datetime as dt

os.system("cls")


# CLASS UNTUK MENYIMPAN INFORMASI KOTA DAN JUGA JARAK ANTAR KOTA
class Peta:
    def __init__(self):
        self.kota = []  # MENYIMPAN NAMA KOTA
        self.cabang = {}  # MENYIMPAN JARAK ANTAR KOTA

    # FUNGSI UNTUK MENAMBAHKAN KOTA (HANYA NAMA KOTA SAJA)
    def addKota(self, value):
        self.kota.append(value)
        self.cabang[value] = {}

    # FUNGSI UNTUK MENYAMBUNGKAN ANTAR KOTA
    def addCabang(self, lokasiAwal, tujuan, jarak):
        self.cabang[lokasiAwal][tujuan] = jarak
        self.cabang[tujuan][tujuan] = jarak

    # FUNGSI UNTUK MENCARI RUTE TERDEKAT DARI LOKASI AWAL KE TUJUAN
    def FindRute(self, kotaAwal, kotaTujuan):
        jarak = {vertex: float("inf") for vertex in self.cabang}
        jarak[kotaAwal] = 0
        dikunjungi = set()

        while len(dikunjungi) < len(self.cabang):
            ruteSekarang = None
            for rute in self.cabang:
                if rute not in dikunjungi and (
                    ruteSekarang is None or jarak[rute] < jarak[ruteSekarang]
                ):
                    ruteSekarang = rute

            dikunjungi.add(ruteSekarang)

            for tetangga, distance in self.cabang[ruteSekarang].items():
                if jarak[ruteSekarang] + distance < jarak[tetangga]:
                    jarak[tetangga] = jarak[ruteSekarang] + distance

        rute = [kotaTujuan]
        ruteSekarang = kotaTujuan
        jarakTempuh = 0

        while ruteSekarang != kotaAwal:
            for tetangga, distance in self.cabang[ruteSekarang].items():
                if jarak[ruteSekarang] - distance == jarak[tetangga]:
                    rute.append(tetangga)
                    jarakTempuh += distance
                    ruteSekarang = tetangga
                    break
        rute.reverse()
        return rute, jarakTempuh


class Login:
    # HANYA BERISI LOGIN FLOW
    def __init__(self):
        self.password = set()
        self.count = 0

    # FUNGSI REKURSIF YANG TERUS BERULANGAN SAMPAI 3 KALI APABILA ID SALAH
    def repeat(self):
        self.count += 1
        if self.count < 6:
            user = input("Masukkan Id Anda : ")
            if self.validation(user):
                print("Id tersedia\n")
                Main(Data)
            else:
                self.validation(user)
        elif self.count >= 6:
            print("Anda Salah Memasukkan Id Sebanyak 3 Kali\nProgram Akan Berhenti ")

    def check(self, id):
        return id in self.password

    def validation(self, id):
        if not self.check(id):
            print("Id tidak ada silahkan daftar terlebih dahulu")
            print()
            register = input("Apakah anda ingin mendaftar ? (y/n) : ")
            if register == "y":
                self.register()
                self.repeat()
            elif register == "n":
                print("Silahkan Masukkan Id Lain : ")
                self.repeat()
            else:
                return False
        elif self.check(id):
            return True

    def register(self):
        id = input("\nMasukkan Id Baru Anda : ")
        if id in self.password:
            print("Id sudah terdaftar")
            id = input("\nMasukkan Id Baru Anda : ")
            self.password.add(id)
        else:
            self.password.add(id)
        self.repeat()


# CLASS UNTUK HISTORY PERJALANAN
class History:
    def __init__(self):
        self.historyPerjalanan = []

    # FUNGSI UNTUK MENAMBAHKAN HISTORY SETIAP MELAKUKAN PERJALANAN
    def setHistoryPerjalanan(self, date, hour, before, after):
        item = [date, hour, before, after]
        return self.historyPerjalanan.append(item)

    # FUNGSI UNTUK MENDAPATKAN HISTORY PERJALANAN YANG SUDAH DILAKUKAN
    def getHistoryPerjalanan(self):
        print("\n==============================================================")
        print("                    History Perjalanan                        ")
        print("==============================================================")
        if self.historyPerjalanan == []:
            print("Belum Ada Data Yang Ter Catat")
        else:
            for idx, data in enumerate(self.historyPerjalanan, start=1):
                print(f" {idx}. {data[0]}\t\t| {data[1]} ({data[2]} ke {data[3]})")
        print()


# class ini berfungsi untuk mengeluarkan output dan juga flow program
class Main:
    def __init__(self, peta):
        self.infinity = float("infinity")
        self.historyPerjalanan = History()
        self.jarak = {}  # total jarak tempuh
        self.ruteTerdekat = {}  # kumpulan rute terdekat
        self.kotaAwal = ""
        self.kotaTujuan = ""
        self.peta = peta
        self.jalan = True  # KONDISI PERULANGAN
        while self.jalan:
            self.RunCodeHeader()

    # DISPLAY CODE
    def RunCodeHeader(self):
        print("==============================================================")
        print("              PROGRAM MENCARI RUTE TERPENDEK")
        print("==============================================================")
        print("Menu Mencari Lintasan Terpendek Area Sumatera")
        print("1. Cari Lintasan Perjalanan Terpendek")
        print("2. History Perjalanan Pencarian Lintasan Perjalanan Terpendek")
        print("3. Keluar")
        self.pil = int(input("Masukkan Fitur Yang Diinginkan (1 s.d. 3): "))
        self.Menu()

    def Menu(self):
        try:
            if self.pil not in [1, 2, 3]:
                print("Hanya Boleh Memilih 1, 2, atau 3.\n")

            if self.pil == 1:
                print("\nLintasan Yang Tersedia :")  # before
                for index, data in enumerate(self.peta.kota):
                    print(f"{index+1}. {data}")
                self.kotaAwal = input("Masukkan Lokasi Awal Anda : ")
                print("\nLintasan Yang Tersedia :")  # after
                for data in self.peta.cabang:
                    if data != self.kotaAwal:
                        print(f"{self.kotaAwal} -> {data} ")
                print()

                self.kotaTujuan = input("Masukkan Kota Tujuan Anda : ")
                rute, jarak = self.peta.FindRute(self.kotaAwal, self.kotaTujuan)
                print(
                    "\nUntuk Mencapai Lokasi {} Anda Harus Melewati:".format(
                        self.kotaTujuan
                    )
                )
                jarakTempuhTotal = 0
                for i in range(len(rute) - 1):
                    start = rute[i]
                    end = rute[i + 1]
                    jarakTempuh = self.peta.cabang[start][end]
                    jarakTempuhTotal += jarakTempuh
                    print(
                        "{} - {} (Jarak: {} Kilometer)".format(start, end, jarakTempuh)
                    )
                print("Total Jarak: {} Kilometer".format(jarakTempuhTotal), "\n")

                pilihan = input("Apakah Anda Ingin Mencari Perjalanan Lagi? (y/n): ")
                if pilihan == "y":
                    os.system("cls")
                    self.Menu()
                else:
                    os.system("cls")
                # PARAMETER HISTORY PERJALANAN
                date = dt.datetime.now().date()
                hour = str(dt.datetime.now().time())
                before = self.kotaAwal
                after = self.kotaTujuan
                self.historyPerjalanan.setHistoryPerjalanan(
                    date, hour[:8], before, after
                )

            elif self.pil == 2:
                self.historyPerjalanan.getHistoryPerjalanan()
                back = ""
                while back != "y":
                    back = input("Kembali ke awal? (y/n) : ")
                    if back == "y":
                        os.system("cls")
                    elif back == "n":
                        print("Waiting...\n")
                    else:
                        print("Input Tidak Ada\nSilahkan Masukkan (y / n)\n")
            elif self.pil == 3:
                print("Terima Kasih Sudah Menggunakan Program Kami")
                self.jalan = False
        except TypeError:
            print("\nInput Hanya Boleh Berupa Angka : ")


# INISIALISASI
Data = Peta()
# KOTA
Data.addKota("Medan")
Data.addKota("Palembang")
Data.addKota("Padang")
Data.addKota("Pekanbaru")
Data.addKota("Bandar Lampung")
Data.addKota("Jambi")
Data.addKota("Bengkulu")
Data.addKota("Bukit Tinggi")
Data.addKota("Tanjung Pinang")
Data.addKota("Dumai")
# HUBUNGAN ANTAR KOTA (GRAPH)
Data.addCabang("Medan", "Pekanbaru", 400)
Data.addCabang("Medan", "Padang", 600)
Data.addCabang("Medan", "Palembang", 500)
Data.addCabang("Palembang", "Medan", 500)
Data.addCabang("Palembang", "Padang", 400)
Data.addCabang("Palembang", "Pekanbaru", 300)
Data.addCabang("Padang", "Medan", 600)
Data.addCabang("Padang", "Palembang", 400)
Data.addCabang("Padang", "Pekanbaru", 200)
Data.addCabang("Padang", "Bandar Lampung", 700)
Data.addCabang("Pekanbaru", "Padang", 200)
Data.addCabang("Pekanbaru", "Medan", 400)
Data.addCabang("Pekanbaru", "Palembang", 300)
Data.addCabang("Bandar Lampung", "Padang", 700)
Data.addCabang("Bandar Lampung", "Jambi", 400)
Data.addCabang("Jambi", "Bengkulu", 200)
Data.addCabang("Jambi", "Bandar Lampung", 400)
Data.addCabang("Bengkulu", "Jambi", 200)
Data.addCabang("Bengkulu", "Bukit Tinggi", 300)
Data.addCabang("Bukit Tinggi", "Bengkulu", 300)
Data.addCabang("Bukit Tinggi", "Tanjung Pinang", 500)
Data.addCabang("Tanjung Pinang", "Bukit Tinggi", 500)
Data.addCabang("Tanjung Pinang", "Dumai", 400)
Data.addCabang("Dumai", "Tanjung Pinang", 400)


# MENJALANKAN CODE
print("==============================================================")
print("                        LOGIN PAGE                            ")
print("==============================================================")
print("1. Login")
print("2. Register")
form = int(input("Masukkan Pilihan Anda (1 - 2) : "))
run = True
while run:
    try:
        if form == 1:
            user = input("Masukkan Id Anda : ")
            Login().validation(user)
        elif form == 2:
            Login().register()
        else:
            print("Hanya Boleh Memasukkan Angka 1 Atau 2")
        if Main(Data).jalan == False:
            break
    except TypeError:
        print('Inputan Hanya Boleh Berupa Angka 1 Atau 2')
