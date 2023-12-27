import random

def kullanici_secimi():
    print("1. Taş")
    print("2. Kağıt")
    print("3. Makas")
    secim = input("Seçiminizi yapın (1/2/3): ")
    return secim

def bilgisayar_secimi():
    return str(random.randint(1, 3))

def sonucu_belirle(kullanici, bilgisayar):
    if kullanici == bilgisayar:
        return "Berabere!"
    elif (kullanici == "1" and bilgisayar == "3") or (kullanici == "2" and bilgisayar == "1") or (kullanici == "3" and bilgisayar == "2"):
        return "Kazandınız!"
    else:
        return "Kaybettiniz!"

def main():
    while True:
        print("\nTaş-Kağıt-Makas Oyunu")
        kullanici = kullanici_secimi()
        if kullanici not in ["1", "2", "3"]:
            print("Geçersiz bir seçim yaptınız. Lütfen 1, 2 veya 3 girin.")
            continue

        bilgisayar = bilgisayar_secimi()
        print(f"Bilgisayarın seçimi: {bilgisayar}")

        sonuc = sonucu_belirle(kullanici, bilgisayar)
        print(f"Sonuç: {sonuc}")

        devam_et = input("Başka bir oyun oynamak istiyor musunuz? (evet/hayır): ")
        if devam_et.lower() != "evet":
            print("Oyunu kapattınız. İyi günler!")
            break

if __name__ == "__main__":
    main()
