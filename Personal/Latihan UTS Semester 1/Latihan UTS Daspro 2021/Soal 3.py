# DEFINISI TYPE
# type point : <x : real , y : real>
#   {<x,y> adalah point / titik. X = titik pada bagian x pada bidang cartesius dan y = titik pada bagian y bidang cartesius.}

# DEFINISI SELEKTOR


# REALISASI
# def make_point(x,y) :
#     return 

def GetPanjang(x1,x2) :
    return abs(x1 - x2)

def GetLebar(y1,y2) :
    return abs(y1 - y2)

def GetDiagonal(x1,y1,x2,y2) :

    return abs((GetPanjang(x1,x2)) ** 2 - (GetLebar(y1,y2)) ** 2)

# APLIKASI
print(GetDiagonal(2,6,8,6))