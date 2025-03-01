def asal_sayi_kontrol():
    while True:
        giris = input("Bir sayı girin (Çıkmak için 'q' tuşuna basın): ")
        
        if giris.lower() == 'q':
            print("Programdan çıkılıyor...")
            break
        
        if not giris.isdigit():
            print("Lütfen geçerli bir pozitif sayı girin!")
            continue
        
        sayi = int(giris)
        
        if sayi < 2:
            print(f"{sayi} bir asal sayı değildir.")
            continue
        
        for i in range(2, int(sayi ** 0.5) + 1):
            if sayi % i == 0:
                print(f"{sayi} Bir asal sayı değildir! Asal sayı, sadece kendisine ve 1’e bölünebilen 1’den büyük pozitif sayılardır.")
                break
        else:
            print(f"{sayi} bir asal sayıdır.")

asal_sayi_kontrol()
