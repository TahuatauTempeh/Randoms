# Nama File   = menghitung deret 
# Nama        = Azka A. Maulana
# NIM         = 24060124140195
# Tanggal     = 30 September 2024 (tanggal mulai menulis di VsCode)
# Deskripsi   = membuat fungsi menghitung deret

# DEFINISI DAN SPESIFIKASI
# deret : integer > 0 -> integer
#   {deret(n) adalah fungsi rekursif yang menghitung jumlah dari kuadrat bilangan 1 sampai n}

# REALISASI
def deret(n) :
    if n == 1 :
        return 1
    else :
        return deret(n - 1) + (n ** 2)
    
# APLIKASI
print(deret(9))
print(deret(3))
print(deret(100))