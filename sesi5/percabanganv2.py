# POSITIF/NEGATIF
angka = float(input("Masukkan angka: "))
if angka > 0:
    print("Positif")
elif angka < 0:
    print("Negatif")

# GENAP/GANJIL
angka = int(input("Masukkan angka: "))
if angka % 2 == 0:
    print("Genap")
else:
    print("Ganjil")

# GRADE UJIAN
nilai = float(input("Masukkan nilai: "))
if 80 <= nilai <= 100:
    print("A")
elif 70 <= nilai <= 79:
    print("B")
elif 60 <= nilai <= 69:
    print("C")
elif 50 <= nilai <= 59:
    print("D")
else:
    print("E")

# ANGKA TERBESAR
a = float(input("Angka 1: "))
b = float(input("Angka 2: "))
c = float(input("Angka 3: "))
terbesar = a
if b > terbesar:
    terbesar = b
if c > terbesar:
    terbesar = c
print("Angka terbesar:", terbesar)

# TAHUN KABISAT
tahun = int(input('masukan tahun: '))
if (tahun % 4 == 0):
   print('tahun %i merupakan tahun %s' %(tahun, 'kabisat'))
else:
    print('tahun %i bukan tahun %s' %(tahun, 'kabisat'))

# KALKULATOR SEDERHANA
angka1 = float(input("Angka pertama: "))
operator = input("Operator (+, -, *, /): ")
angka2 = float(input("Angka kedua: "))

if operator not in ['+', '-', '*', '/']:
    print("Operator tidak valid")
else:
    if operator == '/':
        if angka2 == 0:
            print("Pembagian dengan nol tidak diizinkan")
        else:
            hasil = angka1 / angka2
    else:
        if operator == '+':
            hasil = angka1 + angka2
        elif operator == '-':
            hasil = angka1 - angka2
        elif operator == '*':
            hasil = angka1 * angka2
    print("Hasil:", hasil)

# KATEGORI BMI
berat = float(input("Berat (kg): "))
tinggi = float(input("Tinggi (m): "))
bmi = berat / (tinggi ** 2)
if bmi < 18.5:
    print("Kekurangan berat badan")
elif 18.5 <= bmi < 25:
    print("Normal")
elif 25 <= bmi < 30:
    print("Kelebihan berat badan")
else:
    print("Obesitas")

# SEGITIGA
a = float(input("Sisi 1: "))
b = float(input("Sisi 2: "))
c = float(input("Sisi 3: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Sisi tidak valid")
else:
    if (a + b > c) and (a + c > b) and (b + c > a):
        print("Bisa membentuk segitiga")
        if a == b == c:
            print("Segitiga sama sisi")
        elif a == b or a == c or b == c:
            print("Segitiga sama kaki")
        else:
            print("Segitiga sembarang")
    else:
        print("Tidak bisa membentuk segitiga")

# SISTEM LOGIN
username = input("Username: ").strip().lower()
password = input("Password: ").strip().lower()

if username == 'admin' and password == 'admin123':
    print("Akses admin")
elif username == 'user' and password == 'user123':
    print("Akses terbatas")
elif username == 'guest' and password == '':
    print("Akses minimal")
else:
    print("Akses ditolak")

# BATU GUNTING KERTAS
import random

pemain_skor = 0
komputer_skor = 0
pilihan = ['batu', 'gunting', 'kertas']

while True:
    pemain = input("Pilih (batu/gunting/kertas): ").lower().strip()
    if pemain not in pilihan:
        print("Pilihan tidak valid")
        continue

    komputer = random.choice(pilihan)
    print(f"Komputer memilih: {komputer}")

    if pemain == komputer:
        print("Seri!")
    elif (pemain == 'batu' and komputer == 'gunting') or \
         (pemain == 'gunting' and komputer == 'kertas') or \
         (pemain == 'kertas' and komputer == 'batu'):
        print("Anda menang!")
        pemain_skor += 1
    else:
        print("Komputer menang!")
        komputer_skor += 1

    print(f"Skor: Anda {pemain_skor} - {komputer_skor} Komputer")
    ulang = input("Lanjutkan? (ya/tidak): ").lower().strip()
    if ulang != 'ya':
        break 