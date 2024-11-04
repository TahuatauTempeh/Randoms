# DEFINISI DAN SPESIFIKASI
# type : int > 0 -> int > 0
#   {type(x) adalah fungsi untuk menentukan bagaimana luas penggunaan air akan dihitung berdasarkan x. Jika x adalah 19, makah harga akan menyesuaikan dengan kode pelanggan. 
# # Jika x > 10 maka x - 10 dan akan ditambahkan dengan harga sesuai kode pelanggan.}
# tagihan : int > 0 , str -> int > 0
#   {tagihan (x,y) adalah fungsi untuk menentukan tagihan air berdasarkan x (luas penggunaan air) dan y (kode pelanggan).}

# REALISASI
def type(x) :
    if x > 10 :
        return x - 10
    else :
        return x == 0
    
def tagihan (x,y) :
    if y == "A" :
        return 30000 + (type(x) * 2500)
    elif y == "B" :
        return 40000 + (type(x) * 3000)
    elif y == "C" :
        return 50000 + (type(x) * 3500)

# APLIKASI
print(tagihan(25,"A"))
print(tagihan(35,"B"))
print(tagihan(5,"C"))