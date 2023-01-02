pi = 22/7

#LUAS PERSEGI
def luas_persegi(sisi=0):
    return (sisi*sisi)

#LUAS PERSEGI PANJANG
def luas_persegi_panjang(panjang=0,lebar=0):
    return (panjang*lebar)

#LUAS SEGITIGA
def luas_segitiga(alas=0,tinggi=0):
    return (alas*tinggi/2)

#LUAS LINGKARAN
def luas_lingkaran(ruas=0):
    return (pi*(ruas**2))

#LUAS JAJARGENJANG
def luas_jajargenjang(alas=0,tinggi=0):
    return (alas*tinggi)

#LUAS BELAH KETUPAT
def luas_belahketupat(diagonal1=0,diagonal2=0):
    return ((diagonal1*diagonal2)/2)

#LUAS LAYANG-LAYANG
def luas_layang_layang(diagonal1=0,diagonal2=0):
    return ((diagonal1*diagonal2)/2)

#LUAS TRAPESIUM
def luas_trapesium(sisi_a=0,sisi_b=0,tinggi=0):
    return (((sisi_a+sisi_b)*tinggi)/2)
