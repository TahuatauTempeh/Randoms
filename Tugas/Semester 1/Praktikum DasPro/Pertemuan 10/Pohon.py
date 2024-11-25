from lol import *

#   DEFINISI DAN SPESIFIKASI TYPE
#       Type elemen: {tergantung type node}
#   Type Pohon-Ner : <A: Elemen, PN:Pohon-Ner> {notasi Prefix}
#       {Pohon N-ner terdiri dari Akar yang berupa elemen dan list dari pohon N-aire yang menjadi anaknya List anak mungkin kosong, tapi pohon N-ner tidak pernah kosong karena minimal mempunyai sebuah elemen sehagai akar pohon.}

#   DEFINISI DAN SPESIFIKASI KONSTRUKTOR
def MakePN(A,PN):
    return [A,PN]

#   DEFINISI DAN SPESIFIKASI SELEKTOR
#   Akar : PohonN-ner tidak  kosong  -→  Elemen  
#       {Akar(P) adalah Akar dari P. Jika P adalah (A,PN) = Akar(P)adaLah A.}  
def akar(PN):
    return PN[0]

 #  Anak  :  PohonN-ner  tidak  kosong  →  List  of  PohonN-  ner  
 #      {Anak(P) adalah List  of pohon N-ner yang merupakan anak-anak (sub phon) dari P. Jika P adalah (A,PN) = Anak  (P) adalah PN.}
def anak(PN):
    return PN[1]

#   DEFINISI DAN SPESOFIKASI PRDIKAT
#   IsTreeNEmpty. PohonN-ner -→ boolean
#       {Is Tree NEmptyIsTreeNEmpty(PN) true jika PN kosong []}
def IsTreeNEmpty(PN):
    return PN == []

#   IsOneElmt: PohonN-ner -→ boolean
#       {IsOne Elmt(PN) true jika PN hanya terdiri dari Akar}
def IsOneElmt(PN):
    return not IsTreeNEmpty(PN)  and IsTreeNEmpty(anak(PN))

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


Wee = MakePN(1,[])
Woo = MakePN(1,[MakePN(2,[MakePN(3,[]),MakePN(4,[])])])

print('-' * 120)
print(Wee) # [2,[]]
print('-' * 120)
print(IsTreeNEmpty(Wee)) # False
print('-' * 120)
print(IsOneElmt(Wee)) # True
print('-' * 120)
print(Woo) 
print('-' * 120)
print(NbNElmt(Woo))
print('-' * 120)
print(NbDaun(Woo))
print('-' * 120)