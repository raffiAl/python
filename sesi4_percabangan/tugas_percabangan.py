# MENENTUKAN TAHUN KABISAT

tahun = int(input('masukan tahun: '))
if (tahun % 4 == 0):
   print('tahun %i merupakan tahun %s' %(tahun, 'kabisat'))
else:
    print('tahun %i bukan tahun %s' %(tahun, 'kabisat'))

angka = int(input('masukan angka: '))
if (angka == 0):
   print('%i nol' %(angka))
elif(angka < 0):
   print('%i negatif' %(angka))
elif(angka >= 1):
   print('%i positif' %(angka))

# # DISCOUNT
   
belanja = int(input('masukan total belanjaan anda: '))
if(belanja > 100):
   print('total belanja: %i' %(belanja))
   print('selamat anda mendapatkan diskon 10%')
   print('berikut update total belanjaan anda: ', belanja - (belanja * 10/100))
elif(belanja > 50):
   print('total belanja: %i' %(belanja))
   print('selamat anda mendapatkan diskon 5%')
   print('berikut update total belanjaan anda: ',  belanja - (belanja * 5/100))
else:
   print('total belanja: %i' %(belanja))
   print('apa saya dapet diskon')
   print('aduhh maaf ya anda tidak mendapatkan diskon')

# PENGECEKAN NILAI
print(' ')
print('Pesyaratan lulus: ')
print(' ')
print('Nilai rata-rata > 75')
print('Hanya satu pelajaran yang < 70')
print('salah satu pelajaran mendapatkan nilai sempurna')
print(' ')

mtk = int(input('masukan nilai: '))
sains = int(input('masukan nilai: '))
inggris = int(input('masukan nilai: '))

rata_rata = (mtk + sains + inggris) / 3
nilai_70 = 0
nilai_100 = 0

# CHECK APAKAH ADA NILAI 100
if (mtk == 100 or sains == 100 or inggris == 100):
  nilai_100 += 1

# JIKA < 70
if (mtk < 70 ):
   nilai_70 += 1
if (sains < 70):
   nilai_70 += 1
if (inggris < 70):
   nilai_70 += 1        

# if (rata_rata >= 75):
#    if (nilai_70 <= 1):
#       if (nilai_100 >= 1):
#          print('')
#          print('LULUS')
#          print('')
#          print('Semua persyaratan terpenuhi')
#          print(f'Nilai rata-rata: {rata_rata} ✅')
#          print(f'Pelajaran dengan nilai < 70: {nilai_70} ✅')
#          print(f'pelajaran dengan nilai sempurna: {nilai_100} ✅')
#       else:
#          print(' ')
#          print('TIDAK LULUS')
#          print(' ')
#          print('Semua persyaratan harus terpenuhi')
#          print(f'Nilai rata-rata: {rata_rata} ✅')
#          print(f'Pelajaran dengan nilai < 70: {nilai_70} ✅')
#          print(f'Pelajaran dengan nilai sempurna: {nilai_100} ❌')
#    else:
#       print(' ')
#       print('TIDAK LULUS')
#       print(' ')
#       print('Semua persyaratan harus terpenuhi')
#       print(f'Nilai rata-rata: {rata_rata} ✅')
#       print(f'Pelajaran dengan nilai < 70: {nilai_70} ❌')
#       if (nilai_100 >= 1):
#          print(f'Pelajaran dengan nilai sempurna: {nilai_100} ✅')
#       else:
#          print(f'Pelajaran dengan nilai sempurna: {nilai_100} ❌')
# else:
#    print(' ')
#    print('TIDAK LULUS')
#    print(' ')
#    print('Semua persyaratan harus terpenuhi')
#    print(f'Nilai rata-rata: {rata_rata} ❌')
#    if (nilai_70 <= 1):
#       print(f'Pelajaran dengan nilai < 70: {nilai_70} ✅')
#    else: 
#       print(f'Pelajaran dengan nilai < 70: {nilai_70} ❌')
#    if (nilai_100 >= 1):
#       print(f'Pelajaran dengan nilai sempurna: {nilai_100} ✅')
#    else:
#       print(f'Pelajaran dengan nilai sempurna: {nilai_100} ❌')
#    CODE SEBELUM DI OPTIMASI

#    CODE SETELAH DI OPTIMASI
def checkKelulusan(rata_rata, nilai_70, nilai_100):
   status = 'LULUS'if rata_rata >= 75 and nilai_70 <= 1 and nilai_100 >= 1 else 'TIDAK LULUS'

   print(' ')
   print('Semua persyaratan terpenuhi' if status == 'LULUS' else 'Semua persyaratan harus terpenuhi')
   print(status)
   print(' ')
   print(f'Nilai rata-rata: {rata_rata} {'✅' if rata_rata >= 75 else '❌'}')
   print(f'Pelajaran dengan nilai < 70: {nilai_70} {'✅' if nilai_70 <= 1 else '❌'}')
   print(f'Pelajaran dengan nilai sempurna: {nilai_100} {'✅' if nilai_100 >= 1 else '❌'}')
checkKelulusan(rata_rata, nilai_70, nilai_100)
 