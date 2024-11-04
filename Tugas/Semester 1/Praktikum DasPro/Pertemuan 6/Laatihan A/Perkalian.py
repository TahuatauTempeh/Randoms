# Nama File   = aritmatika perkalian
# Nama        = Azka A. Maulana
# NIM         = 24060124140195
# Tanggal     = 30 September 2024 (tanggal mulai menulis di VsCode)
# Deskripsi   = fungsi rekuren aritmatika perkalian

# DEFINISI DAN SPESIFIKASI
# multi : 2 integer > 0 -> integer > 0
#   {multi(x, y) adalah fungsi untuk melakukan perkalian rekursif antara x dan y dengan menambahkan x secara rekursif sebanyak y kali}

# REALISASI
def multi(x,y) :
    if y == 0 :
        return x
    else :
        return (multi(x,y - 1)) + x
    
# APLIKASI
print(multi(2,7))
print(multi(90,7))
print(multi(5,3))