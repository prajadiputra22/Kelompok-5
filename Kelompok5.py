
from tugas import *

while True :

    print('''\nAPLIKASI MENGHITUNG LUAS BANGUN DATAR DAN RUANG
KELOMPOK 5

1. Menghitung luas bangun datar
2. Menghitung luas bangun ruang
0. Exit''')

    opt = int(input('\nPilih nomor : '))

    if opt == 1 :
        while True :
            print('''\nMENGHITUNG LUAS BANGUN DATAR
1. Persegi
2. Persegi panjang
3. Segitiga
4. Lingkaran
5. Jajar genjang
6. Belah ketupat
7. Layang layang 
8. Trapesium
0. Exit''')

            opt = int(input('\nPilih luas bangun datar : '))

            if opt == 1 :
                sisi = int(input('\nMasukan panjang sisi : '))
                luas = luas_persegi(sisi)
                print('Luas persegi adalah  : ',luas)

            elif opt == 2 :
                panjang = int(input('\nMasukan panjang : '))
                lebar = int(input('Masukan Lebar   : '))
                luas = luas_persegi_panjang(panjang,lebar)
                print('Luas persegi panjang adalah : ',luas)
                

            elif opt == 3 :
                tinggi = int(input('\nMasukan tinggi : '))
                alas = int(input('Masukan alas   : '))
                luas = luas_segitiga(tinggi,alas)
                print('\nLuas segitiga adalah ',luas)
                

            elif opt == 4 :
                ruas = int(input('\nMasukan jari-jari lingkaran : '))
                luas = luas_lingkaran(ruas)
                print('Luas lingkaran adalah %0.2f '%luas)
                
            elif opt == 5 :
                tinggi = int(input('\nMasukan tinggi : '))
                alas = int(input('Masukan alas   : '))
                luas = luas_jajargenjang(tinggi,alas)
                print('Luas Jajar genjang adalah :',luas)

            elif opt == 6 :
                diagonal1 = int(input('\nMasukan diagonal 1 : '))
                diagonal2 = int(input('Masukan diagonal 2 : '))
                luas = luas_belahketupat(diagonal1,diagonal2)
                print('Luas belah ketupat adalah : ',luas)

            elif opt == 7 :
                diagonal1 = int(input('\nMasukan diagonal 1 : '))
                diagonal2 = int(input('Masukan diagonal 2 : '))
                luas = luas_belahketupat(diagonal1,diagonal2)
                print('Luas layang-layang adalah : ',luas)

            elif opt == 8 :
                sisi_a = int(input('\nMasukan sisi atas : '))
                sisi_b = int(input('Masukan sisi bawah : '))
                tinggi = int(input('Masukan tinggi : '))
                luas = luas_trapesium(sisi_a,sisi_b,tinggi)
                print('Luas trapesium adalah : ',luas)

            elif opt == 0 :
                exit = input('\nApakah anda ingin keluar? (y/n) :')
                if exit == 'y' :
                    print('Terima kasih telah menggunakan program ini'.upper())
                    break
                else : continue

    elif opt == 2 :
        while True :
            print('''\nMENGHITUNG LUAS BANGUN RUANG
1. Balok
2. Kubus
3. Kerucut
4. Prisma
5. Limas
6. Tabung
7. Bola
0. Exit''')
            opt = int(input('\nPilih : '))
            if opt == 1 :
                panjang = int(input('\nMasukan panjang : '))
                lebar = int(input('Masukan Lebar : '))
                tinggi = int(input('Masukan tinggi : '))
                luas = luas_balok(panjang,lebar,tinggi)
                print('Luas Balok adalah ',luas)
            elif opt == 2:
                pass
            elif opt == 3:
                pass
            elif opt == 4:
                pass
            elif opt == 5:
                pass
            elif opt == 6:
                pass
            elif opt == 7:
                pass
            elif opt == 8:
                pass
            elif opt == 0:
                exit = input('\nApakah anda ingin keluar? (y/n) :')
                if exit == 'y':
                    print('Terima kasih telah menggunakan program ini'.upper())
                    break

    elif opt == 0 :
        exit = input('\nApakah anda ingin keluar? (y/n) :')
        if exit == 'y' :
            print('Terima kasih telah menggunakan program ini'.upper())
            break
        else : continue
    
    else :
        print('ERROR - MOHON MASUKAN NOMOR YANG TERDAPAT DI MENU')


