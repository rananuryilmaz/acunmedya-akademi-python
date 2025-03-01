def hesap_makinesi():
    while True:
        sayi1 = input("Birinci sayıyı giriniz (Çıkmak için 'q' tuşuna basın): ")
        if sayi1.lower() == 'q':
            print("Programdan çıkılıyor...")
            break
        try:
            sayi1 = float(sayi1)
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz!")
            continue
        
        sayi2 = input("İkinci sayıyı giriniz: ")
        try:
            sayi2 = float(sayi2)
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz!")
            continue

        islem = input("Yapmak istediğiniz işlemi giriniz (+, -, *, /): ")
        if islem not in ['+', '-', '*', '/']:
            print("Geçersiz işlem türü girdiniz!")
            continue

        if islem == '+':
            print(f"{sayi1} + {sayi2} = {sayi1 + sayi2}")
        elif islem == '-':
            print(f"{sayi1} - {sayi2} = {sayi1 - sayi2}")
        elif islem == '*':
            print(f"{sayi1} * {sayi2} = {sayi1 * sayi2}")
        elif islem == '/':
            if sayi2 == 0:
                print("Bölme işleminde ikinci sayı 0 olamaz!TANIMSIZ!")
            else:
                print(f"{sayi1} / {sayi2} = {sayi1 / sayi2}")

hesap_makinesi()
