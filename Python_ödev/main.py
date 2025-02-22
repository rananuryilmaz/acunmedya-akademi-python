#1.Ders Videosu Öğrenilenler:

print("Kodlamaio")
baslik = "Taşit Kredisi"
print(baslik)
# string => metinsel ifade
baslik ="İhtiyaç Kredisi"
print(baslik)
# int, integer => tam sayı 
vade= 36
ekVade = 36
vade2 ="36"

# float,decimal, double
aylikOdeme= 200.50

# bool, boolean => True veya False
yukselisteMi = False

#matematiksel operatörler

# +
print(5 + 5)
print(vade + 12)
print(vade + ekVade)
print(36 + 6)

# -
print(5 - 5)
print(vade - 12)
print(vade - ekVade)
print(36 - 6)

# *
print(5 * 5)
print(vade * 2)
print(vade * ekVade)
print(10 * 10)

# /
print(5 / 5)
print(vade / 2)
print(vade / ekVade)
print(10/2)

yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# % => mod operator

print(10%2) #çıktısı ne olur sorusuna cevabım : Sıfır  (mod alma kalanı verir.)
print(vade % 5)
print(vade % 5)
print(vade % ekVade)
print(30 % 10)

#mantıksal operatörler
print(1 == 1)              
print(1 == 2)     #değer doğruysa çıktı True değilse False döner.

print(1 > 2)
print(3 > 1)
print(1 > 1)
print(1 >= 1) 

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)

# CTRL K + CTRL C ile tüm satırı yorum satırı yapıyorsun. CTRL+Ö ile yorum satırına ekle çıkart.

print(1 != 1)
print(1 != 2)

# or and 

#or => veya
print(1 > 2 or 5 > 2) #  0 or 1 den çıktısı True olur.

print(1 > 2 and 5 > 2) # 0 and 1 den çıktısı False olur.

print(1 > 2 or 5 > 2 and 3 > 2) # (soldan başla okumaya) 0 or 1 => 1 and 1 den çıktısı True olur.

print(1 > 2 and 5 > 2 and 3 > 2 ) # 0 and 1 => 0 and 0 dan çıktısı False olur.

print(2 > 1 or 1 >2 and 3 > 2) # çıktısı True olur.

# karar yapıları
# if else
sayi1 = 15
sayi2 = 15
# sayi1 sayi2'den büyükse ekrana sayi 1 daha büyük yazdır.
#condition

#indent
if sayi1 < sayi2:
    print("Sayi 1 Sayi 2 'den küçüktür")
    print("Hala if bloğunun içerisindeyim") #Python da if- else - elif vb. bloklarında satır başına değil içine print yazman gerekli. 
#eğer if bloğuna girmez ise
elif sayi1 == sayi2:
    print("İki sayı eşittir")
#eğer if ve else if bloklarında hiç birine girmez ise
else:
   print("Sayi 1 Sayi 2'den büyüktür")

print("*****************************************")

if sayi1 <= sayi2:
    print("Sayi 1 Sayi 2 'den küçüktür")
if sayi1 == sayi2:
    print("İki sayı eşittir")
else:
   print("Sayi 1 Sayi 2'den büyüktür")

print("Burası if bloğunun dışıdır.")