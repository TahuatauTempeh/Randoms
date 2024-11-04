# Nama File   = tipe bentukan garis
# Nama        = Azka A. Maulana
# NIM         = 24060124140195
# Tanggal     = 29 September 2024 (tanggal mulai menulis di VsCode)
# Deskripsi   = menjawab soal tipe bentukan garis

# Definisi type
# type Point: <x:integer, y:integer>
#   {<x,y> adalah sebuah point dengan x adalah absis dan y adalah oordinat}

# Definisi Dan Spesifikasi Konstruktor
# Make-point: 2real --> point
#   {Make_point(X,Y) membentuk point dari x dan y dengan x sebagai absis dan y sebagai oordinat}
# Realisasi
def Make_point(X,Y):
    return [X,Y]

# Definisi Dan Spesifikasi Selector
# absis: point --> integer
#   {absis(P) memberikan absis dari point P}
# oordinat: point --> integer
#   {oordinat(P) memberikan oordinat dari point P}
# Realisasi
def absis(P):
    return P[0]

def oordinat(P):
    return P[1]

# =================================================================================================================================================================
# Definisi type
# type Garis: <P1:point, P2:point>
#   {<P1,P2> adalah sebuah garis dengan P1 adalah Point1 dan P2 adalah Point2}

# Definisi Dan Spesifikasi Konstruktor
# Make-Garis: 2point --> Garis
#   {Make_Garis(P1,P2) membentuk Garis dari P1 dan P2 dengan P1 sebagai point-1 dan P2 sebagai point-2}
# Realisasi
def Make_Garis(P1,P2):
    return [P1,P2]

# Definisi Dan Spesifikasi Selector
# Point1: Garis --> Point
#   {Point1(G) memberikan Point-1 dari Garis G}
# 
# Point2: Garis --> Point
#   {Point2(G) memberikan Point-2 dari Garis G}
# Realisasi
def Point1(G):
    return G[0]

def Point2(G):
    return G[1]

# Definisi dan Spesifikasi Operator/Fungsi Lain terhadap garis
# panjang_garis: Garis --> real
#   {panjang_garis(G) menghitung panjang garis dari point-1 ke point-2}
# Realisasi
def panjang_garis(G):
    panjang_x = absis(Point2(G)) - absis(Point1(G))
    panjang_y = oordinat(Point2(G)) - oordinat(Point1(G))
    return ((panjang_x ** 2) + (panjang_y ** 2))**0.5


# Definisi dan Spesifikasi Predikat
# Issejajar: Garis --> Boolean
#   {IsSejajar(G1,G2) benar jika G1 sama dengan G2}
# Realisasi
def IsSejajar(G1,G2):
    return G1 == G2


# Aplikasi 
print(IsSejajar(Make_Garis(Make_point(1,2), Make_point(1,2)), Make_Garis(Make_point(1,2), Make_point(1,2))))
print(IsSejajar(Make_Garis(Make_point(1,2), Make_point(1,2)), Make_Garis(Make_point(1,3), Make_point(1,5))))
print(panjang_garis(Make_Garis(Make_point(2,2), Make_point(5,2))))