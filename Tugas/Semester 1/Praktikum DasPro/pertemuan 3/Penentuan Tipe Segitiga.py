# Nama File   = Penentuan Tipe Segitiga
# Nama        = Azka A. Maulana
# Tanggal     = 11 September 2024
# Deskripsi   = Apakah segitiga itu sama sisi, sama kaki, atau sembarang

# DEFINISI DAN SPESIFIKASI
# tipe_segitiga : 3 real -> string
#   [tipe_segitiga (a,b,c) adalah fungsi untuk menentukan tipe segitiga]

# REALISASI
def tipe_segitiga (a,b,c) :
    if a == b == c:
        print("Segitiga sama sisi")
    elif a == b or a == c or b == c:
        print("Segitiga sama kaki")
    else:
        print("Segitiga sembarang")

# APLIKASI

tipe_segitiga (1,2,3)
tipe_segitiga (1,2,1)
tipe_segitiga (2,2,2)