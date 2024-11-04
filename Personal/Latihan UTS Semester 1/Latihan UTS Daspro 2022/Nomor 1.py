# DEFSPEK
# begitu dah

# REALISASI
def tarif(x) :
    if x > 30 :
        return x - 30
    else :
        return x == 0

def kode (x,y) :
    if y == "A" :
        return 200 + (tarif(x) * 10)
    elif y == "B" :
        return 300 + (tarif(x) * 20)
    elif y == "C" :
        return 350 + (tarif(x) * 25)

def harga(x,y) :
    return kode (x,y)

# APLIKASI
print(harga(25,"A"))
print(harga(100,"B"))
print(harga(5,"C"))