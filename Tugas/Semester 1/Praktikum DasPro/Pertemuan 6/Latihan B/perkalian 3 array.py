# Nama File   = perkalian dgn 3 array
# Nama        = Azka A. Maulana
# NIM         = 24060124140195
# Tanggal     = 30 September 2024 (tanggal mulai menulis di VsCode)
# Deskripsi   = membuat fungsi perkalian dgn 3 array

# DEFINISI DAN SPESIFIKASI
# fungsi : integer > 0 -> integer
#   {fungsi(n) adalah fungsi rekursif yang menghitung hasil perkalian n dengan 3}

# REALISASI
def fungsi(n) :
    if n == 1 :
        return 3
    else :
        return fungsi(n - 1) + 3
    
# APLIKASI
print(fungsi(8))
print(fungsi(3))
print(fungsi(27))