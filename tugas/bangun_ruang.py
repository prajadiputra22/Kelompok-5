pi=22/7

def luas_kubus(sisi=0):
    """
    Menghitung Luas Kubus
    """
    return (sisi * 6)

def luas_balok(panjang=0, lebar=0, tinggi=0):
    """
    Menghitung Luas Balok
    """
    return panjang*lebar*tinggi

def luas_kerucut(ruas=0, sisi_miring=0):
    """
    Menghitung Luas Kerucut
    """
    luas_alas = pi * ruas * ruas
    luas_selimut = pi * ruas * sisi_miring
    return (luas_alas + luas_selimut)

def luas_prisma_segitiga(alas=0, tinggi=0, tinggi_prisma=0):
    """
    Menghitung Luas Prismas Segitiga
    """
    luas_alas = alas * tinggi / 2
    luas_selimut = luas_alas * tinggi_prisma
    return (2 * luas_alas + luas_selimut)

def luas_tabung(ruas=0, tinggi=0):
    """
    Menghitung Luas tabung
    """
    return ((2 * pi * ruas * ruas) + (2 * pi * ruas * tinggi))

def luas_bola(ruas=0):
    """
    Menghitung luas bola
    """
    return (4*pi*ruas*ruas)

def luas_limas_segitiga(luas_sisi_1 = 0, luas_sisi_2 = 0, luas_sisi_3 = 0, luas_sisi_4 = 0):
    """
    Menghitung Limas Segi Empat
    """
    return (luas_sisi_1 + luas_sisi_2 + luas_sisi_3 + luas_sisi_4)

def luas_limas_segiempat(luas_sisi_1=0,luas_sisi_2=0,luas_sisi_3=0,luas_sisi_4=0,luas_sisi_5=0):
    """
    Menghitung Luas Limas Segi Empat
    """
    return (luas_sisi_1+luas_sisi_2+luas_sisi_3+luas_sisi_4+luas_sisi_5)