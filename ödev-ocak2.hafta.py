#tek-çift
sayi = int(input("Bir sayı girin: "))

if sayi % 2 == 0:
    print(f"Girdiğiniz Sayı: {sayi} -> bir çift sayıdır.")
else:
    print(f"Girdiğiniz Sayı: {sayi} -> bir tek sayıdır.")



#yaş
yaş = int(input("Bir yaş giriniz: "))

if yaş<0:
    print(f"Geçersiz Yaş girdiniz !")
elif yaş>=0 and yaş<=12:
    print(f"Çocuk")
elif yaş>=13 and yaş<=19:
    print(f"Genç")
elif yaş>=20 and yaş<=59:
    print(f"Yetişkin")
else :
    print("Yaşlı")


#not
sayı = int(input("Notunuzu Giriniz: "))

if sayı >=90 and sayı <=100 :
    print(f"Notunuz A")
elif sayı >=80 and sayı <=89 :
    print(f"Notunuz B")
elif sayı >=70 and sayı <=79 :
    print(f"Notunuz C ")
elif sayı >=60 and sayı <=69 :
    print(f"Notunuz D")
elif sayı>=0 and sayı<=50 :
   print(f"Notunuz F")
else:
    print(f"Girdiğiniz sayı doğru bir not değil.Lütfen doğru bir not aralığı giriniz !")
