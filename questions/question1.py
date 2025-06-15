#1 ile 500 arasındaki tam sayılardan tek sayıların toplamı ile çift sayıların toplamının 
#farkı negatif mi, pozitif mi olduğunu bulan programın algoritma ve akış diyagramını 
#çiziniz.(Döngü Kullanarak) 

i=1
sumeven=0
sumodd=0

for i in range (501): 
    if i%2==0 :#ciftse ciftlerin toplamını arttırır
        sumeven=sumeven+i
    else:#tekse teklerin toplamını arttırır
        sumodd=sumodd+i

sayi=sumodd-sumeven
print(sayi)

#farklarının sonucunu yazar
if sayi > 0:
    print("Pozitif")
elif sayi < 0:
    print("Negatif")
else:
    print("Sıfır")