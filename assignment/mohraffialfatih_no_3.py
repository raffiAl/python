inventaris = {}

def tampilkan_tabel():
    print("\nDaftar Barang:")
    print("{:<20} {:<10} {:<10}".format("Nama Barang", "Harga", "Stok"))
    for nama, (harga, stok) in inventaris.items():
        print("{:<20} {:<10} {:<10}".format(nama, harga, stok))

while True:
    print("\nMenu:")
    print("1. Tambah Barang Baru")
    print("2. Tampilkan Semua Barang")
    print("3. Cari Barang")
    print("4. Perbarui Stok Barang")
    print("5. Hapus Barang")
    print("6. Analisis Data")
    print("7. Keluar")
    pilihan = input("Pilih menu (1-7): ")

    if pilihan == '1':
        nama = input("Nama Barang: ")
        harga = int(input("Harga: "))
        stok = int(input("Stok: "))
        inventaris[nama] = (harga, stok)
    elif pilihan == '2':
        if inventaris:
            tampilkan_tabel()
        else:
            print("Inventaris kosong.")
    elif pilihan == '3':
        nama = input("Nama Barang: ")
        if nama in inventaris:
            harga, stok = inventaris[nama]
            print(f"Harga: {harga}, Stok: {stok}")
        else:
            print("Barang tidak ditemukan.")
    elif pilihan == '4':
        nama = input("Nama Barang: ")
        if nama in inventaris:
            stok_baru = int(input("Stok baru: "))
            harga = inventaris[nama][0]
            inventaris[nama] = (harga, stok_baru)
        else:
            print("Barang tidak ditemukan.")
    elif pilihan == '5':
        nama = input("Nama Barang: ")
        if nama in inventaris:
            del inventaris[nama]
            print("Barang dihapus.")
        else:
            print("Barang tidak ditemukan.")
    elif pilihan == '6':
        if inventaris:
            harga_tertinggi = max(inventaris.items(), key=lambda x: x[1][0])
            harga_terendah = min(inventaris.items(), key=lambda x: x[1][0])
            total_nilai_stok = sum(h * s for h, s in inventaris.values())
            print(f"Barang dengan harga tertinggi: {harga_tertinggi[0]} ({harga_tertinggi[1][0]})")
            print(f"Barang dengan harga terendah: {harga_terendah[0]} ({harga_terendah[1][0]})")
            print(f"Total nilai stok: {total_nilai_stok}")
        else:
            print("Tidak ada data untuk dianalisis.")
    elif pilihan == '7':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid.")
