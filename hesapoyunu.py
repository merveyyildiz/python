""""
Kayıt olmak için 1 , Giriş için 2
Puan tablosu için 3 -> ekrana bassın yeter
 kullanıcılar kayıt olacak
 Kullanıcı giris yapacak
 random sayılarla 3 soru sorulcak
 4+5 = 9 -> 3 puan  6 + 2 = 8 -> 3puan
3 + 1 = 4 -> 3 puan hatalı olursa 0 puan
 3 sefer sonra oyun bitcek
  kullanıcı adı ile puanlar saklancak

Giriş yapmak için 1 kayıt 2 puanlar 3
2
Kullanıcı adı - şifre
Giriş yapmak için 1 kayıt 2 puanlar 3
1
4 + 5 -> 9 = +3
5 +6 -> 123 = 0
123 + 2 = 125 = +3
Giriş yapmak için 1 kayıt 2 puanlar 3
3
Kullanıcı Puan
"""
import random
userTable = {}
pointTable = {}
while True:
    print("Giriş 1 kayıt 2 puan 3 kapat 4")
    secenek = int(input())
    if secenek == 1:
        print("Kullanıcı adı")
        kullaniciAdi = input()
        print("Şifre")
        sifre = input()
        auth = userTable.get(kullaniciAdi)
        if auth !="None" and auth == sifre:
            print("Başladık")
            puan = 0
            for x in range(3):
                numberOne = random.randint(0,10)
                numberTwo = random.randint(0,10)
                print("%d + %d ="%(numberOne,numberTwo))
                toplam = int(input())
                if toplam == (numberOne + numberTwo):
                    puan += 3
            eskiPuan = pointTable.get(kullaniciAdi)
            yeniPuan = eskiPuan + puan
            print("Yeni puan = %d"%(yeniPuan))
            pointTable.update({kullaniciAdi:yeniPuan})
    elif secenek == 2:
        print("Kullanıcı adı")
        kullaniciAdi = input()
        print("Şifre")
        sifre = input()
        user = {kullaniciAdi: sifre}
        userTable.update(user)
        userPoint = {kullaniciAdi:0}
        pointTable.update(userPoint)
        print("Kayıt Başarılı")
    elif secenek == 3:
        for name,point in pointTable.items():
            print("İsim %s Puan %d"%(name,point))
    elif secenek == 4:
        print("Gorusuruz haci")
        break