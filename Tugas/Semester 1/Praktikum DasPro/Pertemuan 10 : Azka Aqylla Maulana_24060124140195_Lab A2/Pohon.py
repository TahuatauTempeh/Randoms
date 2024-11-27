#   Nama File   = Tree
#   Nama        = Azka A. Maulana
#   NIM         = 24060124140195
#   Tanggal     = 22 Novembre 2024 (when it's written)
#   Deskripsi   = tree itu pohon

print('-' * 120)

from lol import *

#   DEFINISI DAN SPESIFIKASI TYPE
#       Type elemen: {tergantung type node}
#   Type Pohon-Ner : <A: Elemen, PN:Pohon-Ner> {notasi Prefix}
#       {Pohon N-ner terdiri dari Akar yang berupa elemen dan list dari pohon N-aire yang menjadi anaknya List anak mungkin kosong, tapi pohon N-ner tidak pernah kosong karena minimal mempunyai sebuah elemen sehagai akar pohon.}

#   DEFINISI DAN SPESIFIKASI KONSTRUKTOR
def MakePN(A,PN):
    return [A,PN]

print('*' * 12, "MakePN :", '*' * 12)
print('-' * 120)
print(MakePN(1, []))
print('-' * 120)
print(MakePN(2, [[3, []]]))
print('-' * 120)
print(MakePN(1, [[2, [[3, []]]]]))
print('-' * 120)

#   DEFINISI DAN SPESIFIKASI SELEKTOR
#   Akar : PohonN-ner tidak  kosong  -→  Elemen  
#       {Akar(P) adalah Akar dari P. Jika P adalah (A,PN) = Akar(P)adaLah A.}  
def akar(PN):
    return PN[0]

print('*' * 12, "Akar", '*' * 12)
print('-' * 120)
print(akar([1, []]))
print('-' * 120)
print(akar([2, [[3, []]]]))
print('-' * 120)
print(akar([1, [[2, [[3, []]]]]]))
print('-' * 120)

 #  Anak  :  PohonN-ner  tidak  kosong  →  List  of  PohonN-  ner  
 #      {Anak(P) adalah List  of pohon N-ner yang merupakan anak-anak (sub phon) dari P. Jika P adalah (A,PN) = Anak  (P) adalah PN.}
def anak(PN):
    return PN[1]

print('*' * 12, "Anak", '*' * 12)
print('-' * 120)
print(anak([1, []]))
print('-' * 120)
print(anak([2, [[3, []]]]))
print('-' * 120)
print(anak([1, [[2, [[3, []]]]]]))
print('-' * 120)

#   DEFINISI DAN SPESOFIKASI PRDIKAT
#   IsTreeNEmpty. PohonN-ner -→ boolean
#       {Is Tree NEmptyIsTreeNEmpty(PN) true jika PN kosong []}
def IsTreeNEmpty(PN):
    return PN == []

print('*' * 12, "Tree kosong", '*' * 12)
print('-' * 120)
print(IsTreeNEmpty([]))
print('-' * 120)
print(IsTreeNEmpty([1, []]))
print('-' * 120)
print(IsTreeNEmpty([2, [[3, []]]]))
print('-' * 120)

#   IsOneElmt: PohonN-ner -→ boolean
#       {IsOne Elmt(PN) true jika PN hanya terdiri dari Akar}
def IsOneElmt(PN):
    return not IsTreeNEmpty(PN)  and IsTreeNEmpty(anak(PN))

print('*' * 12, "Satu elemen", '*' * 12)
print('-' * 120)
print(IsOneElmt([1, []]))
print('-' * 120)
print(IsOneElmt([2, [[3, []]]]))
print('-' * 120)
print(IsOneElmt([1, [[2, []]]]))
print('-' * 120)

#   DEFINISI DAN SPESIFIKASI OPERATOR
#   NbNElmt PohonN-ner -→ integer >= 0
#       {NbNElmt(PN) memberikan banyaknya node dari pohon PN}
#   Basis 1 NbNElmt ((A)\)=1
#   Rekurens NbNElmt ((A,PN))= 1 + NbNElmt(PN)}

def NbNElmt(PN):
    if IsTreeNEmpty(PN):
        return 0
    elif IsOneElmt(PN):
        return 1
    else:
        return 1 + NbNElmt(anak(PN)[0]) + NbElmntChild(anak(PN)[1:])
    
#   Fungsi tambahan untuk menghitung jumlah elemen pada sisa anak-anak
def NbElmntChild(PN):
    if IsTreeNEmpty(PN):
        return 0
    else:
        return NbNElmt(PN[0]) + NbElmntChild(PN[1:])
    
print('*' * 12, "Jumlah node biasa?", '*' * 12)
print('-' * 120)
print(NbNElmt([1, []]))
print('-' * 120)
print(NbNElmt([2, [[3, []]]]))
print('-' * 120)
print(NbNElmt([1, [[2, [[3, []]]]]]))
print('-' * 120)

print('*' * 12, "Jumlah node anak?", '*' * 12)
print('-' * 120)
print(NbElmntChild([]))
print('-' * 120)
print(NbElmntChild([[3, []]]))
print('-' * 120)
print(NbElmntChild([[2, [[3, []]]], [4, []]]))
print('-' * 120)
    
#   NbDaun PohonN-ner -→ integer >= 0
#       {NbDaun(PN) memberikan banyaknya daun dari pohon PN}
#   Basis 1 NbDaun ((A)\)=1
#   Rekurens NbDaun ((A,PN)) = NbDaun(PN)}

def NbDaun(PN):
    if IsTreeNEmpty(PN):
        return 0
    elif IsOneElmt(PN) and IsTreeNEmpty(anak(PN)):
        return 1
    else:
        return NbDaunChild(anak(PN))

#   Fungsi tambahan untuk menghitung jumlah daun pada sisa anak-anak
def NbDaunChild(PN):
    if IsTreeNEmpty(PN):
        return 0
    
    else:
        return NbDaun(PN[0]) + NbDaunChild(PN[1:])

print('*' * 12, "Julah daun di pohon?", '*' * 12)
print('-' * 120)
print(NbDaun([1, []]))
print('-' * 120)
print(NbDaun([2, [[3, []]]]))
print('-' * 120)
print(NbDaun([1, [[2, [[3, []]]]]]))
print('-' * 120)

print('*' * 12, "Jumlah daun di anak pohon?", '*' * 12)
print('-' * 120)
print(NbDaunChild([]))
print('-' * 120)
print(NbDaunChild([[3, []]]))
print('-' * 120)
print(NbDaunChild([[2, [[3, []]]], [4, []]]))
print('-' * 120)

# Wee = MakePN(1,[])
# Woo = MakePN(1,[MakePN(2,[MakePN(3,[]),MakePN(4,[])])])

# print(Wee) # [2,[]]
# print('-' * 120)
# print(IsTreeNEmpty(Wee)) # False
# print('-' * 120)
# print(IsOneElmt(Wee)) # True
# print('-' * 120)
# print(Woo) 
# print('-' * 120)
# print(NbNElmt(Woo))
# print('-' * 120)
# print(NbDaun(Woo))
# print('-' * 120)