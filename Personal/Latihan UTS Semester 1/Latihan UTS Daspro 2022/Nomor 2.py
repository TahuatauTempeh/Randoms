# DEFINISI DAN SPESIFIKASI
# DiskonUsia : int [1...31], int [1...12], int [9999], int [1...31], int [1...12], int [9999] -> str, int >0
#   {DiskonUsia(d1, m1, y1, d2, m2, y2) adalah fungsi untuk menentukan apakah seseorang mendapatkan diskon berdasarkan variabel tersebut}

#DEFINISI DAN SPESIFIKASI FUNGSI PERANTARA
# # months : int [1...12] -> int [1...335]
#   {months(m) adalah fungsi untuk menhitung total hari dalam sekian bulan}
# total_hari : int [1...31], int [1...12], int [9999], int [1...31], int [1...12], int [9999] -> int > 0
#   {total_hari(d1,m1,y1,d2,y2,m2) adalah fungsi untuk menghitung total hari dari d1, m1, y1, d2, m2, y2}
# Dll


# REALISASI
def months(m) :
    if m == 1 :
       return 1
    elif m == 2 :
       return 32
    elif m == 3 :
       return 60
    elif m == 4 :
       return 91
    elif m == 5 :
       return 121
    elif m == 6 :
       return 152
    elif m == 7 :
       return 182
    elif m == 8 :
       return 213
    elif m == 9 :
       return 244
    elif m == 10 :
       return 274
    elif m == 11 :
       return 305
    elif m == 12 :
       return 335

def total_hari(d, m, y):
    return d + months(m) + (y * 365)

def selisih(d1, m1, y1, d2, m2, y2):
    total_hari_1 = total_hari(d1, m1, y1)
    total_hari_2 = total_hari(d2, m2, y2)

    return total_hari_2 - total_hari_1

def DiskonUsia(d1, m1, y1, d2, m2, y2):
    umur_hari = selisih(d1, m1, y1, d2, m2, y2)

    if umur_hari < 365 * 2:
        return "Infant", 75
    elif 365 * 2 < umur_hari <= 365 * 12:
        return "Child", 25
    else:
        return "Adult", 0

# APLIKASI
print(DiskonUsia(20,8,2009,8,1,2010))

# print(DiskonUsia(1,1,2020,2,3,2040))
