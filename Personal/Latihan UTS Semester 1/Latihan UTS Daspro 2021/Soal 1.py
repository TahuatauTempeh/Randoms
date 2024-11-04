# DEFINISI DAN SPESIFIKASI
# DateofBirth : int[1...31], int[1...12], int > 1900 -> str
#   {DateofBirth(d,m,y) adalah fungsi yang membentuk sebuah tanggal, kemudian memberikan keluaran berupa string tanggal lahir.}
# NameofMonths : int [1...12] -> str
#   {NameofMonths(m) adalah fungsi untuk memunculkan nama bulan dalam bentuk alfabet dari bentuk angka.}

# REALISASI
def NameofMonths(m) :
    if m == 1 :
        return "January"
    elif m == 2 :
        return "February"
    elif m == 3 :
        return "March"
    elif m == 4 :
        return "April"
    elif m == 5 :
        return "May"
    elif m == 6 :
        return "June"
    elif m == 7 :
        return "July"
    elif m == 8 :
        return "August"
    elif m == 9 :
        return "September"
    elif m == 10 :
        return "Octobre"
    elif m == 11 :
        return "Novembre"
    elif m == 12 :
        return "Decembre"

def DateofBirth(d,m,y) :
    return f"{d} {NameofMonths(m)} {y}"

# APLIKASI
print(DateofBirth(2,3,2009))
print(DateofBirth(10,12,2010))
print(DateofBirth(9,12,2001))
