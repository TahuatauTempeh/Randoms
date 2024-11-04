# Nama File   = belajar tenang
# Nama        = Azka A. Maulana
# NIM         = 24060124140195
# Tanggal     = 22 September 2024 (tanggal mulai menulis di VsCode)
# Deskripsi   = belajar tenang

# DEFINISI DAN SPESIFIKASI
# BelajarTenang : 2 int -> string
#   [BelajarTenang (dB,m) adlaah fungsi yang menyatakan berapa meter yang Shibusawa minimal harus tempuh atau bensin Shibusawa tidak cukup]


# REALISASI
def BelajarTenang (dB,m) :
    bt = 15 * 10**((dB - 40)/20)
    if bt < m :
        return f"{round (bt, 3)} meter"
    else :
        return "Isi bensin dulu, bang"
    
print(eval(input()))

# APLIKASI
BelajarTenang(102, 20000)
BelajarTenang(100, 1300)