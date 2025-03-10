# is_bayar = False
# rata_rata = False

# user_bayar = input('Pembayaran truee/false?: ')
# nilai = input('Masukan nilai truee/false?: ')

# is_bayar = bool(1 if user_bayar == 'true' else 0)
# rata_rata = bool(1 if nilai == 'true' else 0)

# def cek_kelulusan(bayaran, rata_rata) :
#   status = 'LULUS' if bayaran and rata_rata else 'TIDAK LULUS'
#   print(status)

# cek_kelulusan(is_bayar, rata_rata)

# # APP2 KATEGORI USIA

# usia = int(input('masukan usia: '))
# print('Bayi'if  usia <= 2 else 'Balita' if usia <= 5 else 'Anak_anak' if usia <= 12 else 'Remaja' if usia <= 18 else 'Dewasa') 

# HITUNG PAJAK 

njkb = int(input('masukan nilai jual kendaraan bermotor (NJKB): '))
jenis_kendaraan  = input('masukan jenis kendaraan mobil/motor: ')
kepemilikan_kendaraan = []
pkb = 0
motor = 35000
mobil = 143000

def hitung_pajak(count, njkb) :
  state = 2

  for i in range(count) :
    kepemilikan_kendaraan.append(state)
    state += 0.5
  
  for i in (kepemilikan_kendaraan) :
    pkb = njkb - (njkb * (i/len(kepemilikan_kendaraan)))
    pkb += motor if jenis_kendaraan == 'motor' else mobil
    return pkb

print(hitung_pajak(5, njkb))

