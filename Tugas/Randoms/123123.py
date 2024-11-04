def Make_point(X,Y):
    return [X,Y]

def Make_Segiempat(P1,P2,P3,P4):
    return [P1,P2,P3,P4]

# Realisasi Selector
def absis(P):
    return P[0]

def ordinat(P):
    return P[1]

def Point1(S):
    return S[0]

def Point2(S):
    return S[1]

def Point3(S):
    return S[2]

def Point4(S):
    return S[3]

# Realisasi operator terhadap Point
def Jarak(P1,P2):
    return (((absis(P1) - absis(P2))** 2) + ((ordinat(P1) - ordinat(P2))** 2))**0.5

def Gradien(P1,P2):
    return (ordinat(P2) - ordinat(P1)) / (absis(P2) - absis(P1))

# Realisasi operator terhadap Segiempat
def AreaBujurSangkar(S):
    return Jarak(Point1(S), Point2(S)) * Jarak(Point3(S), Point4(S))

# Realisasi Predikat
def isBujurSangkar(S):
    return Jarak(Point1(S), Point2(S)) == Jarak(Point3(S), Point4(S)) and Jarak(Point1(S), Point3(S)) == Jarak(Point2(S), Point4(S))

def isJarjargenjang(S):
    P1 = Point1(S)
    P2 = Point2(S)
    P3 = Point3(S)
    P4 = Point4(S)
    return Gradien(P1, P2) == Gradien(P3, P4) and Gradien(P1, P4) == Gradien(P2, P3) and Jarak(P1, P2) == Jarak(P3, P4) and Jarak(P1, P4) == Jarak(P2, P3)


# =================================================================================================================================================================
# Aplikasi
# =================================================================================================================================================================

# Contoh Aplikasi 1: Segiempat bujur sangkar
S_bujur_sangkar = Make_Segiempat(Make_point(1, 3), Make_point(2, 3), Make_point(1, 2), Make_point(2, 2))

# Contoh Aplikasi 2: Segiempat jajar genjang
S_jajar_genjang = Make_Segiempat(Make_point(1, 1), Make_point(4, 1), Make_point(6, 4), Make_point(3, 4))

# Menghitung dan mencetak hasil aplikasi
print("Area Bujur Sangkar:", AreaBujurSangkar(S_bujur_sangkar))  # Output: Area dari bujur sangkar
print("Apakah bujur sangkar?:", isBujurSangkar(S_bujur_sangkar))  # Output: True atau False
print("Apakah jajar genjang?:", isJarjargenjang(S_jajar_genjang))  # Output: True atau False