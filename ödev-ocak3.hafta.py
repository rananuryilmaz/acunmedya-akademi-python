#1den 100 e kadar olan say.
i = 1
while i <= 100:
    print(i)
    i += 1


print("***************************")
#• 1’den 100’e kadar sadece çift sayılar

for i in range(1, 101):  
    if i % 2 == 0:  
        print(i)


print("***************************")
#girilen sayının faktöriyelini hesaplama 

sayı = int(input("Bir sayı giriniz:"))  
f = 1  
sayılar = []

for s in range(1,sayı+1):
    f *= s
    sayılar.append(str(s))

print(f"{sayı}! = {' * '.join(sayılar)} = {f}")


print("**************************")
#1den 100 asal sayı olanları bulma

for a in range(2, 101): 
    for i in range(2,a): 
        if a % i == 0:
            break
    else:
        print(a,end="-")



        

