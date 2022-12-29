pi = 22/7

def luas_persegi(sisi=0):
    """
    Menghitung Luas persegi
    """
    return (sisi*sisi)

def luas_persegi_panjang(panjang=0,lebar=0):
    """
    Menghitung Luas Persegi Panjang
    """
    return (panjang*lebar)

def luas_segitiga(alas=0,tinggi=0):
    """
    Menghitung Luas Segitiga
    """
    return (alas*tinggi/2)

def luas_lingkaran(ruas=0):
    """
    Menghitung Luas Lingkaran
    """
    return (pi*(ruas**2))

def luas_jajargenjang(alas=0,tinggi=0):
    """
    Menghitung Luas Jajar Genjang
    """
    return (alas*tinggi)

def luas_belahketupat(diagonal1=0,diagonal2=0):
    """
    Menghitung Luas Belah Ketupat
    """
    return ((diagonal1*diagonal2)/2)


def luas_layang_layang(diagonal1=0,diagonal2=0):
    """
    Menghitung Luas Layang-Layang
    """
    return ((diagonal1*diagonal2)/2)


def luas_trapesium(sisi_a=0,sisi_b=0,tinggi=0):
    """
    Menghitung Luas Trapesium
    """
    return (((sisi_a+sisi_b)*tinggi)/2)