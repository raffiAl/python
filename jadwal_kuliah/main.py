class JadwalKuliah:
    def __init__(self):
        self.jadwal = {}
        self.kelas = ['A', 'B', 'C', 'D']
        self.hari_jam = {
            'Senin': [(8, 10), (10, 12), (13, 15), (15, 17)],
            'Selasa': [(8, 10), (10, 12), (13, 15), (15, 17)],
            'Rabu': [(8, 10), (10, 12), (13, 15), (15, 17)],
            'Kamis': [(8, 10), (10, 12), (13, 15), (15, 17)],
            'Jumat': [(8, 10), (10, 12), (13, 15), (15, 17)]
        }
        self.prodi_dosen = {
            'Informatika': ['Dosen A', 'Dosen B'],
            'Sistem Informasi': ['Dosen C', 'Dosen D']
        }
        self.mata_kuliah_prodi = {
            'Informatika': ['Pemrograman Berorientasi Objek', 'Algoritma dan Struktur Data'],
            'Sistem Informasi': ['Manajemen Basis Data', 'Sistem Operasi']
        }
        self.mata_kuliah_umum = ['Bahasa Indonesia', 'Matematika']

    def cek_kelas_kosong(self, hari, jam):
        for kelas in self.kelas:
            if (hari, jam, kelas) not in self.jadwal:
                return kelas
        return None

    def tambah_jadwal(self, dosen, mata_kuliah, prodi, hari, jam):
        if dosen not in self.prodi_dosen[prodi]:
            print(f"Dosen {dosen} tidak sesuai dengan prodi {prodi}.")
            return

        if mata_kuliah not in self.mata_kuliah_prodi[prodi] and mata_kuliah not in self.mata_kuliah_umum:
            print(f"Mata kuliah {mata_kuliah} tidak tersedia untuk prodi {prodi}.")
            return

        kelas = self.cek_kelas_kosong(hari, jam)
        if kelas is None:
            print(f"Tidak ada kelas kosong pada {hari} jam {jam}. Mencari alternatif...")
            for h, j_list in self.hari_jam.items():
                for j in j_list:
                    kelas = self.cek_kelas_kosong(h, j)
                    if kelas is not None:
                        print(f"Alternatif ditemukan pada {h} jam {j}, kelas {kelas}.")
                        self.jadwal[(h, j, kelas)] = {'dosen': dosen, 'mata_kuliah': mata_kuliah, 'prodi': prodi}
                        return
            print("Tidak ada alternatif kelas yang tersedia.")
        else:
            self.jadwal[(hari, jam, kelas)] = {'dosen': dosen, 'mata_kuliah': mata_kuliah, 'prodi': prodi}
            print(f"Jadwal berhasil ditambahkan pada {hari} jam {jam}, kelas {kelas}.")

    def tampilkan_jadwal(self):
        print(f"{'Nama Dosen':<20} | {'Mata Kuliah':<30} | {'Kelas':<5} | {'Hari - Jam'}")
        print("-" * 75)
        for (hari, jam, kelas), detail in self.jadwal.items():
            print(f"{detail['dosen']:<20} | {detail['mata_kuliah']:<30} | {kelas:<5} | {hari} - {jam[0]}-{jam[1]}")

# Contoh penggunaan
jadwal = JadwalKuliah()
jadwal.tambah_jadwal('Dosen A', 'Pemrograman Berorientasi Objek', 'Informatika', 'Senin', (8, 10))
jadwal.tambah_jadwal('Dosen B', 'Algoritma dan Struktur Data', 'Informatika', 'Senin', (8, 10))  # Permintaan yang bentrok
jadwal.tambah_jadwal('Dosen C', 'Manajemen Basis Data', 'Sistem Informasi', 'Selasa', (10, 12))
jadwal.tambah_jadwal('Dosen D', 'Sistem Operasi', 'Sistem Informasi', 'Selasa', (10, 12))  # Permintaan yang bentrok
jadwal.tambah_jadwal('Dosen A', 'Bahasa Indonesia', 'Informatika', 'Rabu', (13, 15))
jadwal.tampilkan_jadwal()