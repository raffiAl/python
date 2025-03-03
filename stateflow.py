# # # Tugas 1: Kondisi kompleks dengan operator logika. Done!

# # a = int(input("Masukan bilangan bulat: "))
# # b = int(input("Masukan bilangan bulat: "))
# # c = int(input("Masukan bilangan bulat: "))

# # def kondisi_kompleks(a, b, c):
# #   if (a > b or b > c):
# #    if (a % 2 == 0 and c % 2 != 0):
# #     if (b != c):
# #       print("Kondisi terpenuhi")
# #       return
    
# #   print("kondisi belum terpenuhi")
      
# # kondisi_kompleks(a, b, c)

# # # Tugas 2: Pengecekan type dengan operasi logika. Done!

# # def type_checker(string, integer, Ifloat):
# #   if isinstance(string, str):
# #     print("type input valid")
# #   else:
# #     print('type input invalid')

# #   if isinstance(integer, int):
# #     print("type input valid")
# #   else:
# #     print("type input invalid")

# #   if isinstance(Ifloat, float):
# #     print("type input valid")
# #   else:
# #     print("type input invalid")

# # type_checker('kucing', 80, 3.4)

# # # Tugas 3: Operator Logika dengan Nilai Boolean dan Konversi Tipe. Done!

# # def im_afunction(x, y):
# #   konversi_x = bool(x)
# #   konversi_y = bool(y)
 
# #   return(
# #     konversi_x and konversi_y,
# #     konversi_x or konversi_y,
# #     not konversi_x,
# #     x != y
# #   )

# # print(im_afunction(1, 1))

# # menentukan tahun kabisat

# tahun = int(input('masukan tahun: '))
# if (tahun % 4 == 0):
#     print('tahun %i merupakan tahun %s' %(tahun, 'kabisat'))
# else:
#   print('tahun %i bukan tahun %s' %(tahun, 'kabisat'))

# angka = int(input('masukan angka: '))
# if (angka == 0):
#    print('%i nol' %(angka))
# elif(angka < 0):
#    print('%i negatif' %(angka))
# elif(angka >= 1):
#    print('%i positif' %(angka))

# belanja = int(input('masukan total belanjaan anda: '))
# if(belanja > 100):
#    print('total belanja: %i' %(belanja))
#    print('selamat anda mendapatkan diskon 10%')
#    print('berikut update total belanjaan anda: ', belanja - (belanja * 10/100))
# elif(belanja > 50):
#    print('total belanja: %i' %(belanja))
#    print('selamat anda mendapatkan diskon 5%')
#    print('berikut update total belanjaan anda: ',  belanja - (belanja * 5/100))
# else:
#    print('total belanja: %i' %(belanja))
#    print('apa saya dapet diskon')
#    print('aduhh maaf ya anda tidak mendapatkan diskon')
