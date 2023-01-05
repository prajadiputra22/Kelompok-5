
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

            opt = int(input('\nPilih : '))

            if opt == 1 :
                sisi = int(input('\nMasukan panjang sisi : '))
                luas = luas_persegi(sisi)
                print('Luas persegi adalah ',luas)

            elif opt == 2 :
                panjang = int(input('\nMasukan panjang : '))
                lebar = int(input('Masukan Lebar   : '))
                luas = luas_persegi_panjang(panjang,lebar)
                print('Luas persegi panjang adalah ',luas)
                

            elif opt == 3 :
                tinggi = int(input('\nMasukan tinggi : '))
                alas = int(input('Masukan alas   : '))
                luas = luas_segitiga(tinggi,alas)
                print('Luas segitiga adalah ',luas)
                

            elif opt == 4 :
                ruas = int(input('\nMasukan jari-jari lingkaran : '))
                luas = luas_lingkaran(ruas)
                print('Luas lingkaran adalah %0.2f '%luas)
                
            elif opt == 5 :
                tinggi = int(input('\nMasukan tinggi : '))
                alas = int(input('Masukan alas   : '))
                luas = luas_jajargenjang(tinggi,alas)
                print('Luas Jajar genjang adalah ',luas)

            elif opt == 6 :
                diagonal1 = int(input('\nMasukan diagonal 1 : '))
                diagonal2 = int(input('Masukan diagonal 2 : '))
                luas = luas_belahketupat(diagonal1,diagonal2)
                print('Luas belah ketupat adalah ',luas)

            elif opt == 7 :
                diagonal1 = int(input('\nMasukan diagonal 1 : '))
                diagonal2 = int(input('Masukan diagonal 2 : '))
                luas = luas_belahketupat(diagonal1,diagonal2)
                print('Luas layang-layang adalah ',luas)

            elif opt == 8 :
                sisi_a = int(input('\nMasukan sisi atas : '))
                sisi_b = int(input('Masukan sisi bawah : '))
                tinggi = int(input('Masukan tinggi : '))
                luas = luas_trapesium(sisi_a,sisi_b,tinggi)
                print('Luas trapesium adalah ',luas)

            elif opt == 0 :
                    break

    elif opt == 2 :
        while True :
            print('''\nMENGHITUNG LUAS BANGUN RUANG
1. Kubus
2. Balok
3. Kerucut
4. Prisma segitiga
5. Tabung
6. Bola
7. Limas Segitiga
8. Limas Segiempat
0. Exit''')
            opt = int(input('\nPilih : '))
            if opt == 1 :
                sisi = int(input('\nMasukan panjang sisi : '))
                luas = luas_kubus(sisi)
                print('Luas kubus adalah ',luas)

            elif opt == 2:
                panjang = int(input('\nMasukan panjang : '))
                lebar = int(input('Masukan Lebar : '))
                tinggi = int(input('Masukan tinggi : '))
                luas = luas_balok(panjang,lebar,tinggi)
                print('Luas balok adalah  ',luas)

            elif opt == 3:
                ruas = int(input("Masukkan jari-jari : "))
                sisi_miring = int(input("Masukkan sisi miring : "))
                luas = luas_kerucut(ruas, sisi_miring)
                print('Luas kerucut adalah  %0.2f '%luas)
            
            elif opt == 4:
                alas = int(input('\nMasukan alas : '))
                tinggi = int(input('Masukan tinggi alas : '))
                tinggi_prisma = int(input('Masukan tinggi prisma : '))
                luas = luas_prisma_segitiga(alas, tinggi, tinggi_prisma)
                print('Luas prisma segitiga adalah ',luas)

            elif opt == 5:
                ruas = int(input('\nMasukan jari-jari : '))
                tinggi = int(input('Masukan tinggi : '))
                luas = luas_tabung(ruas, tinggi)
                print('Luas tabung adalah %0.2f '%luas)

            elif opt == 6:
                ruas = int(input('\nMasukan ruas : '))
                luas = luas_bola(ruas)
                print('Luas bola adalah  %0.2f'%luas)

            elif opt == 7:
                luas_sisi_1 = int(input('\nMasukan Luas sisi 1 : '))
                luas_sisi_2 = int(input('Masukan Luas sisi 2 : '))
                luas_sisi_3 = int(input('Masukan Luas sisi 3 : '))
                luas_sisi_4 = int(input('Masukan Luas sisi 4 : '))
                luas = luas_limas_segitiga(luas_sisi_1,luas_sisi_2,luas_sisi_3,luas_sisi_4)
                print('Luas limas segitiga adalah  ',luas)

            elif opt == 8:
                luas_sisi_1 = int(input('\nMasukan Luas sisi 1 : '))
                luas_sisi_2 = int(input('Masukan Luas sisi 2 : '))
                luas_sisi_3 = int(input('Masukan Luas sisi 3 : '))
                luas_sisi_4 = int(input('Masukan Luas sisi 4 : '))
                luas_sisi_5 = int(input('Masukan Luas sisi 5 : '))
                luas = luas_limas_segiempat(luas_sisi_1,luas_sisi_2,luas_sisi_3,luas_sisi_4,luas_sisi_5)
                print('Luas limas segiempat adalah ',luas)
            
            elif opt == 0:
                    break

    elif opt == 0 :
        exit = input('\nApakah anda ingin keluar? (y/n) :')
        if exit == 'y' :
            print('Terima kasih telah menggunakan program ini'.upper())
            break
        else : continue
    
    else :
        print('ERROR - MOHON MASUKAN NOMOR YANG TERDAPAT DI MENU')


