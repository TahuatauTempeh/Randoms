# Nama File   = deret geometri
# Nama        = Azka A. Maulana
# NIM         = 24060124140195
# Tanggal     = 30 September 2024 (tanggal mulai menulis di VsCode)
# Deskripsi   = membuat fungsi deret geometri

# DEFINISI DAN SPESIFIKASI
# geometri : integer > 0 -> integer
#   {geometri(n) adalah fungsi rekursif yang menghitung nilai dari deret geometri dengan rasio 3 pada suku ke-n}


# REALISASI
def geometri(n) :
    if n == 1 :
        return 1
    else :
        return geometri(n - 1) * 3
    
# APLIKASI
print(geometri(4))
print(geometri(7))
print(geometri(5))