def luas_persegi(a, b): 
  result = a * b
  print(result)
  
luas_persegi(10, 10)

def uang_kembalian(total_belanja, bayar): 
  result = bayar - total_belanja
  print(result)

uang_kembalian(10000, 20000)

def perhitungan(a, b): 
  perkalian = a * b
  pertambahan = a + b
  pengurangan = a - b
  pembagian = a / b
  print(pembagian, perkalian, pertambahan, pengurangan)
  
perhitungan(12, 4)

def diskon(bayar, diskon): 
  result = bayar * diskon
  print(result)
  
diskon(100000, 20/100)

def profit_calculation(harga_jual, modal): 
  result = harga_jual - modal
  print(f"modal = {modal}, harga jual = {harga_jual}, profit = {result}")
  
profit_calculation(3000000, 2500000)

buah = "apel"
harga = 10000 

def ubah_nilai(a, b): 
  buah = a
  harga = b
  print(buah, harga)
  
ubah_nilai("jeruk", 20000)

def rata_rata(*args):
  list_data = []
  for data in args:
    list_data.append(data)

  total = sum(list_data[:3])
  rata_rata = total / 3

  return rata_rata

print(rata_rata(12, 13, 14))

def luas_keliling_segitiga(sa, sb, sc, alas, tinggi):
   luas = 1/2 * alas * tinggi
   keliling = sa + sb +sc

   print(f"luas = {luas} dan keliling = {keliling}")

luas_keliling_segitiga(4, 5, 6, 10, 15)