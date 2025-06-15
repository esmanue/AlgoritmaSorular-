#Tam sayılardan oluşan bir dizi veriliyor, bu dizi elemanlarından kaç tanesinin bir 
#basamaklı, kaç tanesinin iki basamaklı, kaç tanesinin de üç basamaklı olduğunu 
#bulan programın algoritma ve akış diyagramını çiziniz. 
a = [5, 61, 236, 235, 4]
c = []
b=10 #burada 10 vermemin sebebi 10la bölünen bir sayının sonucunun tam sayı kısmı 0 dan büyükse (tam sayı) en az iki basamaklıdır
basamak=1
bir = iki = uc = 0
for i in range(len(a)):
    basamak=1
    for x in range (3): #en fazla üç basamaklı olan sayılar üzerinde olduğu için. range değiştirilebilir 
        if int(a[i]/(b*(10**x)))!=0: #eğer tam sayı kısmı 10 la bölününce bile 0 dan farklıysa bu sefer 10**n ile bolerız
            basamak=basamak+1

    if basamak == 1:
        bir += 1
    elif basamak == 2:
        iki += 1
    elif basamak == 3:
        uc += 1

print("dizideki bir basamakli sayi",bir,"tane, iki basamakli sayi",iki,"tane, uc basamakli sayi sayisi",uc,"tane")


