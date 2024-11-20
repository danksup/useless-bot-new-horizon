#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
def makePN(A, PN) : 
    return [A, PN]

#DEFINISI DAN SPESIFIKASI SELEKTOR
#Akar : PohonN-ner tidak kosong → ELemen
# { Akar(P) adalah Akar dari P. Jika P adalah (A, PN) = Akar(P) adalah A }
def akar(PN) :
    return PN[0]

#Anak : PohonN-ner tidak kosong → List of PohonN-ner
#{ Anak(P) adalah List of pbhon N-ner yang merupakan anak-anak (sub phon)
# dari P. Jika P adalah (A, PN) = Anak (P) adalah PN }
def anak(PN) :
    return PN[1]

#DEFINISI DAN SPESIFIKASI PREDIKAT
#IsTreeNEmpty : PohonN-ner → boolean
# {IsTreeNEmpty(PN) true jika PN kosong : ) }
def isTreeNEmpty (PN) :
    return PN == []

#IsOneELmt : PohonN-ner → boolean
#{IsOneELmt(PN) true jika PN hanya terdiri dari Akar }
def isOneElmt (PN) :
    return (isTreeNEmpty (PN) == False) and (isTreeNEmpty (anak(PN)) == True)

#N6NELmt : PohonN-ner → integer ≥ 0
# {NbNELmt(P) memberikan banyaknya node dari pohon P :
# Basis 1: NbNELmt ((A)|) = 1
# Rekurens : NbNELmt ((A, PN)) = 1 + NbELmt (PN) }
def NbNElmt (PN) :
# Basis: Jika pohon kosong
    if isTreeNEmpty(PN) :
        return 0
# Jika hanya ada satu elemen (akar saja)
    if isOneElmt (PN) :
        return 1
# Hitung 1 untuk akar, dan rekursif pada setiap anak pohon
# Tanpa menggunakan Loop, kita memanggil fungsi untuk setiap anak secara rekursif
# Pertama pada anak pertama
    return 1 + NbNElmt (anak(PN) [0]) + NbNElmtChild(anak(PN) [1:])

# Fungsi tambahan untuk menghitung jumlah elemen pada sisa anak-anak
def NbNElmtChild(PN):
# Basis: Jika tidak ada anak
    if isTreeNEmpty(PN) :
        return 0
# Jika ada anak, rekursif pada anak pertama dan sisa anak-anak
    return NbNElmt (PN[0]) + NbNElmtChild(PN[1:])

# Fungsi tambahan untuk menghitung jumlah elemen pada sisa anak-anak
def NbNElmtChild(PN) :
# Basis: Jika tidak ada anak
    if isTreeNEmpty(PN) :
        return 0
# Jika ada anak, rekursif pada anak pertama dan sisa anak-anak
    return NbNElmt (PN[0]) + NbNElmtChild(PN[1:])

def NbNDaun (PN) :
# Basis: Jika pohon kosong
    if isTreeNEmpty(PN) :
        return 0
# Jika pohon adalah daun (anak kosong)
    if isOneElmt(PN) and isTreeNEmpty(anak(PN)) :
        return 1
# Rekursi pada akar dan anak-anak
    return NbNDaunChild(anak(PN))

# Fungsi tambahan untuk menghitung jumlah daun pada sisa anak-anak
def NbNDaunChild(PN) :
# Basis: Jika tidak ada anak
    if isTreeNEmpty(PN):
        return 0
# Jika ada anak, rekursif pada anak pertama dan sisa anak-anak
    return NbNDaun(PN[0]) + NbNDaunChild(PN[1:])

#APLIKASI
T = makePN(2, [])
print (makePN(2, []) )
print (isTreeNEmpty (T) )
print (isOneElmt (T) )
T2 = makePN('A', [makePN('B', [makePN('D', []),makePN('E', []), makePN( 'F', [])]), makePN('G', [makePN('G', []) ,makePN('H', [makePN('I', [])])])])
print (T2)
print (NbNElmt (T2))
print (NbNDaun (T2))