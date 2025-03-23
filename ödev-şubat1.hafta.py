def hesap_makinesi(sayi1, sayi2):
    toplam = sayi1 + sayi2
    fark = sayi1 - sayi2
    çarpım = sayi1 * sayi2
    bölme = sayi1 / sayi2
    
    return toplam, fark, çarpım, bölme

sayi1 = float(input("Birinci sayıyı giriniz: "))
sayi2 = float(input("İkinci sayıyı giriniz : "))


toplam, fark, çarpım, bölme = hesap_makinesi(sayi1, sayi2)


print(f"Toplam->{sayi1}+{sayi2}= {toplam}")
print(f"Fark  ->{sayi1}-{sayi2}= {fark}")
print(f"Çarpma->{sayi1}*{sayi2}= {çarpım}")
print(f"Bölme ->{sayi1}/{sayi2}= {bölme}")

print("*-*-*-*-*-*-*-*-*-*-*-*")

def palindrom_mu(kelime):
    if kelime == ''.join(reversed(kelime)):
        return True
    else:
        return False
kelime = input("Bir kelime girin: ")

if palindrom_mu(kelime):
    print(f"{kelime} bir palindromdur.")
else:
    print(f"{kelime} bir palindrom değildir.")

print("*-*-*-*-*-*-*-*-*-*-*-*")

def yaş_yıl_hesapla(yaş):
    if yaş < 0 or yaş > 100:
        return "Geçerli bir yaş giriniz!"
    elif yaş == 100:
        return "Zaten 100 yaşındasınız!"
    else:
        return f"{100 - yaş} yıl sonra 100 yaşına ulaşacaksınız."

yaş = int(input("Yaşınızı giriniz: "))
print(yaş_yıl_hesapla(yaş))




