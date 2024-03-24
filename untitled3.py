# -*- coding: utf-8 -*-
"""
Created on Sat May 21 00:52:19 2022

@author: 90535
"""
import sqlite3                                                     # veritabanı başlangıcı#
baglanti=sqlite3.connect("uye.db")
islem = baglanti.cursor()
baglanti.commit()
table = islem.execute("create table if not exists uye (isim text, soyisim text, sifre int)")

def veri_ekle2():
    isim = input("Adınızı girin:")
    soyisim = input("Soyadınızı girin:")
    sifre = int(input("Şifrenizi  girin:"))
    islem.execute("insert into uye values (?,?,?)",(isim,soyisim,sifre))
    baglanti.commit()
veri_ekle2()
baglanti.close()                                                    #veritabanı bitişi#
class basla():                                          #sınıf başlangıcı#
    def start(self):
        print("siparişe başlıyoruz")
    def stop(self):
        print("sipariş sonlandırılıyor")               #sınıf bitiş#
basla1=basla()
basla2=basla()        
def bdn():#fonksiyon#
    print("Renk ve bedenleri görmek için e ye girmeden devam tmek için a ya  basın")
    sec=input("Seçim:")
    if sec=='e':
        print("Kazakta mavi renk için:S , M")
        print("Elbisede yeşil renk için:S , L")
        print("Pantolonda siyah renk için:L , XL bedenleri vardır")
        print("Diğer mevcut renkler ve kıyafetler için tüm bedenler vardır")
   

def blg(): #fonksiyon#

 print("1-Kazak,2-Elbise,-3Etek,4-Pantolon")
 giris=input("bilgilendirmeye girmek için g girmeden devam etmek  seçin:")
 if giris=='g':
  bilgi={"kazak":"kış için iyidir, yünlü ve düz olarak elimizde 2 çeşidi vardır",
       "elbise":"özel günler için uygundur,diz üstü ve diz altı seçeneklerimiz mevcuttur",
       "etek":"yazın vazgeçilmez giysisi,her türlü rengi ve bedeni mevcuttur",
       "pantolon":"kot,keten,kumaş seçenekleri ve her bedene uygun pantolon mevcuttur. "}#SÖZLÜK YAPISI#
 for i in bilgi.items():
     print(i[0]+" "+i[1])
 
     
print("1-Kazak,2-Elbise,-3Etek,4-Pantolon") 
   
print("Sipariş bilgilerini girmek için 5 e basın")
fiyatliste=['50','75','35','150']#LİSTE YAPISI#
cikis='N'
toplam=0
sayac=0
while cikis!='Y':
    
   
   basla1.start()
   secim=int(input("seçim yapın:"))
   if secim==1:
     print("kazak seçtiniz fiyatı:",fiyatliste[0])
     toplam+=50
     sayac+=1
     bdn()
     blg()
   elif secim==2:
    print("elbise seçtiniz fiyatı:",fiyatliste[1])
    toplam+=75
    sayac+=1
    bdn()
    blg()
   elif secim==3:
     print("etek seçtin fiyatı:",fiyatliste[2])
     toplam+=35
     sayac+=1
     bdn()
     blg()
   elif secim==4:
    print("pantolon seçtiniz fiyatı:",fiyatliste[3])
    toplam+=150
    sayac+=1
    bdn()
    blg()
   elif secim>5:
       print("Yanlış seçim yaptınız!!")
       
       
   else:
    print("Alışverişin toplam tutarı:",toplam) 
    print("Sipariş bilgilerine geçiliyor...") 
    print("Sipariş verdiğiniz şehir Hatay,Adana,Mersin,Rize,Trabzon,Artvin,Diyarbakır,Hakkari ise belirtiniz değil ise diğer yazınız.")
    print(" Ayrıca yurtdışı için Avusturya,Bulgaristan,Gürcistana gönderimimiz vardır bu ülkeler dışında ise farklı yazınız. ")
    şehir={"Hatay":["Kargo ücreti mesafeden dolayı 20 tl dir"],
           "Mersin":["Kargo ücreti mesafeden dolayı 20 tl dir"],
           "Adana":["Kargo ücreti mesafeden dolayı 20 tl dir"],
           "Rize":["Kargo ücreti 25 tl dir"],
           "Trabzon":["Kargo ücreti mesafeden dolayı 25 tl dir"],
           "Artvin":["Kargo ücreti mesafeden dolayı 25 tl dir"],
           "Diyarbakır":["Kargo ücreti 30 tl dir"],
           "Hakkari":["Kargo ücreti mesafeden dolayı 30 tl dir"],
           "diğer":["kargo bedava hayırlı olsun"],
          "Avusturya":["Kargo ücreti 10£"],
          "Gürcistan":["KArgo ücreti 20 laridir"],
          "Bulgaristan":["Kargo ücreti 25 leva dır"],
          "farklı":["Maalesef ülkenize kargo hizmetimiz yoktur"]}#SÖZLÜK YAPISI#
    yer=input("sipariş şehrini giriniz:")
    print("{} için:".format(yer))
    for i in (şehir[yer]):
        print(i)
    
    
    print("Sipariş bilgilerini girerken lütfen dikkat ediniz!") 
    print("Sayı yerine harf veya harf yerine sayı girişi yaparsanız sizi seçim menüsüne geri atacaktır.")
          
    adres=input("adres giriniz:")
    try:                                                 #try-except başlangıcı#
     telefon=int(input("telefon giriniz:"))      
    except:                                      
     print("Lütfen sadece sayı girin!")          
     continue                                    
    try:
     kartno=int(input("kartno giriniz:"))        
    except:
     print("Lütfen sadece sayı girin!")
     continue
    try:   
     cvv=int(input("cvv giriniz:"))
    except:
     print("Lütfen sadece sayı girin!")
     continue
    try:
     karttarih=int(input("karttarih giriniz:"))
    except:
     print("Lütfen sadece sayı girin!")
     continue                                             #try-except bitişi#
    print("SIPARISINIZ ALINDI TESEKKURLER :)\n")
    print("Çıkış yapıp gün sonu raporunu almak icin Y gir, devam etmek icin N gir\n ")
    cikis=input("yapmak istediğini işlemi girin:")
    if cikis=='Y':
        basla2.stop()
        print("çıkış yapılıyor")
        print("alışveriş sonunda alınan kıyafet sayısı:",sayac)
        print("Harcanan para:",toplam)
        print("Hayırlı olsun yine bekleriz :)")
        break
    elif cikis=='D':
        print("devam ediliyor")