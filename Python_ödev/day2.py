#2.Ders Videosu Öğrenilenler:
faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

#type hangi veri türü olduğunu gösterir.

print(int(vade)+12) #vade string veri türü olmasına rağmen burada vade ile işlem yapmak istediğim için vadenin türünü bu işlem kısmında değiştirmiş oldum ve int yani sayısal veri türü olarak yazdım.

#metinsel bir ifade olursa string olarak olmaz dikkat et sadece string olarak yazılmış sayısal değerler de olur !!!
#Örneğin print(int(krediAdi)+12) Burada hata alırsın çünkü metinsel bir ifade.

faiz = str(faiz)
print(type(faiz))

vade= 36 #int(input("Lütfen istediğiniz vade sayısını giriniz: ")) #imput kullanıcı girişi almamızı sağlayan bir fonksiyondur.
print(type(vade))
vade = vade + 12

#string interpolation
#Seçtiğiniz vade sonucu ortaya çıkan vade:
print("Seçtiğiniz vade sonucu ortaya çıkan vade :" + str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade : {vadeSayisi}".format(vadeSayisi=vade))
print(f"Seçtiğiniz vade sonucu ortaya çıkan vade : {vade}")

isim = "Rana" #input ("İsminizi giriniz")
metin ="Merhaba {name}".format(name=isim) #format fonksiyonu
print(metin)

#f-string
metin= f"Hoşgeldiniz {1+1}"
print(metin)

print("**********DİZİLER***************")

# listeler
# döngüler
# fonksiyonlar

dizi=["İhtiyaç Kredisi", 10, 5.2] #Pythonda bir dizi içerisinde farklı türlerdeki veriler tutulabilir.
print(dizi)


krediler=["İhtiyaç kredisi","Taşıt Kredisi","Konut kredisi"]
print(type(krediler))

print(krediler[0])

# print(krediler[5]) 5 yazamayız çünkü index hatası verir.0-1-2 ye kadar yazabiliriz.

print(len(krediler)) #len,length fonksiyonu dizide kaç eleman olduğunu bize söyler.

krediler.append("Özel Kredi") #append dizi sonuna yeni eleman eklemek için kullanılan bir fonksiyondur.
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop(0) #pop fonksiyonu içerisine her hangi bir değer almıyor.index girmedikçe son elemanı siler ama 0 girersen 0.indexi siler.
print(krediler)

krediler.append("Taşıt Kredisi")
print(krediler)
krediler.remove("Taşıt Kredisi") #ilk gördüğü taşıt kredisini sildi ama sondaki durmaya devam ediyor.
print(krediler)

krediler.extend(["Y Kredisi", "Z Kredisi"])# extend birden fazla elemanı eklemek için kullanılır.
print(krediler)

print("*********DÖNGÜLER***********")
#DÖNGÜLER
# for
#i=0 i<10

for i in range(10): 
    print("xx")
    print(i)

#range i ...'ya a kadar ilerletir burada içine 10 yazdık 10 dahil olmadan ekrana yazdırmış olucak yani 10 a kadar i yi arttırıcak.

print("********************")

for i in range(5,10): 
    print(i)

# ... ile ... arasında olmasını istersem bu şekilde burada 5 (dahil) ile 10 arasında olmuş oldu ve i değerim 0 dan değil 5 den başladı.
#i ye 5 atadım => 10 kadar birer birer arttırdım => döngü bitti => döngüden çıktı.

print("********************")

for i in range(0,51,10): 
    print(i)

# Artış miktarının 1 den farklı sayı değeri olarak artmasını istiyorsam döngüde range ifadesinin içine 3. kısım da artış girmem gerekli.
#1.kısm i nin nerden başlayacağı | 2.kısım nereye kadar artıcağı | 3.kısım artış miktarına karar veridiğim kısımdır|

#range int olarak giriş ister floatlı bir şekilde sayı giremezsin!

krediler = ["İhtiyaç Kredisi" ,"Taşıt Kredisi", "Konut Kredisi"]
for kredi in krediler:
    print(kredi)
print("******************")
for i in range(len(krediler)):
    print(krediler[i])

#sonsuz döngü
i=10
while i<10:
    print("x")
    i += 1
print("y")

print("*******************")

while True:
    print("X")
    break

print("**************")

i = 0
while i <len(krediler):
    i+=1
    print(i)
    print(krediler[i])
    if krediler[i]=="Konut Kredisi":
        break
#break => buradaki döngüyü kır demek i konut kredisine eşit olması durumunda döngüden çık.

print("***********FONKSİYONLAR***************")
#FONKSİYONLAR

fiyat = 10
indirim = 20
#definition define
def calculate():
    print(100-20)

def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)

def sayHello(name):
    print(f"Merhaba{name}")


calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)
sayHello("Halit")
sayHello("Arif")
sayHello("Mevlüt")

def calculateAndReturn(fiyat, indirim):
    return fiyat - indirim

yeniFiyat = calculateAndReturn(200, 50)
print(yeniFiyat + 10)

#void 
def calculatePrice(price, discount):
    print (price-discount)

def calculatePriceAndReturn(price, discount):
    return price-discount

print("***************")
fonk1 = calculatePrice(100, 50)
fonk2 = calculatePriceAndReturn(300, 100)
#print(f"174. satır: {fonk1+100}") # fonk1 return olmadığı için fonk1 de değer ataması olmadı
print(f"175. satır: {fonk2+100}")
print("***************")
#retunde çağrıldığı noktaya bir değer döndürüldüğü için bu değer üzerinde matematiksel operatörler kullanabiliyor değişkene atanabiliyor. 