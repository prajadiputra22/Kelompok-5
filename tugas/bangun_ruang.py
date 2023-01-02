pi = 22/7

#lUAS kUBUS
def luas_kubus(sisi) :
    return sisi * 6

#lUAS BALOK
def luas_balok(panjang, lebar, tinggi) :
    return panjang*lebar*tinggi

#LUAS KERUCUT
def luas_kerucut(ruas, sisi_miring):
    luas_alas = pi * ruas * ruas
    luas_selimut = pi * ruas * sisi_miring
    return luas_alas + luas_selimut

def luas_prisma_segitiga(alas, tinggi, tinggi_prisma):
    luas_alas = alas * tinggi / 2
    luas_selimut = luas_alas * tinggi_prisma
    return 2 * luas_alas + luas_selimut

#lUAS TABUNG
def luas_tabung(ruas, tinggi) :
    return (2 * pi * ruas * ruas) + (2 * pi * ruas * tinggi)
