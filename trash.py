import os
import datetime as dt

os.system("cls")


# CLASS UNTUK MENYIMPAN INFORMASI KOTA DAN JUGA JARAK ANTAR KOTA
class Peta:
    def __init__(self):
        self.kota = [] # MENYIMPAN NAMA KOTA
        self.cabang = {} # MENYIMPAN JARAK ANTAR KOTA

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

        path = [kotaTujuan]
        ruteSekarang = kotaTujuan
        jarak_tempuh = 0

        while ruteSekarang != kotaAwal:
            for tetangga, distance in self.cabang[ruteSekarang].items():
                if jarak[ruteSekarang] - distance == jarak[tetangga]:
                    path.append(tetangga)
                    jarak_tempuh += distance
                    ruteSekarang = tetangga
                    break
        path.reverse()
        return path, jarak_tempuh


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
                pil = input("Masukkan Id baru anda : ")
                self.password.add(pil)
                self.repeat()
            elif register == "n":
                print("Silahkan Masukkan Id Lain : ")
                self.repeat()
            else:
                return False
        elif self.check(id):
            return True


# CLASS UNTUK HISTORY PERJALANAN
class History:
    def __init__(self):
        self.historyPerjalanan = []

# FUNGSI UNTUK MENAMBAHKAN HISTORY SETIAP MELAKUKAN PERJALANAN
    def sethistoryPerjalanan(self, date, hour, before, after):
        item = [date, hour, before, after]
        return self.historyPerjalanan.append(item)

# FUNGSI UNTUK MENDAPATKAN HISTORY PERJALANAN YANG SUDAH DILAKUKAN
    def getHistoryPerjalanan(self):
        print("==============================================================")
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
        self.historyPerjalanan = History
        self.jarak = {}  # total jarak tempuh
        self.ruteTerdekat = {}  # kumpulan rute terdekat
        self.kotaAwal = ""
        self.kotaTujuan = ""
        self.peta = peta 
        self.jalan = True  # KONDISI PERULANGAN
        while self.jalan:
            self.RunCode()

# DISPLAY CODE
    def RunCode(self):
        print("==============================================================")
        print("              PROGRAM MENCARI RUTE TERPENDEK")
        print("==============================================================")
        print("Menu Mencari Lintasan Terpendek Area Sumatera")
        print("1. Cari Lintasan Perjalanan Terpendek")
        print("2. History Perjalanan Pencarian Lintasan Perjalanan Terpendek")
        print("3. Keluar")

        self.pil = int(input("Masukkan Fitur Yang Diinginkan (1 s.d. 3): "))
        if self.pil not in [1, 2, 3]:
            print("Hanya Boleh Memilih 1, 2, atau 3.\n")

        if self.pil == 1:
            print("\nLintasan Tersedia :")  # before
            for index, data in enumerate(self.peta.kota):
                print(f"{index+1}. {data}")
            self.kotaAwal = input("Masukkan Kota Anda: ")
            print("\nLintasan Tersedia :")  # after
            for data in self.peta.cabang:
                if data != self.kotaAwal:
                    print(f"{self.kotaAwal} -> {data} ")
            print()

            self.kotaTujuan = input("Masukkan peta Yang Ingin DiTuju : ")
            path = self.peta.FindRute(self.kotaAwal, self.kotaTujuan)
            print(
                "\nUntuk Mencapai Lokasi {} Anda Harus Melewati:".format(
                    self.kotaTujuan
                )
            )
            jarak_tempuh_total = 0
            for i in range(len(path) - 1):
                start = path[i]
                end = path[i + 1]
                jarak_tempuh = self.peta.cabang[start][end]
                jarak_tempuh_total += jarak_tempuh
                print("{} - {} (Jarak: {} Kilometer)".format(start, end, jarak_tempuh))
            print("Total Jarak: {} Kilometer".format(jarak_tempuh_total), "\n")

            pilihan = input("Apakah anda ingin Mencari Perjalanan Lagi? (y/n): ")
            if pilihan == "y":
                os.system("cls")
            else:
                self.jalan = False
            # PARAMETER HISTORY PERJALANAN
            date = dt.datetime.now().date()
            hour = str(dt.datetime.now().time())
            before = self.kotaAwal
            after = self.kotaTujuan
            self.historyPerjalanan().sethistoryPerjalanan(date, hour[:8], before, after)

        elif self.pil == 2:
            self.historyPerjalanan().getHistoryPerjalanan()
            back = input("Kembali ke awal? (y/n) : ")
            if back == "y":
                os.system("cls")
            elif back == "n":
                print("\nTerima Kasih Telah Menggunakan Program")
                return False
            else:
                print("\nInput Tidak Ada\nProgram Akan Dihentikan")
                print("Terima Kasih Telah Menggunakan Program")
                return False
        elif self.pil == 3:
            print("Terima Kasih Sudah Menggunakan Program Kami")
            self.jalan = False


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
user = input("Masukkan id anda : ")
Login().validation(user)
