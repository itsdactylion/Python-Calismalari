"""
Problem 3
1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.
"""

print("""***********************************
Carpim Tablosuna Hosgeldin Yegen
Written by BYK haberin olsun
***********************************""")

for i in range(1,10):
    for j in range(1,11):
        print(" {} * {} = {}".format(i,j,i*j))
    print("**************")