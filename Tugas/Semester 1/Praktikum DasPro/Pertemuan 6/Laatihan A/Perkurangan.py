# Nama File   = aritmatika perkurangan
# Nama        = Azka A. Maulana
# NIM         = 24060124140195
# Tanggal     = 30 September 2024 (tanggal mulai menulis di VsCode)
# Deskripsi   = fungsi rekuren aritmatika pengurangan

# DEFINISI DAN SPESIFIKASI
# min : 2 integer > 0 -> integer > 0
#   {min (x,y) adalah fungsi untuk mengurangkan variabel x dengan y untuk infinite hingga y = 0, dimana nanti akan menyebut variabel x}

# REALISASI
def min(x,y) :
    if y == 0 :
        return x
    else :
        return min(x,y - 1) - 1

# APLIKASI
print(min(3,4))
print(min(1,9))
print(min(8,1))