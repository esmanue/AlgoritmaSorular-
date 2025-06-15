#4 haneli bir sayının birler, onlar, yüzler ve binler hanesini bulan programın algoritma 
#ve akış diyagramını çiziniz. 
sayi = int(input('4 basamakli bir sayi giriniz:'))
for i in range (4):
    print(sayi%10) #sondaki basamağı yazdırır
    sayi=int(sayi/10) #yazdırdığımız basamağı çıkarır ve int() ile virgülden sonrası 0 lanır