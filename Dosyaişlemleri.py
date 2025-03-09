def dosya_yaz():

    metin = input("Lütfen dosyaya yazmak için metni giriniz: ")

    with open("dosyaişlemleri.txt", "w", encoding="utf-8") as f:
        f.write(metin + "\n")
    print("Metniniz dosyaya yazıldı.")


def dosya_oku():
    
    try:
        with open("dosyaişlemleri.txt", "r", encoding="utf-8") as f:
            dosya_içerik = f.read()
            print("Dosya içeriği:")
            print(dosya_içerik)  
    except FileNotFoundError:
        print("Dosya bulunamadı!")


def satirlar():
    
    satirlar = []
    print("Lütfen 5 farklı satır giriniz:")
    for i in range(5):
        satir = input(f"Satır {i+1}: ")
        satirlar.append(satir)

    with open("dosyaişlemleri.txt", "a",encoding="utf-8") as f:
        for satir in satirlar:
          f.write(satir + "\n")
    print("\nSatırlar dosyaya yazıldı.")

    try:
        with open("dosyaişlemleri.txt", "r",encoding="utf-8") as f:
            print("\nDosyadaki satırlar:")
            for satir in f:
                print(satir.strip())
    except FileNotFoundError:
        print("Dosya bulunamadı!")


def main():
    dosya_yaz()
    dosya_oku()
    satirlar()
    


main()
    