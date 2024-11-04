# Nama File   = sequence bil penyebut
# Nama        = Azka A. Maulana
# NIM         = 24060124140195
# Tanggal     = 24 September 2024 (tanggal mulai menulis di VsCode)
# Deskripsi   = mencari jawaban dari soal sequence bilangan penyebut

# DEFINISI DAN SPESIFIKASI
# denumeratirSeq : int -> str
#   [denumeratorSeq (x) untuk menentukan apakah urutan angka x terulang tersebut sesuai dengan desimal hasil pembagian 1 dengan sebuah bilangan bulat]

# REALISASI
def denumeratorSeq(x):
    if (10 ** len(x)-1) % int(x) == 0:
        return f"Ada: {(10**len(x)-1) // int(x)}"
    else :
        return f"Tidak ada"

print(eval(input()))

# APLIKASI
denumeratorSeq('3')
denumeratorSeq('166')