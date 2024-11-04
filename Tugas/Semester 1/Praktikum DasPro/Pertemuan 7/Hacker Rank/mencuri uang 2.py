#   Nama File   = mencuri uang
#   Nama        = Azka A. Maulana
#   NIM         = 24060124140195
#   Tanggal     = 28 Octobre 2024 (when it's written)
#   Deskripsi   = Hacker rank

user_input = input("")

def Konso(e, l):
    return [e] + l

def IsEmpty(s):
    return s == ""

def FirstChar(s):
    return s[0]

def TailString(s):
    return s[1:]

def StringToList(s):
    if IsEmpty(s):
        return []
    else:
        return Konso(FirstChar(s), StringToList(TailString(s)))

def char_to_int(c):
    if c == '0':
        return 0
    elif c == '1':
        return 1
    elif c == '2':
        return 2
    elif c == '3':
        return 3
    elif c == '4':
        return 4
    elif c == '5':
        return 5
    elif c == '6':
        return 6
    elif c == '7':
        return 7
    elif c == '8':
        return 8
    elif c == '9':
        return 9

def is_digit(S):
    return '0' <= S <= '9'

def hasil(S):
    if IsEmpty(S):
        return 0
    else:
        if is_digit(FirstChar(S)):
            return char_to_int(FirstChar(S)) + hasil(TailString(S))
        else:
            return hasil(TailString(S))

print(f"{hasil(user_input)} Milyar")
