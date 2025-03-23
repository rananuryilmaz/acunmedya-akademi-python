sayılar = []

for i in range(5):
    say = int(input(f"Lütfen {i+1}. sayıyı girin: "))
    sayılar.append(say)

print("Girilen Sayılar:", sayılar)

print("----------")

toplam = sum(sayılar)
print(f"Sayıların Toplamı : {toplam}")

print("----------")

ortalama = toplam/5
print(f"Sayıların Ortalaması:{ortalama}")

print("----------")

max_sayı= max(sayılar)
print(f"En Büyük Sayı:{max_sayı}")

print("----------")

min_sayı= min(sayılar)
print(f"En Küçük Sayı:{min_sayı}")

print("*-*-*-*-*-*-*-*-*-*-*-*")

Kelimeler= []

for i in range(5):
    kelime = input(f"Lütfen {i+1}.Kelimenizi giriniz: ")
    Kelimeler.append(kelime)
print("Girilen Kelimeler:", Kelimeler)

Kelimeler.reverse()
print("Tersden Sıralanmış Kelimeler Listesi:", Kelimeler)


print("*-*-*-*-*-*-*-*-*-*-*-*")

liste = [12, 13, 13, 14, 15, 16, 16, 17]
print("Listedeki Elamanlar:",liste)

Yeni_Liste = []
for eleman in liste:
    if eleman not in Yeni_Liste:
        Yeni_Liste.append(eleman)

print("-Tekrar eden elemanlar kaldırıldı-> Yeni Liste:", Yeni_Liste)
