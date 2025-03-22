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

