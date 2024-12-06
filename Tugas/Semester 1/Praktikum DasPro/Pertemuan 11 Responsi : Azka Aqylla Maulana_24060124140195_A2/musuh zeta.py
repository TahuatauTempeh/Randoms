#   Nama File   = musuh zeta
#   Nama        = Azka A. Maulana
#   NIM         = 24060124140195
#   Tanggal     = 4 Decembre 2024 (when it's written)
#   Deskripsi   = musuh zeta :0


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

def IsOneElmt(l) :
    if IsEmpty(l) :
        return False
    else :
        return Tail(l) == [] and Head(l) == []
    
def NbElmt(l) :
    if IsEmpty(l) :
        return 0
    else :
        return 1 + NbElmt(Tail(l))
    
def ElmtKeN(N,l) :
    if N == 1 :
        return FirstElmt(l)
    else :
        return ElmtKeN(N - 1, Tail(l))
    
def IsMember (X,l) :
    if IsEmpty(l) :
        return False
    else :
        if FirstElmt(l) == X :
            return True
        else :
            return IsMember(X,Tail(l))
        
def FindMax(wewo) :
    if IsOneElmt(wewo) : 
        return FirstElmt(wewo)
    else :
        tail_max = FindMax(Tail(wewo))
        if FirstElmt(wewo) > tail_max :
            return FirstElmt(wewo)
        else :
            return tail_max

def RemoveElmt(X, wewo) :
    if IsEmpty(wewo) : 
        return []
    else :
        if FirstElmt(wewo) == X :
            return RemoveElmt(X, Tail(wewo))
        else :
            return Konso(FirstElmt(wewo), RemoveElmt(X, Tail(wewo)))
        
def DescendingSortUnique(wewo) :
    if IsEmpty(wewo):
        return []
    else :
        max_elmt = FindMax(wewo)
        filtered_list = RemoveElmt(max_elmt, wewo)
        return Konso(max_elmt, DescendingSortUnique(filtered_list))


#   APLIKASI
user_input = [int(x) for x in input().split(',')]
print(DescendingSortUnique(user_input))