# Nama File   = deret aritmatika
# Nama        = Azka A. Maulana
# NIM         = 24060124140195
# Tanggal     = 30 September 2024 (tanggal mulai menulis di VsCode)
# Deskripsi   = membuat fungsi deret aritmatika

# DEFINISI DAN SPESIFIKASI
# thing : integer > 0 -> integer
#   {thing(n) adalah fungsi rekursif yang menghitung suku ke-n dari suatu deret aritmatika yang dimulai dari 3 dan setiap suku ditambah dengan nilai n}

# REALISASI
def thing(n) :
    if n == 1 :
        return 3
    else :
        return thing(n - 1) + n
    
# APLIKASI
print(thing(3))
print(thing(2))
print(thing(9))