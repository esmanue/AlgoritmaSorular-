matris = [[0, 0, 0] for _ in range(5)]#0 larla dolu bir matris oluşturdum

#her satır için id vize ve final değerlerini aldım
for i in range(5):
    id = int(input('örenci id giriniz'))
    matris[i][0]=id
    vize = int(input('vize notunu giriniz'))
    matris[i][1]=vize
    final = int(input('final notunu giriniz'))
    matris[i][2]=final

print(matris)

#istenen ögrencinin bilgilerini getirir
sira=int(input('kacinci ogrencinin bilgilerini goruntulemek istersiniz'))
print(matris[sira])