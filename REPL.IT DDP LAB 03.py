# DDP LAB-3

# SOAL 1 - Gunting-Batu-Kertas
# Tuliskan program untuk Soal 1 di bawah ini

print("Soal No 1")
print()

A = input("Masukakan Pilihan Player-1: ")
B = input("Masukakan Pilihan Player-2: ")

# berikut adalah program yang berisi kemungkinan yang terjadi.

if A == ("gunting") and B == ("kertas"):
  print("Player-1 menang!")
elif A == ("gunting") and B == ("batu"):
  print("Player-2 menang!")
elif A == ("kertas") and B == ("gunting"):
  print("Player-2 menang!")
elif A == ("batu") and B == ("kertas"):
  print("Player-2 menang!")
elif A == ("batu") and B == ("gunting"):
  print("Player-1 menang!")
elif A == ("batu") and B == ("kertas"):
  print("Player-1 menang!")
else:
  print("seri!")
# ketika player 1 dan 2 memasukkan benda yang sama maka, hasilnya akan seri.
print()

# SOAL 2 - Toko Buku Bekas
# Tuliskan program untuk Soal 2 di bawah ini

print("Soal No 2")
print()
# Berikut daftar harga buku yang dijual.
print("1-10 buku = Rp. 20.000/buku")
print("11-25 buku = Rp. 18.000/buku")
print("26-50 buku = Rp. 15.000/buku")
print("50+ buku = Rp. 10.000/buku")
print()

# Pengguna diminta memasukkan berapa banyak buku yang akan dibeli.
A = int(input("Mau beli berapa buku?: "))

# Berikut program yang akan menghasilkan berapa harga total buku yang telah dimasukkan oleh pengguna.
if A > 50:
  print("Harga Rp. 20.000/buku")
  print("Harga Total = Rp.",A*20000) 
elif A >=26 and A <=50:
  print("Harga Rp. 18.000/buku")
  print("Harga Total = Rp.",A*18000)
elif A >=11 and A <=25:
  print("Harga Rp. 15.000/buku")
  print("Harga Total = Rp.",A*15000)
elif A <= 10:
  print("Harga Rp. 10.000/buku")
  print("Harga Total = Rp.",A*10000)
# Jika pengguna memasukkan angka negatif, maka program akan mengeluarkan tulisan sebagai berikut,
else:
  print("KESALAHAN!")
  print()

# SOAL 3 - Mencetak Persegi
# Tuliskan program untuk Soal 3 di bawah ini

print("Soal NO 3")
print() 

# print("i <= k")
k = eval(input("Masukkan sebuah bilangan bulat: "))
for i in range(k):
    for j in range(k):
        if (i % 2 == 0):
            print("#", end='', sep='')
        else:
             print("$", end='')
    print()