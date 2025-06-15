#10 elemanlı bir sayı dizisinde en küçük elemanın bu dizinin kaçıncı elemanı olduğunu 
#bulan programın algoritma ve akış diyagramını çiziniz.

a = [5,11,6,7,3,78,21,46,2,8]
minval=a[0] #karsılastırma yapmak için ilk elemana en kücük degeri verdim
sira=0

for i in range(len(a)):
    if minval>a[i]: #min degerin dizide daha  buyuk oldugu sayılar varsa bunu atama yaparak degistirdim
        minval=a[i]

#esit olmadıgı sürece sirayi arttirir
for x in range(len(a)):
    if minval!=a[x]:
        sira+=1
    else:
        sira+=1 #esit oldugu anda da kacıncı sırada oldugunu kaydedip sonra donguden cıkması icin
        break


print(sira)