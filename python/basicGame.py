import random

kullaniciAdiKayitli = ""
kullaniciCinsiyetKayitli = ""
kullaniciYasKayitli = 0
kullaniciSifresiKayitli = ""
gun = 1
can = 100
barisCan = 30
trumpCan = 5000
vampirCan = 70

barisAtak = 10
trumpAtak = 90
vampirAtak = 70

print("Dunyanın en zor oyununa hosgeldiniz")
while True:
    print("Giris yapmak için 1 , kayıt olmak için 2 ye basınız")
    secim = int(input())
    if secim == 1 :
        print("Kullanıcı adini ve şifrenizi giriniz")
        kullaniciAdi = input()
        kullaniciSifresi = input()
        if kullaniciAdiKayitli == "" or kullaniciSifresiKayitli =="" :
            print("Kayıtlı kullanıcı bulunamadı")
        elif kullaniciAdi == kullaniciAdiKayitli and kullaniciSifresi == kullaniciSifresiKayitli:
            print("Giriş yapıldı")
            if kullaniciCinsiyetKayitli == "E":
                hitap = "Lord"
            elif kullaniciCinsiyetKayitli == "K":
                hitap = "Leydi"
            if kullaniciYasKayitli <= 15:
                lakap = "bebe"
            elif kullaniciYasKayitli > 15 and kullaniciYasKayitli < 30:
                lakap = "Usta"
            elif kullaniciYasKayitli >= 30:
                lakap = "Rehber"
            while True:
                if can <= 0:
                    print("Herkes öldürür sevdiğini , GAME OVER")
                    break
                print("Merhaba " + kullaniciAdiKayitli +" " + hitap +" "+ lakap)
                print("Bugun %d inci gün şuan ki canınız %d dir."%(gun,can))
                print(" Yapmak istediğiniz eylemi seçiniz")
                print(" 1 : Av 2:Keşif 3: Uyumak")
                secimGunluk = int(input())
                if secimGunluk == 1:
                    print("Hangi canlıya saldırmak istersin")
                    print("1- Barış 2- Trump 3- Vampir")
                    secimAv = int(input())
                    if secimAv == 1 and barisCan > 0:
                        print("Dikkatli ol , saldırıya geciyorsun")
                        print(" Tokat Tekme Terlik Ok Katana Oklava vb")
                        sucAleti = input()
                        barisCan -= len(sucAleti) * 4
                        if barisCan > 0:
                            barisCan = random.randint(0,101)
                            can -= barisCan
                            print(" Barış canlısının canı ",barisCan , " kaldı")
                        if barisCan <= 0:
                            print("Barış mefta oldu , gözün aydın ")
                    elif secimAv == 1 and barisCan <0:
                        print("Yeter vurma ayol")

                    elif secimAv == 2 and trumpCan > 0:
                        print("Karşında Trump, Adam ol ")
                        print(" S400, YerliSavaşUcağı, YerliVeMilli2023BorBombasi")
                        sucAleti = input()
                        trumpCan -= len(sucAleti) * 50
                        if trumpCan > 0:
                            trumpAtak = random.randint(40,200)
                            can -= trumpAtak
                            print(" Trump reisin canı " , trumpCan , " kaldı")
                        if trumpCan <= 0:
                            print("Bir Trump ölür bin trump doğar, ama sonra ")
                    elif secimAv == 2 and trumpCan < 0:
                        print("Allah gani gani rahmet eylesin , amin ")

                    elif secimAv == 3 and vampirCan > 0:
                        print("Kimsesiz gecelerinin ışığıyım ")
                        print(" sarımsak,gümüşKazık,kurtadam,kutsalsu")
                        sucAleti = input()
                        vampirCan -= len(sucAleti) * 3
                        if vampirCan > 0:
                            vampirAtak = random.randint(10,90)
                            can -= vampirAtak
                            vampirCan += vampirAtak / 2
                            print(" Dracula " , vampirCan , " kaldı")
                        if vampirCan <= 0:
                            print("Kuş öldü beybisi. ")
                    elif secimAv == 3 and vampirCan < 0:
                        print(" İyi bilirdik .  ")

                if secimGunluk == 2:
                    kesif = random.randint(0,100)
                    if kesif % 2 == 0:
                        print("Petrol buldun gucune guc kattın")
                        can += random.randint(0,200)
                    if kesif % 2 == 1:
                        print("Mayına bastın sakat kaldın g.o krdş")
                        can -= random.randint(0,200)
                        if  can <= 0:
                            print("Ölmekte öldürmekte ekip işi")
                        else:
                            print("Ey Mayın , Sen kimsin ! ")
                if secimGunluk == 3:
                    can += 30
                    gun +=1


    elif secim == 2:
        for i in range(3):
            print("Kayıt olmak için kullanıcı adı giriniz")
            kullaniciAdiKayitli = input()
            print("Kullanıcı şifresini giriniz")
            kullaniciSifresiKayitli = input()
            print("Cinsiyet ve yas giriniz")
            kullaniciCinsiyetKayitli = input()
            kullaniciYasKayitli = int(input())
            if kullaniciAdiKayitli == "" or kullaniciSifresiKayitli == "" or kullaniciYasKayitli <= 0 or kullaniciCinsiyetKayitli == "":
                print(" Hatalı kayıt yaptınız lütfen tekrar deneyin")
                kullaniciAdiKayitli = ""
                kullaniciCinsiyetKayitli = ""
                kullaniciYasKayitli = 0
                kullaniciSifresiKayitli = ""
            else:
                break

