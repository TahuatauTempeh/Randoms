# Nama File   = perpustakaan agung
# Nama        = Azka A. Maulana
# NIM         = 24060124140195
# Tanggal     = 23 September 2024 (tanggal mulai menulis di VsCode)
# Deskripsi   = mencari jawaban dari soal perpustakaan agung

# DEFINISI DAN SPESIFIKASI
# average : str -> int
#   [average (x) untuk mencari rata rata]
# jangkauan : 3 int -> int
#   [jangakauan (AS, AM, AIP) untuk mencari jangkauan]
# EstimateGreatLib : str, int {0 <= 24}, int, int, int {0 <= 24}, int {0 <= n}, int, int {0...10000}, int {1 <= n <= 100}
#   [EstimateGreatLib (D, X, Y, SS, SR, AS, AM, AIP, R) untuk hasil dari soal (aku nggak tau mau dikasih apa disini)]

# REALISASI
def average(x):
    if x == "senin":
        return (5000 + 6000 + 4000) / 3
    elif x == "selasa":
        return (7000 + 5000 + 2000) / 3
    elif x == "rabu":
        return (4500 + 3500 + 3000) / 3
    elif x == "kamis":
        return (2900 + 2100 + 2000) / 3
    elif x == "jumat":
        return (3000 + 3000 + 3000) / 3
    elif x == "sabtu":
        return (2000 + 2500 + 2300) / 3
    elif x == "minggu":
        return (1100 + 900 + 1000) / 3


def jangkauan(AS, AM, AIP):
    return max(AS, AM, AIP) - min(AS, AM, AIP)


def EstimateGreatLib(D, X, Y, SS, SR, AS, AM, AIP, R):
        if SR <= X < Y <= SS:
            return (Y - X) * jangkauan(AS, AM, AIP) / average(D)
        elif (X >= SS and Y > SS):
            return (Y - X) * jangkauan(AS, AM, AIP) * (R / 100) / average(D)
        elif (X < SR and Y <= SR):
            return ((Y - X) * (max(AS, AM, AIP) - min(AS, AM, AIP)) / average(D) * R / 100)
        elif X >= SR and Y > SS:
            return ((SS - X) * jangkauan(AS, AM, AIP) / average(D) + (Y - SS) * jangkauan(AS, AM, AIP) * (R / 100) / average(D)) / 2
        elif X < SR and (Y > SR and Y <= SS):
            return ((SR - X) * jangkauan(AS, AM, AIP) * (R / 100) / average(D) + (Y - SR) * jangkauan(AS, AM, AIP) / average(D) )/ 2
        elif X < SR < SS < Y:
            return ((SR - X) * jangkauan(AS, AM, AIP) * (R / 100) / average(D) + (SS - SR) * jangkauan(AS, AM, AIP) / average(D) + (Y - SS) * jangkauan(AS, AM, AIP) * (R / 100) / average(D)) / 3


print(round(eval(input()), 5))

# APLIKASI
EstimateGreatLib("senin", 12, 17, 18, 9, 6000, 5000, 4500, 50)
EstimateGreatLib("selasa", 8, 16, 20, 12, 7000, 5000, 2000, 75)

# ADDITIONAL RANDOM NOTES
# X = jam mulai buka / mulai bekerja
# Y = jam tutup
# D = hari tertentu
# SR = waktu sunrise
# SS = waktu sunset
# AS = ahli statistika
# AM = ahli matematika
# AIP = ahli ilmu perpustakaan
# R = persentase