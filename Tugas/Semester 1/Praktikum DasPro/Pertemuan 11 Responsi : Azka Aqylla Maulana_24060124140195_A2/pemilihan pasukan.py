#   Nama File   = pasukan
#   Nama        = Azka A. Maulana
#   NIM         = 24060124140195
#   Tanggal     = 4 Decembre 2024 (when it's written)
#   Deskripsi   = pasukan

#   REALISASI

def KonsLo(l,s) :
    return [l] + s

def KonsLo(l,s) :
    return [l] + s

def FirstList(s) :
    return s[0]

def LastList(s) :
    return s[-1]

def TailList(s) :
    return s[1:] 

def HeadList(s) :
    return s[:-1]

def NbElmt(s) :
    if IsEmpty(s) :
        return 0
    else :
        return 1 + NbElmt(TailList(s))

def IsEqual(s1,s2) :
    if NbElmt(s1) == NbElmt(s2) :
        if IsEmpty(s1) and IsEmpty(s2) :
            return True
        else :
            return FirstList(s1) == FirstList(s2) and IsEqual(TailList(s1),TailList(s2))
    else :
        return False

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
                return IsMemberLS(l,TailList(s))
            
def isAtom(s) :
    return type(s) != list            

def IsEqS(s1, s2) :
    if IsEmpty(s1) and IsEmpty(s2) :
        return True
    elif IsEmpty(s1) or IsEmpty(s2) :
        return False
    else :
        if isAtom(FirstList(s1)) and isAtom(FirstList(s2)) :
            if FirstList(s1) == FirstList(s2) :
                return IsEqS(TailList(s1), TailList(s2))
            else :
                return False
        elif isList(FirstList(s1)) and isList(FirstList(s2)) :
            return IsEqS(FirstList(s1), FirstList(s2)) and IsEqS(TailList(s1), TailList(s2))
        else :
            return False
        
def IsMemberS(x, S) :
    if IsEmpty(S) :
        return False
    else :
        if isAtom(FirstList(S)) :
            return FirstList(S) == x or IsMemberS(x, TailList(S))
        else :
            return IsMemberS(x, FirstList(S)) or IsMemberS(x, TailList(S))
        
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
        
def SumLoL(S) :
    if IsEmpty(S) :
        return 0
    else :
        if isAtom(FirstList(S)) :
            return FirstList(S) + SumLoL(TailList(S))
        else :
            return SumLoL(FirstList(S)) + SumLoL(TailList(S))
        
def NBElmtAtom(S) :
    if IsEmpty(S) :
        return 0
    else :
        if isAtom(FirstList(S)) :
            return 1 + NBElmtAtom(TailList(S))
        else :
            return NBElmtAtom(TailList(S))
        
def avg(s) :
    if IsEmpty(s) :
        return 0  
    else :
        return SumLoL(s) / NBElmtAtom(s)


def IsEmpty(s) :
    return s == []

def hapusKuat(LoL, Avg) :
    if IsEmpty(LoL) :
        return []
    else : 
        return KonsLo(RemberAbove(FirstList(LoL)  , Avg)  , hapusKuat(TailList(LoL), Avg))  

def RemberAbove(unit, Avg) :
    if IsEmpty(unit) :  
        return []
    else :
        reee = FirstList(unit)
        if reee > Avg: 
            return RemberAbove(TailList(unit), Avg) 
        else : 
            return KonsLo(reee, RemberAbove(TailList(unit), Avg)) 


# APLIKASI 

import ast

LoL = ast.literal_eval(input("Masukkan"))

Avg = avg(LoL)

print(hapusKuat(LoL, Avg))

#   IDK this one kak