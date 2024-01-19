import os
import datetime as dt

os.system("cls")

# SET
class Login:
    def __init__(self,name):
        self.name = name
        self.set = set()
        self.validation(self.name)
    def repeat(self):
        user = input('Masukkan Id Anda : ')
        self.validation(user)
    def check(self):
        return self.name in self.set
    def validation(self, name):
        if (not self.check()):
            print('Id tidak ada silahkan daftar terlebih dahulu')
            print()
            pil = input('Masukkan Id baru anda : ')
            print('Id berhasil dibuat\n')
            self.set.add(pil)
            self.repeat()
        if (self.check()):
            print('Id Tersedia')
            print()
            return True

# QUEUE
# class InformasiKota:
#     def __init__(self):
class Map:
    def __init__(self):
        self.node = set()
        self.edge = {}
    def addNode(self, value):
        self.node.add(value)
        self.edge[value] = []
    def addEdge(self,fromNode, toNode, value):
        self.edge[fromNode].append((toNode,value))
        self.edge[toNode].append((fromNode,value))

class MencariLintasanTerdekat:
    def __init__(self, lokasi):
        self.infinity = float("infinity")
        self.history = []
        self.jarak = {}
        self.kota = {}
        self.kota_pertama = ""
        self.kota_tujuan = ""
        self.lokasi = lokasi
        self.jalan = True
        while jalan:
            self.RunCode()

    def RunCode(self):
        print("Menu Mencari Lintasan Terpendek Area Sumatera")
        print("1. Cari Lintasan Perjalanan Terpendek")
        print("2. History Pencarian Lintasan Perjalanan Terpendek")
        print("3. Keluar")

        self.pil = int(input("Masukkan Fitur Yang Diinginkan : "))

        if self.pil not in [1, 2, 3]:
            print("Hanya Boleh Memilih 1, 2, atau 3.")
            self.jalan = False

        if self.pil == 1:
            print()
            print("Lintasan Tersedia :")

            for index, data in enumerate(self.lokasi):
                print(f"{index+1}. {data}")

            self.kota_pertama = input("Masukkan Kota Anda: ")
            self.Setup()

            print()
            print("Lintasan Tersedia :")

            for index, data in enumerate(self.lokasi):
                if (data==self.kota_pertama):
                    if index==0:
                        index+=1
                    else:
                        index-=1
                elif data != self.kota_pertama:
                    print(f"{index+1}. {data} ")
            print()

            self.kota_tujuan = input("Masukkan Lokasi Yang Ingin DiTuju : ")

            self.GraphSearch()

            if self.jarak[self.kota_tujuan] < self.infinity:
                # MEMASUKKAN SETIAP KOTA AWAL DAN TUJUAN KE DALAM HISTORY
                alur_terpendek = self.filterJalurTercepat()
                print(
                    f"Menghitung jarak terpendek dari {self.kota_pertama} ke {self.kota_tujuan}"
                )
                print()
                print(
                    "=============================================================================="
                )
                print(
                    f"Jarak tempuh terpendek untuk dari {self.kota_pertama} ke {self.kota_tujuan} adalah: {self.jarak[self.kota_tujuan]} km "
                )
                print(f"Alur terpendek untuk anda adalah {alur_terpendek}")
                print(
                    "=============================================================================="
                )
                date = dt.datetime.now().date()
                hour = str(dt.datetime.now().time())
                before = self.kota_pertama
                after = self.kota_tujuan
                self.setHistory(date, hour[:8], before, after)
            else:
                print("Maaf alur yang anda cari tidak ditemukan")
                self.jalan = False

        elif self.pil == 2:
            self.getHistory()
        elif self.pil == 3:
            self.jalan = False
        else:
            print()
            print("Masukkan Perintah Yang Sudah Tertera")

    def Setup(self):
        for node in self.lokasi:
            self.jarak[node] = self.infinity
            self.kota[node] = {}
        self.jarak[self.kota_pertama] = 0

    def MencariNodeTerdekat(self, not_check):
        jarakTerpendek = self.infinity
        nodeTerendah = ""
        for node in not_check:
            if self.jarak[node] <= jarakTerpendek:
                jarakTerpendek = self.jarak[node]
                nodeTerendah = node
        return nodeTerendah

    def GraphSearch(self):
        not_check = list(self.jarak.keys())
        node = self.MencariNodeTerdekat(not_check)
        while not_check:
            dist = self.jarak[node]
            child_dist = self.lokasi[node]
            for c in child_dist:
                if self.jarak[c] > dist + child_dist[c]:
                    self.jarak[c] = dist + child_dist[c]
                    self.kota[c] = node
            not_check.pop(not_check.index(node))
            node = self.MencariNodeTerdekat(not_check)

    def filterJalurTercepat(self):
        alur = [self.kota_tujuan]
        i = 0
        while self.kota_pertama not in alur:
            alur.append(self.kota[alur[i]])
            i += 1
        return alur[::-1]

    def setHistory(self, date, hour, before, after):
        item = [date, hour, before, after]
        return self.history.append(item)

    def getHistory(self):
        print()
        print("================================================")
        print("                    HISTORY")
        print("================================================")
        for idx, data in enumerate(self.history, start=1):
            print(f"| {idx+1}. {data[0]} | {data[1]} ({data[2]} ke {data[3]}) |")
        print()

# INISIALISASI
Data = Map()
# KOTA
Data.addNode('Medan')
Data.addNode('Palembang')
Data.addNode('Padang')
Data.addNode('Pekanbaru')
Data.addNode('Jambi')
Data.addNode('Pekanbaru')
Data.addNode('Bandar Lampung')
Data.addNode('Jambi')
Data.addNode('Bengkulu')
Data.addNode('Bukit Tinggi')
Data.addNode('Tanjung Pinang')
Data.addNode('Dumai')
# HUBUNGAN ANTAR KOTA
Data.addEdge('Medan', 'Pekanbaru', 400)
Data.addEdge('Medan', 'Padang', 600)
Data.addEdge('Medan', 'Palembang', 500)
Data.addEdge('Palembang', 'Medan', 500)
Data.addEdge('Palembang', 'Padang', 400)
Data.addEdge('Palembang', 'Pekanbaru', 300)
Data.addEdge('Padang', 'Medan', 600)
Data.addEdge('Padang', 'Palembang', 400)
Data.addEdge('Padang', 'Pekanbaru', 200)
Data.addEdge('Padang', 'Bandar Lampung', 700)
Data.addEdge('Pekanbaru', 'Padang', 200)
Data.addEdge('Pekanbaru', 'Medan', 400)
Data.addEdge('Pekanbaru', 'Palembang', 300)
Data.addEdge('Bandar Lampung', 'Padang', 700)
Data.addEdge('Bandar Lampung', 'Jambi', 400)
Data.addEdge('Jambi', 'Bengkulu', 200)
Data.addEdge('Jambi', 'Bandar Lampung', 400)
Data.addEdge('Bengkulu', 'Jambi', 200)
Data.addEdge('Bengkulu', 'Bukit Tinggi', 300)
Data.addEdge('Bukit Tinggi', 'Bengkulu', 300)
Data.addEdge('Bukit Tinggi', 'Tanjung Pinang', 500)
Data.addEdge('Tanjung Pinang', 'Bukit Tinggi', 500)
Data.addEdge('Tanjung Pinang', 'Dumai', 400)
Data.addEdge('Dumai', 'Tanjung Pinang', 400)

# MENJALANKAN CODE
jalan = True
user = input('Masukkan id anda : ')
valid = Login(user)
if (valid):
    MencariLintasanTerdekat(Data.node)
else:
    valid = Login(user)
