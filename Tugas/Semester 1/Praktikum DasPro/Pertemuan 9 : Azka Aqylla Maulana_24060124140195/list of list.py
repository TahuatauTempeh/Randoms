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

def IsEmpty(s) :
    return s == []

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
        
def isAtom(s) :
    return type(s) != list

def isList(s) :
    return type(s) == list

def KonsLo(l,s) :
    return [l] + s

def KonsLi(s,l) :
    return s + [l]

def 
