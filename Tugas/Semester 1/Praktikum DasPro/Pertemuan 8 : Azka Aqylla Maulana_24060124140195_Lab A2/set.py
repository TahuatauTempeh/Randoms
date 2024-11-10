#   Nama File   = set
#   Nama        = Azka A. Maulana
#   NIM         = 24060124140195
#   Tanggal     = 4 Novembre 2024 (when it's written)
#   Deskripsi   = set

#   DEFINISI TYPE
#   type list : [ ] or [e , list]
#       {elemen di bagian awal dan list di bagian akhir}
#   type list : [ ] or [list , e]
#       {elemen di akhir dan list di awal}
#   type set : [ ] or [e, set] 
#       {set adalah list yang tidak mengandung elemen berulang dan urutan elemen tidak diperhitungkan}


#   DEFINISI DAN SPESIFIKASI FUNGSI DASAR LIST
#   Konso: elemen, list -> list
#       {Konso(e, l) menambahkan elemen e di awal list l}
#   Konsi: list, elemen -> list
#       {Konsi(l, e) menambahkan elemen e di akhir list l}
#   FirstElmt: list tidak kosong -> elemen
#       {FirstElmt(l) mengembalikan elemen pertama dari list l}
#   LastElmt: list tidak kosong -> elemen 
#       {LastElmt(l) mengembalikan elemen terakhir dari list l}
#   Tail: list tidak kosong -> list
#       {Tail(l) mengembalikan list tanpa elemen pertama dari list l}
#   Head: list tidak kosong -> list
#       ead(l) mengembalikan list tanpa elemen terakhir dari list l}
#   IsEmpty: list -> boolean
#       {IsEmpty(l) mengembalikan True jika l adalah list kosong}
#   NbElmt: list -> integer
#       {NbElmt(l) menghitung jumlah elemen pada list l}

#   DEFINISI DAN SPESIFIKASI OPERASI LIST YANG DIPERLUKAN UNTUK HIMPUNAN
#   Rember: elemen, list -> list
#       {Rember(x,L) menghapus sebuah elemen x dari list L. Jika x ada di list L, maka elemen L berkurang 1. Jika x tidak ada di list L maka L tetap. List kosong tetap menjadi list kosong.}
#   MultiRember: elemen, list -> list
#       {MultiRember(x,L) menghapus semua kemunculan elemen x dari list L. List baru yang dihasilkan tidak lagi memiliki elemen x. List kosong tetap menjadi list kosong.}

#   DEFINISI DAN SPESIKASI KONSTRUKTOR SET DARI LIST
#   MakeSet: list -> set
#       {MakeSet(L) membuat set dari list L dengan menghapus semua kemunculan lebih dari satu kali. list kosong tetap menjadi himpunan kosong}

#   DEFINISI DAN SPESIKASI KONSTRUKTOR SET
#   KonsoSet: elemen,set -> set
#       {konsoSet(e,H) menambahkan sebuah elemen e sebagai elemen pertama set H dengan syarat e belum ada di dalam himpunan H}

#   DEFINISI DAN SPESIFIKASI PREDIKAT
#   IsSet: list -> boolean
#       {IsSet(L) mengembalikan true jika L adalah sebuah set}
#   IsSubset: 2 set -> boolean
#       {IsSubset(H1,H2) mengembalikan true jika H1 merupakan subset dari H2}
#   IsEqualSet: 2 set -> boolean
#       {IsEqualSet(H1,H2} benar jika H1 adalah set yang sama dengan H2}
#   IsIntersect: 2 set -> boolean
#       {IsIntersect(H1,H2) benar jika H1 beririsan dengan H2}

#   DEFINISI DAN SPESIFIKASI OPERASI TERHADAP HIMPUNAN 
#   MakeIntersect: 2 set -> set
#       {MakeIntersect(H1,H2) menghasilkan set baru yang merupakan hasil irisan antara H1 dan H2}
#   MakeUnion: 2 set -> set
#       {MakeUnion(H1,H2) menghasilkan set baru yang merupakan hasil gabungan antara H1 dan H2}
#   NBIntersect: 2 set -> integer 
#       {NBIntersect(H1,H2) menghasilkan jumlah elemen yang beririsan pada H1 dan H2 tanpa memanfaatkan fungsi MakeIntersect(H1,H2).}
#   NBUnion: 2 set -> integer
#       {NBUnion(H1,H2) menghasilkan jumlah elemen hasil gabungan antara H1 dan H2 tanpa memanfaatkan fungsi MakeUnion(H1,H2)}

#   REALISASI

def Konso(e,l) :
    return [e] + l

def Konsi(l,e) :
    return l + [e]

def FirstElmt(l) :
    return l[0]

def LastElmt(l) :
    return l[-1]

def Tail(l) :
    return l[1:]

def Head(l) :
    return l[:-1]

def IsEmpty(l) :
    return l == []
    
def NbElmt(l) :
    if IsEmpty(l) :
        return 0
    else :
        return 1 + NbElmt(Tail(l))

def IsMember (X,l) :
    if IsEmpty(l) :
        return False
    else :
        if FirstElmt(l) == X :
            return True
        else :
            return IsMember(X,Tail(l))
    
def Rember(x,l) :
    if IsEmpty(l) :
        return l
    else :
        if FirstElmt(l) == x :
            return Tail(l)
        else :
            return Konso(FirstElmt(l), Rember(x, Tail(l)))
        
def Rember2(x,l) :
    if IsEmpty(l) :
        return l
    else :
        if LastElmt(l) == x :
            return Head(l)
        else :
            return Konsi(Rember2(x, Head(l)), LastElmt(l))
        
def MultiRember(x,l) :
    if IsEmpty(l) :
        return l
    else :
        if FirstElmt(l) == x :
            return MultiRember(x,Tail(l))
        else :
            return Konso(FirstElmt(l), MultiRember(x,Tail(l)))

def MakeSetIM(l) :
    if IsEmpty(l) :
        return l
    else :
        if IsMember(FirstElmt(l), Tail(l)) :
            return MakeSetIM(Tail(l))
        else :
            return Konso(FirstElmt(l), MakeSetIM(Tail(l)))

def MakeSetMR(l) :
    if IsEmpty(l) :
        return l
    else :
        return Konso(FirstElmt(l), MakeSetMR(MultiRember(FirstElmt(l), Tail(l))))

def KonsoSet(e,h) :
    if IsMember(e,h) :
        return h 
    else :
        return Konso(e, h)

def IsSet(l) :
    if IsEmpty(l) :
        return True
    else :
        if IsMember(FirstElmt(l), (Tail(l)))  :
            return False
        else :
            return IsSet(Tail(l))

def IsSubset(h1,h2) : # h1 yang subset dari h2
    if IsEmpty(h1) :
        return True
    else :
        if IsMember(FirstElmt(h1), h2)  :
            return IsSubset(Tail(h1), h2)
        else :
            return False
        
def IsEqSet1(h1,h2) : # h1 di cek ke h2 dgn subset
    return IsSubset(h1,h2) and IsSubset(h2,h1)

def IsEqSet2(h1,h2) : # cek satu satu, h1 cek ke h2
    if IsEmpty(h1) :
        return True
    else :
        if FirstElmt(h1) == FirstElmt(h2) :
            return IsEqSet2(Tail(h1), Tail(h2))
        else :
            return False
        
def IsIntersect(h1, h2) :
    if IsEmpty(h1) :
        return False
    else :
        if IsMember(FirstElmt(h1), h2) :
            return True
        else :
            return IsIntersect(Tail(h1), h2)

def MakeIntersectV1(h1, h2) : # rekursif ke h1
    if IsEmpty(h1) :
        return []
    else : 
        if IsMember(FirstElmt(h1), h2) :
            return Konso(FirstElmt(h1), MakeIntersectV1(Tail(h1), h2))
        else :
            return MakeIntersectV1(Tail(h1), h2)

def MakeIntersectV2(h1, h2) : #  rekursif ke h2
    if IsEmpty(h2) :
        return []
    else :
        if IsMember(FirstElmt(h2), h1) :
            return Konso(FirstElmt(h2), MakeIntersectV2(h1, Tail(h2)))
        else :
            return MakeIntersectV2(h1, Tail(h2))
    
def MakeUnionV1(h1, h2) : # rekursif h1
    if IsEmpty(h1) :
        return h2
    else:
        return KonsoSet(FirstElmt(h1), MakeUnionV1(Tail(h1), h2))

def MakeUnionV2(h1, h2) : # rekursif h2
    if IsEmpty(h2) :
        return h1
    else :
        return KonsoSet(FirstElmt(h2), MakeUnionV2(h1, Tail(h2)))

def NBIntersect(h1, h2) :
    if IsEmpty(h1) :
        return 0
    else : 
        if IsMember(FirstElmt(h1), h2):
            return 1 + NBIntersect(Tail(h1), h2)
        else :
            return NBIntersect(Tail(h1), h2)

def NBUnion(h1, h2) :
    if IsEmpty(h1) : 
        return NbElmt(h2) 
    else : 
        if IsMember(FirstElmt(h1), h2):  
            return NBUnion(Tail(h1), h2)  
        else :
            return 1 + NBUnion(Tail(h1), h2)  


#   APLIKASI
print('=' * 120)
print(f"Rember depan : {Rember(4,[2,4,5,6,7,4,4,2])}")
print(f"Rember depan : {Rember(4,[4,4,5,6,7,4,4,2])}")
print('=' * 120)
print(f"Rember belakang : {Rember2(4,[2,4,5,6,7,4,4,2])}")
print(f"Rember belakang : {Rember2(2,[2,4,5,6,7,4,4,2])}")
print('=' * 120)
print(f"Multi Rember : {MultiRember(4,[2,2,2,4,4,4,5,4,5,4,5])}")
print(f"Multi Rember : {MultiRember(2,[2,2,2,4,4,4,5,4,5,4,5])}")
print('=' * 120)
print(f"Make set dengan IsMember : {MakeSetIM([2,2,2,2,3,4,3,5,6,4,8])}")
print(f"Make set dengan IsMember : {MakeSetIM([3,3,3,3,4,5,4,1,2,1,7,6,9])}")
print('=' * 120)
print(f"Make set dengan MultiRemmber : {MakeSetMR([2,2,2,2,2,3,4,5])}")
print(f"Make set dengan MultiRemmber : {MakeSetMR([9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,7,7,7,7,7,6,6,6,6,5,5,5,5])}")
print('=' * 120)
print(f"Konso set : {KonsoSet(3,[2,4,5,6])}")
print(f"Konso set : {KonsoSet(3,[])}")
print(f"Konso set : {KonsoSet(3,[1,2,3,4,5])}")
print('=' * 120)
print(f"Is set : {IsSet([3,3,4,5])}")
print(f"Is set : {IsSet([2,3,4,5])}")
print(f"Is set : {IsSet([2,3,4,5,5,5,5,5,5])}")
print('=' * 120)
print(f"Apakah Sub Set : {IsSubset([3,4],[1,2,3,4,5])}")
print(f"Apakah Sub Set : {IsSubset([6,7],[1,2,3,4,5])}")
print(f"Apakah Sub Set : {IsSubset([],[1,2,3,4,5])}")
print('=' * 120)
print(f"Apakah equal pakai subset : {IsEqSet1([1,2,3],[1,2,3])}")
print(f"Apakah equal pakai subset  : {IsEqSet1([2,4,6],[1,2,3])}")
print('=' * 120)
print(f"Apakah equal cek satu satu : {IsEqSet2([1,2,3],[1,2,3])}")
print(f"Apakah equal cek satu satu : {IsEqSet2([1,3,5],[1,2,3])}")
print('=' * 120)
print(f"Apakah Intersect : {IsIntersect([2,3,4],[1,2,3,4,5])}")
print(f"Apakah Intersect : {IsIntersect([6,7,8],[1,2,3,4,5])}")
print('=' * 120)    
print(f"Make Intersect : {MakeIntersectV1([1,2],[2,3,4])}")
print(f"Make Intersect : {MakeIntersectV1([1,3,4],[2,3,4])}")
print('=' * 120)   
print(f"Make Intersect : {MakeIntersectV2([1,3,4],[2,3,4])}")
print(f"Make Intersect : {MakeIntersectV2([1,2],[2,3,4])}")
print('=' * 120)   
print(f"Make Union terhadap h1 : {MakeUnionV1([1,2],[2,3,4])}")
print('=' * 120)   
print(f"Make Union terhadap h2 : {MakeUnionV2([1,2,6],[2,3,4])}")
print('=' * 120)  
print(f"NbIntersect : {NBIntersect([1,2,3,4],[1,2,3,4,5,6])}")
print('=' * 120)  
print(f"NbUnion : {NBUnion([1,2,3],[3,2])}")
print('=' * 120)  
print(f"NBUnion : {NBUnion([1,2,3],[3,4,5])}")

# dsadsajdasjdajsd