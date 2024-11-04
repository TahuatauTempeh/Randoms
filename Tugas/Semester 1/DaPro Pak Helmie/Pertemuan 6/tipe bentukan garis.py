# Nama File   = Type bentukan garis
# Nama        = Azka A. Maulana
# Tanggal     = 20 Octobre 2024 (when it's written)
# Deskripsi   = membuat fungsi garis dengan type bentukan garis

# DEFINISI TYPE
# type point: <x: real, y: real>
#   {membuat point dari x dan y}
# type garis: <P1: point, P2: point>
#   {membuat garis dari point 1 dan point 2}

# DEFINISI DAN SPESIFIKASI SELEKTOR
# GetX: point → real
#   {GetX(P) memberikan koordinat x dari sebuah point.}
# GetY: point → real
#   {GetY(P) memberikan koordinat y dari sebuah point.}
# GetP1: garis → point
#   {GetP1(G) memberikan point P1 dari sebuah garis.}
# GetP2: garis → point
#   {GetP2(G) memberikan point P2 dari sebuah garis.}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakePoint: 2 real → point
#   {MakePoint(x,y) membentuk point dari koordinat x dan y.}
# MakeGaris: 2 point → garis
#   {MakeGaris(P1,P2) membentuk garis dari dua buah point P1 dan P2.}

# DEFINISI DAN SPESIFIKASI OPERATOR 
# Gradien: garis → real
#   {Gradien(G) menghitung gradien dari garis G. Jika garis vertikal, mengembalikan None}
# PanjangGaris: garis → real
#   {PanjangGaris(G) menghitung panjang garis G menggunakan rumus Pythagoras.}
# IsSejajar: 2 garis → boolean
#   {IsSejajar(P1,P2) mengecek apakah dua garis sejajar, berdasarkan gradiennya.}
# IsTegakLurus: 2 garis → boolean
#   {IsTegakLurus(P1,P2) mengecek apakah dua garis tegak lurus, gradien G1 * gradien G2 == -1}

# REALISASI
def MakePoint(x, y):
    return [x, y]  

def GetX(P):
    return P[0]  

def GetY(P):
    return P[1] 

def MakeGaris(P1, P2):
    return [P1, P2] 

def GetP1(G):
    return G[0]  

def GetP2(G):
    return G[1] 

def Gradien(G):
    if GetX(GetP1(G)) == GetX(GetP2(G)):
        return None  
    else :
        return (GetY(GetP2(G)) - GetY(GetP1(G))) / (GetX(GetP2(G)) - GetX(GetP1(G)))

def PanjangGaris(G):
    return (((GetX(GetP2(G)) - GetX(GetP1(G))) ** 2) + ((GetY(GetP2(G)) - GetY(GetP1(G))) ** 2)) ** 0.5

def IsSejajar(G1, G2):
    return Gradien(G1) == Gradien(G2)

def IsTegakLurus(G1, G2):
    if Gradien(G1) == None :
        return Gradien(G2) == 0
    elif Gradien(G2) == None :
        return Gradien(G1) == 0 
    else :
        return Gradien(G1) * Gradien(G2) == -1
    
# APLIKASI
print(Gradien(MakeGaris(MakePoint(3, 2), MakePoint(6, 8)))) # 2.0
print(PanjangGaris(MakeGaris(MakePoint(3, 2), MakePoint(6, 8)))) # 6.708203932499369
print(Gradien(MakeGaris(MakePoint(2, 7), MakePoint(5, 3))))  # -1.3333333
print(PanjangGaris(MakeGaris(MakePoint(2, 7), MakePoint(5, 3)))) # 5.0
print(IsSejajar(MakeGaris(MakePoint(3, 2), MakePoint(6, 8)), MakeGaris(MakePoint(2, 7), MakePoint(5, 3)))) # False
print(IsTegakLurus(MakeGaris(MakePoint(3, 2), MakePoint(6, 8)), MakeGaris(MakePoint(2, 7), MakePoint(5, 3)))) # False
print(Gradien(MakeGaris(MakePoint(2, 3), MakePoint(2, 7)))) # None
print(Gradien(MakeGaris(MakePoint(1, 3), MakePoint(5, 3)))) # 0.0
