# SOAL 1 - Menghitung rata-rata
# Tuliskan program untuk Soal 1 di bawah ini
print("soal 1")
x = eval(input('Masukkan bilangan pertama  : ')) 
y = eval(input('Masukkan bilangan kedua    : '))
z = eval(input('Masukkan bilangan ketiga   : '))
tambah = float(x) + float(y) + float(z)
ratarata = tambah / 3
print('Rata-rata bilangan {0}, {1}, dan {2} adalah {3}'.format(x, y, z, ratarata))

# SOAL 2 - Menulis kelipatan bilangan
# Tuliskan program untuk Soal 2 di bawah ini
print("soal 2")
x = int(input(' Masukkan sebuah bilangan bulat : '))
print('kelipatan bilangan', x , 'adalah: ')
print(x, x*2, x*3, x*4, x*5, x*6, sep='---')