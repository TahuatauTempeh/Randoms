# Nama File   = gradien magis
# Nama        = Azka A. Maulana
# NIM         = 24060124140195
# Tanggal     = 23 September 2024 (tanggal mulai menulis di VsCode)
# Deskripsi   = mencari soal gradien magis

# DEFINISI DAN SPESIFIKASI
# gradien (a,b) : 2 int -> int
#   [gradien (a,b) adalah fungsi untuk menghitung gradien]
# f(x) : int -> int
#   [f(x) adalah fungsi untuk mencari nilai pada sebuah titik]

# REALISASI
def f(x) :
    return (3*(x**2)) + (2*x) - 5

def gradien(a,b) :
    return (f(a) - f(b))/(a - b)

    
print(eval(input()))

# APLIKASI
gradien(3,1)