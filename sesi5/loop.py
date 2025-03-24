from datetime import datetime

# Data yang akan diolah
data = [
    {"name": "Nugraha", "birthdate": "1989-09-13"},
    {"name": "John", "birthdate": "1990-01-01"},
    {"name": "Jane", "birthdate": "1992-02-02"},
    {"name": "Doe", "birthdate": "1994-03-03"},
]

def calculate_age(birthdate_str):
    """Menghitung umur berdasarkan tanggal lahir (YYYY-MM-DD)"""
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    today = datetime.now().date()
    
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    
    return age

def generate_table(data):
    """Menghasilkan tabel dari data"""
    # Header tabel
    table = "No | Nama      | Umur\n"
    table += "---|-----------|-----\n"
    
    for index, person in enumerate(data, 1):
        name = person["name"]
        age = calculate_age(person["birthdate"])
        # Format baris tabel dengan padding agar rapi
        table += f"{index:<2} | {name:<10} | {age}\n"
    
    return table

# Menampilkan tabel
print(generate_table(data))

# patern/pola
def deret1():
    """
    Deret 1: 50, 48, 44, 38, 30, 20, 8, -6
    Pola: Selisih awal -2, lalu setiap langkah selisih dikurangi 2 lagi.
    """
    start = 50
    diff = -2
    for _ in range(8):
        print(start, end=" ")
        start += diff
        diff -= 2
    print()

def deret2():
    """
    Deret 2: 2, 3, 5, 8, 13, 21, 34, 55
    Pola: Ini mirip Fibonacci, tetapi dimulai dari 2 dan 3.
    """
    a, b = 2, 3
    print(a, b, end=" ")
    for _ in range(6):  # total 8 angka, sudah terpakai 2
        c = a + b
        print(c, end=" ")
        a, b = b, c
    print()

def deret3():
    """
    Deret 3: 40, 39, 36, 31, 24, 15, 4, -9
    Pola: Selisih awal -1, lalu setiap langkah selisih dikurangi 2.
    """
    start = 40
    diff = -1
    for _ in range(8):
        print(start, end=" ")
        start += diff
        diff -= 2
    print()

def deret4():
    """
    Deret 4: 100, 99, 96, 91, 84, 75, 64, 51
    Pola: Selisih awal -1, lalu setiap langkah selisih dikurangi 2 (sama seperti deret3, beda nilai awal).
    """
    start = 100
    diff = -1
    for _ in range(8):
        print(start, end=" ")
        start += diff
        diff -= 2
    print()

def deret5():
    """
    Deret 5: 1, 1, 2, 3, 5, 8, 13, 21
    Pola: Deret Fibonacci klasik, dimulai dari 1 dan 1.
    """
    a, b = 1, 1
    print(a, b, end=" ")
    for _ in range(6):  # total 8 angka, sudah terpakai 2
        c = a + b
        print(c, end=" ")
        a, b = b, c
    print()

def main():
    print("Deret 1:")
    deret1()
    print("\nDeret 2:")
    deret2()
    print("\nDeret 3:")
    deret3()
    print("\nDeret 4:")
    deret4()
    print("\nDeret 5:")
    deret5()

if __name__ == "__main__":
    main()
