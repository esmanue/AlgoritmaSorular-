sayi = int(input('aramak istediginiz sayiyi giriniz'))
a = [5,11,6,7,3,78,21,46,2,8]
first=0
last=len(a)

for first in range(last):
    mid=int((first+last)/2)
    if sayi==a[mid]:
        print("aradiginiz sayi",mid+1,". siradadir")
        break
    elif sayi>a[mid]:
        first=mid+1
    elif sayi<a[mid]:
        last=mid-1

