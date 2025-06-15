#50 elemanlı bir dizinin 1. ve 2. elemanları toplamının yarısı başka bir dizinin ilk 
#elemanı, 3. ve 4. elemanları toplamının yarısı 2. elemanı şeklindedir. Bu işlemi yapan 
#programın algoritma ve akış diyagramını çiziniz. 
import array as arr
a = arr.array('i', range(1, 51)) #1 den 50 ye kadar otomatik doldurmasını sağladım
b = []
c=[range(1,51)]
for i in range(0,50,2): #2 şer artmasını sağladım ki +1 yaptığımızda kullanılan sayılar bir daha kullanılmasın
        b.append((a[i] + a[i+1])/2)

print(b)
