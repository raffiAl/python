# a. Membuat list berisi 10 angka (dapat diisi secara manual atau melalui input pengguna)
myList = []
for i in range(1, 20, 2): 
    myList.append(i)
print('List angka:', myList)

# b. Menjumlahkan semua elemen yang ada dalam list tersebut
total = sum(myList)
print(f'Jumlah list menggunakan method sum = {total}')
print(' ')

# Menambahkan value baru ke dalam list
# a. Membuat sebuah list berisi 5 nama buah
fruits = ['apel', 'mangga', 'jeruk', 'semongko', 'jambu']
print('List buah:', fruits)

# b. Menampilkan seluruh isi list
# c. Menampilkan buah pada indeks ke-2
print(f'Buah di indeks ke-2: {fruits[2]}')

# d. Menambahkan 1 nama buah baru ke dalam list
fruits.append('leci')
print('Menambahkan leci:', fruits)
print(' ')

# Buatlah program Python yang menerima input angka-angka dari pengguna
# a. Simpan angka-angka tersebut dalam sebuah list
input_angka = input('Masukkan beberapa angka, pisahkan dengan spasi: ')
angka_list = [int(num) for num in input_angka.split()]
print('List angka:', angka_list)

# b. Hitung jumlah total dari semua angka dalam list
total_angka = sum(angka_list)
print(f'Jumlah total: {total_angka}')

# c. Tampilkan nilai rata-rata dari list
average = total_angka / len(angka_list) if angka_list else 0
print(f'Rata-rata: {average}')

# d. Temukan dan tampilkan nilai terbesar dan terkecil dalam list
print(f'Nilai terbesar: {max(angka_list)}')
print(f'Nilai terkecil: {min(angka_list)}')
print(' ')

# Buatlah program Python untuk menghitung nilai statistik dari sebuah list angka:
# a. Minta pengguna memasukkan beberapa angka (minimal 5 angka)
input_angka_statistik = input('Masukkan beberapa angka (minimal 5 angka), pisahkan dengan spasi: ')
angka_list_statistik = [int(num) for num in input_angka_statistik.split()]

# Pastikan ada minimal 5 angka
if len(angka_list_statistik) < 5:
    print("Silakan masukkan minimal 5 angka.")
else:
    # b. Hitung dan tampilkan nilai minimum, maksimum, rata-rata, dan median
    print('List angka:', angka_list_statistik)
    total_statistik = sum(angka_list_statistik)
    average_statistik = total_statistik / len(angka_list_statistik)
    print(f'Jumlah total: {total_statistik}')
    print(f'Rata-rata: {average_statistik}')
    print(f'Nilai terbesar: {max(angka_list_statistik)}')
    print(f'Nilai terkecil: {min(angka_list_statistik)}')

    # Menghitung median
    angka_list_statistik.sort()  # Mengurutkan list
    n = len(angka_list_statistik)
    if n % 2 == 1:  # Jika jumlah elemen ganjil
        median = angka_list_statistik[n // 2]
    else:  # Jika jumlah elemen genap
        median = (angka_list_statistik[n // 2 - 1] + angka_list_statistik[n // 2]) / 2
    print(f'Median: {median}')

    # c. Tampilkan list setelah diurutkan dari terkecil ke terbesar
    print('List setelah diurutkan:', angka_list_statistik)

# Membuat list kosong untuk daftar belanja
daftar_belanja = []

# Meminta pengguna memasukkan 5 item belanjaan
print("Masukkan 5 item belanjaan:")
for i in range(5):
    item = input(f"Item ke-{i+1}: ")
    daftar_belanja.append(item)

# Menampilkan seluruh daftar belanja
print("\nDaftar belanja Anda:")
for idx, item in enumerate(daftar_belanja, start=1):
    print(f"{idx}. {item}")

# Meminta pengguna untuk menghapus 1 item yang sudah dibeli
hapus_item = input("\nMasukkan nama item yang sudah dibeli dan ingin dihapus: ")

if hapus_item in daftar_belanja:
    daftar_belanja.remove(hapus_item)
    print(f"\n'{hapus_item}' telah dihapus dari daftar belanja.")
else:
    print(f"\nItem '{hapus_item}' tidak ada dalam daftar belanja.")

# Menampilkan daftar belanja yang diperbaharui
print("\nDaftar belanja terbaru:")
for idx, item in enumerate(daftar_belanja, start=1):
    print(f"{idx}. {item}")
