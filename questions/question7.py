import copy #burada atama yaparak kopyasını oluşturduğumda orijinali üzerinde işlem yapılınca kopyası da değişti
#bu yüzden copy kütüphanesini import ettim
matris=[[1,2],
       [3,4]]

copymatris = copy.deepcopy(matris)

#satırları sütün sütunları satır yaptım
matris[0][1]=copymatris[1][0]
matris[1][0]=copymatris[0][1]

print(matris)