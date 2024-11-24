import random
import time

gameDiff=""
life=10
number=random.randint(1,99)
def guessCheck(guess):
    if guess>number:
        return "Aşağı in"
    elif guess<number:
        return "Yukarı çık"

while input("\nSayı tahmin oyununa hoşgeldiniz! Oynamak ister misiniz? (E/H)").lower()=="e":
    diffChoice=input("\nHangi zorlukta oynamak istersiniz? (Kolay[1]/Zor[2])")
    if diffChoice=="2":
        life-=5
        print(f"Tahmin hakkınız: {life}")
    print(f"Tahmin Hakkınız: {life}")
    guess=0
    while life>0 and guess!=number:
        guess=int(input("\n0-100 Arasında tuttuğum sayıyı tahmin ediniz : "))
        if guess!=number:
            life-=1
            print(f"Yanlış tahmin,", guessCheck(guess))
            if life!=0:
                print(f"Kalan tahmini hakkınız: {life}")
            else:
                print("Oyunu kaybettiniz.")
    print("Tebrikler! Tuttuğum sayıyı bildiniz!")
    time.sleep(0.5)
print("Çıkış yapılıyor...")