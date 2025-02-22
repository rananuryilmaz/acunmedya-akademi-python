# 3.Ders Videosu Öğrenilenler:

# sınıflar => classlar
# modules
# paket yönetimi
#self => this

class Human:
    #built-in #constructor #initialize
    def __init__(self,name):
        self.name = name
        print("Bir human instance'i üretildi")
    def __str__(self) -> str:   #-> str ilgili fonksiyonun geriye dönüş tipini anlatan yapıdır. geriye string dönüyor burda kullanmak zorunda değiliz. 
        return f"STR Fonksiyonundan dönen değer: {self.name}"     
    def talk(self,sentence):
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking..")

# instance => örnek
human1 = Human("Enes")
human1.talk("Merhaba")
human1.walk() 
print(human1)

human2 = Human("Rana")
human2.talk("Selam")
human2.walk()
print(human2)

Human("Melike").talk("Merhaba") #tek satırda bunu bir değişkene atamadan da yapabiliriz.

# human isminde bir class oluşturduk human burada nesne konumunda.
# nesnelere erişebilmemiz için bu nesnelerden birer instance ürün oluşturmamız gerekiyor.   