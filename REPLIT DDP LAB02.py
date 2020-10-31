# DDP LAB-2

# SOAL 1 - Mencetak bilangan
# Tuliskan program untuk Soal 1 di bawah ini
print("soal 1")
for i in range(100,1,-2):
  print(i)
 
# PENJELASAN SOAL NO 1
#karena soal meminta untuk membuat program yang menghasilkan kelipatan berkurang dari 100 sampai 2, maka 100 adalah bilangan awal, 1 adalah bilangan akhir, dan -2 adalah kelipatannya. sedangkan (end="") berfungsi untuk menampilkan hasil program dengan mengurut kesamping. 

# SOAL 2 - Menghitung rata-rata
# Tuliskan program untuk Soal 2 di bawah ini
print("soal 2")
x= eval(input("Masukkan sebuah bilangan: "))
hasil=0
for i in range(x):
  y= eval(input("Masukkan sebuah bilangan: "))
  hasil=hasil+y
print('jumlah:', hasil)
print('Rata-rata', hasil/x)
#PENJELASAN SOAL 2
#Pengguna akan diminta untuk memasukkan bilangan, dimana dari seluruh bilangan yang dimasukkan akan dihasilkan rata2nya oleh program tersebut.

# SOAL 3 - Mencetak persegi
# Tuliskan program untuk Soal 3 di bawah ini
print("soal 3")
x= int(input(' Masukkan sebuah bilangan bulat : '))
for a in range(x):
  for b in range(x):
    print('#',end=" ")
  print()
#PENJELASAN SOAL 3
#Luaran atau hasil dari program tersebut akan membentuk persegi yang terdiri dari bentuk #. yang mana jumlah dari isi persegi tersebut bergantung dengan bilangan yang dimasukkan oleh pengguna.