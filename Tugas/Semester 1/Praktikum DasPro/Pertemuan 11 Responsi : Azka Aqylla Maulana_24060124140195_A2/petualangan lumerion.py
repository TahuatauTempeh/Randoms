#   Nama File   = lumerion
#   Nama        = Azka A. Maulana
#   NIM         = 24060124140195
#   Tanggal     = 4 Decembre 2024 (when it's written)
#   Deskripsi   = lumerion :0

#   REALISASI

def KonsLo(l,s) :
    return [l] + s

def KonsLi(s,l) :
    return s + [l]

def FirstList(s) :
    return s[0]

def LastList(s) :
    return s[-1]

def TailList(s) :
    return s[1:] 

def HeadList(s) :
    return s[:-1]

def isAtom(s) :
    return type(s) != list

def isList(s) :
    return type(s) == list

def IsEmpty(s) :
    return s == []

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


def NBElmtAtom(S) :
    if IsEmpty(S) :
        return 0
    else :
        if isAtom(FirstList(S)) :
            return 1 + NBElmtAtom(TailList(S))
        else :
            return NBElmtAtom(TailList(S))

def NBElmtList(S) :
    if IsEmpty(S) :
        return 0
    else :
        if isList(FirstList(S)) :
            return 1 + NBElmtList(TailList(S))
        else :
            return NBElmtList(TailList(S))

def SumLoL(S) :
    if IsEmpty(S) :
        return 0
    else :
        if isAtom(FirstList(S)) :
            return FirstList(S) + SumLoL(TailList(S))
        else :
            return SumLoL(FirstList(S)) + SumLoL(TailList(S))

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
            
def EvaluateExpression(s) : #   V3
    if IsEmpty(s) :  
        return []
    else :
        if isAtom(FirstList(s)):  
            ado = FirstList(s)
            miku = s[1]  
            teto = s[2]  
            if ado == '+':
                return miku + teto
            elif ado == '-':
                return miku - teto
            elif ado == '*':
                return miku * teto
            elif ado == '/':
                return miku / teto  
        else:
            return 0         
             
vocaloid = input("Weeee wooowowowowo: ")
vocaloided = vocaloid.split()
vocaloided[1] = int(vocaloided[1])
vocaloided[2] = int(vocaloided[2]) 

print(EvaluateExpression(vocaloided))


