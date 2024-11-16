#   Nama File   = List of list
#   Nama        = Azka A. Maulana
#   NIM         = 24060124140195
#   Tanggal     = 11 Novembre 2024 (when it's written)
#   Deskripsi   = list of list :0


#   IsAtom : list of list -> boolean
#       {IsAtom(s) benar jika s adalah atom(integer lah basically, not list)}
def isAtom(s) :
    return type(s) != list

print(f"IsAtom : {isAtom([3,2,3])}")
print('-' * 120)

#   IsList : list of list -> boolean
#       {IsList(s) benar jika s adalah list}
def isList(s) :
    return type(s) == list

print(f"IsList : {isList([1,2,3,4,5,5,5,6])}")
print('-' * 120)

#   KonLo : list, list of list, -> list of list
#       {KonsLo(l,s) menambahkan list l kepada list s di di awal}
def KonsLo(l,s) :
    return [l] + s

print(f"Konslo : {KonsLo([3,4],[1,2,5])}")
print('-' * 120)

#   KonsLi : list of list, list -> list of list
#       {KonsLi(s,l) menambahkan list l kepada list s di akhir}
def KonsLi(s,l) :
    return s + [l]

print(f"Konsli : {KonsLi([1,2],[1,2,3])}")
print('-' * 120)

#   FirstList : list tidak kosong -> list
#       {FirstList(s) mengembalikan anggota pertama list s. Bisa atom dan bisa juga list}
def FirstList(s) :
    return s[0]

print(f"FirstList : {FirstList([1,2,3,4])}")
print('-' * 120)

#   LastList : list tidak kosong -> list
#       #{LastList(s) mengembalikan anggotan akhir list s. Bisa atom, dan bisa juga list}
def LastList(s) :
    return s[-1]

print(f"LastList : {LastList([1,2,3,4])}")
print('-' * 120)

#   TailList : list tidak kosong -> list
#       {TailList(s) mengebalikan list s tanpa anggota pertama dari list s. Yang dihilangkan bisa list, bisa atom}
def TailList(s) :
    return s[1:] 

print(f"TailList : {TailList([1,2,3,4])}")
print('-' * 120)

#   HeadList : list tidak kosong -> list
#       {HeadList(s) mengembalikan list s tanpa anggota terakhir dari list s. Yang dihilangkan bisa list bisa atom}
def HeadList(s) :
    return s[:-1]

print(f"HeadList : {HeadList([1,2,3,4])}")
print('-' * 120)

#   IsEmpty : list of list -> boolean
#       {IsEmpty(s) benar jika s kosong}
def IsEmpty(s) :
    return s == []

print(f"IsEmpty : {IsEmpty([3,4,2])}") 
print('-' * 120)   

#   NBElmt : list -> integer
#       {NBElmt(s) menghitung jumlah anggota list s}
def NbElmt(s) :
    if IsEmpty(s) :
        return 0
    else :
        return 1 + NbElmt(TailList(s))

print(f"NbElmt : {NbElmt([1,2,3,4,5])}")
print('-' * 120)

#   IsEqual : list, list -> boolean
#       {IsEqual(s1,s2) true jika member dari list s1 sama dengan member dari list s2}
def IsEqual(s1,s2) :
    if NbElmt(s1) == NbElmt(s2) :
        if IsEmpty(s1) and IsEmpty(s2) :
            return True
        else :
            return FirstList(s1) == FirstList(s2) and IsEqual(TailList(s1),TailList(s2))
    else :
        return False
    
print(f"IsEqual : {IsEqual([2,3],[2,3,4])}")
print('-' * 120)

#   IsMemberLS : list, list of list -> boolean
#       {IsMemberLS(l,s) true jika  bagian dari list s}
def IsMemberLS(l,s) :
    if IsEmpty(s) :
        return False
    else :
        if isAtom(FirstList(s)) :
            return IsMemberLS(l,TailList(s))
        else :
            if IsEqual(FirstList(s),l) :
                return True
            else :
                return IsMemberLS(l,Tail(s))
            
print(f"IsmemberLS : {IsMemberLS([1,2],[[1,2],3,[4],5])}")
print('-' * 120)

#   IsEqS : 2 list of list -> boolean
#       {IsEqS(s1,s2) true jika s1 = s2}
def IsEqS(s1,s2) :
    if IsEmpty(s1) and IsEmpty(s2) :
        return True
    else :
        if IsEmpty(s1) and not IsEmpty(s2) :
           return False
        else :
            if not IsEmpty(s1) and IsEmpty(s2) :
                return False
            else :
                if isAtom(FirstList(s1)) and isAtom(FirstList(s2)) :
                    if FirstList(s1) == FirstList(s2) :
                        return IsEqS(TailList(s1),TailList(s2))
                    else :
                        return False
                else :
                    if isList(FirstList(s1)) and isList(FirstList(s2)) :
                        return IsEqS(FirstList(s1),FirstList(s2)) and IsEqS(LastList(s1),LastList(s2))
                    else :
                        return False
                    
print(f"IsEqS : {IsEqS([[2,3],2,3,4],[2,3,[2,3],4])}")
print('-' * 120)

#   IsmemberS : elemen, list of list -> boolean
#       {IsMemberS(x,S) true jika elemex x ada di S}
def IsMemberS(x, S) :
    if IsEmpty(S) :
        return False
    else :
        if isAtom(FirstList(S)) :
            return FirstList(S) == x or IsMemberS(x, TailList(S))
        else :
            return IsMemberS(x, FirstList(S)) or IsMemberS(x, TailList(S))
        
print(f"IsMemberS : {IsMemberS(1,[1,2,[3,4,5],[6,7],[]])}")
print('-' * 120)

#   Rember : elemen, list of list -> list of list
#       {Rember(x,s) menghapus semua elemen x dari list s}
def Rember(x, S) :
    if IsEmpty(S) :
        return []
    else :
        if isAtom(FirstList(S)) :
            if FirstList(S) == x :
                return Rember(x, TailList(S))
            else :
                return KonsLo(FirstList(S), Rember(x, TailList(S)))
        else :
            return KonsLo(Rember(x, FirstList(S)), Rember(x, TailList(S)))

print(f"Rember : {Rember(4,[1,2,3,[1,2,4,4],4,[6,4]])}")
print('-' * 120)

#   Max: list of list -> elemen
#       {Max(S) mengembalikan elemen maksimum di dalam list of list S}
def Max(S) :
    if IsEmpty(S) : 
        return -999999999  
    else :
        if isAtom(FirstList(S)) :  
            if FirstList(S) > Max(TailList(S)) :
                return FirstList(S)
            else :
                return Max(TailList(S))
        else :  
            return Max(FirstList(S) + TailList(S)) 

print(f"Max : {Max([4, 5, 6, [8,9,10], [12,0], 8])}")
print('-' * 120)

#   NBElmtAtom(S) : list of list -> integer
#       {NBElmtAtom(S) mengembalikan banyak atom s}

def NBElmtAtom(S) :
    if IsEmpty(S) :
        return 0
    else :
        if isAtom(FirstList(S)) :
            return 1 + NBElmtAtom(TailList(S))
        else :
            return NBElmtAtom(FirstList(S)) + NBElmtAtom(TailList(S))
        
print(f"NBElmtAtom : {NBElmtAtom([4, 5, 6, [8,9,10], [12,0], 8,[]])}")
print('-' * 120)

#   NBElmtList : list of list -> integer
#       {NBElmtList(S) mengembalikan banyak list s}
def NBElmtList(S) :
    if IsEmpty(S) :
        return 0
    else :
        if isList(FirstList(S)) :
            return 1 + NBElmtList(TailList(S))
        else :
            return NBElmtList(TailList(S))

print(f"NBElmtlist : {NBElmtList([4, 5, 6, [8,9,10], [12,0], 8])}")
print('-' * 120)

#   SumLoL : list of list -> integer
#       {SumLol(S) mengembalikan jumlah semua elemen dalam list of list S}
def SumLoL(S) :
    if IsEmpty(S) :
        return 0
    else :
        if isAtom(FirstList(S)) :
            return FirstList(S) + SumLoL(TailList(S))
        else :
            return SumLoL(FirstList(S)) + SumLoL(TailList(S))
        
print(f"SumLoL : {SumLoL([4, 5, 6, [2,3,1]])}") 
print('-' * 120)

#   MaxNBElmtList : list of list -> integer
#       {MaxNBElmt(S) mengembalikan banyaknya elemen list maksimum yang ada pada list of list S}
def MaxNBElmtList(S) :
    if IsEmpty(S) :
        return 0
    else :
        if isList(FirstList(S)) :
            if NbElmt(FirstList(S)) > MaxNBElmtList(TailList(S)) :
                return NbElmt(FirstList(S))
            else :
                return MaxNBElmtList(TailList(S))
        else :
            return MaxNBElmtList(TailList(S))

print(f"MaxNBElmtList : {MaxNBElmtList([[4,5,6,7], [8,9,10], [12,0], 8])}")
print('-' * 120)

#   MaxSumElmt: list of list -> integer
#       {MaxSumElmt(S) mengembalikan elemen maksimum pada list of list S}
def MaxSumElmt(S) :
    if IsEmpty(S) :
        return -999999999  
    else :
        if isAtom(FirstList(S)) :
            if FirstList(S) > MaxSumElmt(TailList(S)) :
                return FirstList(S)
            else :
                return MaxSumElmt(TailList(S))
        else :
            if SumLoL(FirstList(S)) > MaxSumElmt(TailList(S)) :
                return SumLoL(FirstList(S))
            else :
                return MaxSumElmt(TailList(S))

print(f"MaxSumElmt : {MaxSumElmt([[1,2], 9, [4,5,6], 8])}")
print('-' * 120)
# dasdasdasdas

