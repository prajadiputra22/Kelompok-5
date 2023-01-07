
pi = 22/7

# RUMUS lUAS kUBUS
def luas_kubus(sisi) :
    return sisi * 6

# RUMUS lUAS BALOK
def luas_balok(panjang, lebar, tinggi) :
    return panjang*lebar*tinggi

# RUMUS LUAS KERUCUT
def luas_kerucut(ruas, sisi_miring):
    luas_alas = pi * ruas * ruas
    luas_selimut = pi * ruas * sisi_miring
    return luas_alas + luas_selimut

# RUMUS LUAS PRISMA SEGITGA
def luas_prisma_segitiga(alas, tinggi, tinggi_prisma):
    luas_alas = alas * tinggi / 2
    luas_selimut = luas_alas * tinggi_prisma
    return 2 * luas_alas + luas_selimut

# RUMUS lUAS TABUNG
def luas_tabung(ruas, tinggi) :
    return (2 * pi * ruas * ruas) + (2 * pi * ruas * tinggi)

# RUMUS lUAS BOLA
def luas_bola(ruas=0):
    return (4*pi*ruas*ruas)

# RUMUS lUAS LIMAS SEGITIGA
def luas_limas_segitiga(alas=0,tinggi=0):
    return ((.5*alas*tinggi)+((alas*tinggi*.5)*3))

# RUMUS lUAS LIMAS SEGIEMPAT
def luas_limas_segiempat(luas_alas=0,alas=0,tinggi=0):
    return (luas_alas+((alas*tinggi*.5)*4))
