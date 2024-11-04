#   Nama File   = set
#   Nama        = Azka A. Maulana
#   NIM         = 24060124140195
#   Tanggal     = 4 Novembre 2024 (when it's written)
#   Deskripsi   = set

#   DEFINISI TYPE

#   REALISASI

from list_24060124140195a import *

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
        
def IsIntersect(h1,h2) :
    

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
