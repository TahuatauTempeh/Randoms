# Nama File   = deret bilangan integer
# Nama        = Azka A. Maulana
# NIM         = 24060124140195
# Tanggal     = 30 September 2024 (tanggal mulai menulis di VsCode)
# Deskripsi   = membuat fungsi deret bilangan integer

# DEFINISI DAN SPESIFIKASI
# bilangan : integer > 0 -> integer
#   {bilangan(n) adalah fungsi rekursif yang menghitung jumlah bilangan dari 1 hingga n}


# REALISASI
def bilangan(n) :
    if n == 1 :
        return 1
    else :
        return bilangan(n - 1) + n
    
# APLIKASI
print(bilangan(3))
print(bilangan(4))
print(bilangan(110))