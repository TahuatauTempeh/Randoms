# Nama File   = Akar akar fungsi Kuadray
# Nama        = Azka A. Maulana
# Tanggal     = 11 September 2024
# Deskripsi   = Menentukan akar akar fungsi kuadrat

# DEFINISI DAN SPESIFIKASI
# fungsi_kuadrat (a,b,c) : 3 int -> int
#   {fungsi_kuadrat (a,b,c) adalah fungsi untuk menentukan hasil pembagian akar akar sebuah fungsi kuadrat}

# REALISASI
def fungsi_kuadrat (a,b,c) :
    d = (b**2-4*a*c)**0.5
    x1 = (-b + d)/(2*a*c)
    x2 = (-b - d)/(2*a*c)
    if x1 > x2 :
        return round(x1/x2)
    elif x2 > x1 :
        return round(x2/x1)
    # elif x1 < 0 or x2 < 0 :
    #     return print ("Invalid")
    # return x1,x2


    

# APLIKASI

print (fungsi_kuadrat(1,-7,3))
print (fungsi_kuadrat(-1,4,5))