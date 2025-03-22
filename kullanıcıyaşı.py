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


