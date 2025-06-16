sayi = int(input('sirasini bulmak istediginiz sayiyi giriniz:'))
a = [5,11,6,7,3,78,21,46,2,8]
sira=0

for x in range(len(a)):
    if sayi==a[x]:
        sira+=1 #esit oldugu anda da kacıncı sırada oldugunu kaydedip sonra donguden cıkması icin
        print('aradiginiz sayi',sira,". siradadir")
        break
    else:
        sira+=1 #esit değilse arama yapip sirayi arttirmaya devam eder