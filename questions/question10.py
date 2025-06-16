sayi = int(input('aramak istediginiz sayiyi giriniz'))
a = [5,11,6,7,3,78,21,46,2,8]
first=0
last=len(a)

#last ve first esit olana kadar döngü devam eder
for first in range(last):
    mid=int((first+last)/2) #küsuratlı cıkmasın diye int()
    if sayi==a[mid]:
        print("aradiginiz sayi",mid+1,". siradadir")
        break
    elif sayi>a[mid]: #arama sagda yapilir
        first=mid+1
    elif sayi<a[mid]: # arama solda yapilir
        last=mid-1

