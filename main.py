def luas_lingkaran(phi, r):
    result = phi * r ** 2
    return result

print(luas_lingkaran(3.14, 8))  

first_name = "John"
last_name = "Doe"
age = 18
is_mariage = True
amount_money = 1000.0

print(first_name, last_name, age, is_mariage, amount_money)
print(f"{first_name} {last_name} {age} {is_mariage} {amount_money}")
print("%s %s, %d" % (first_name, last_name, age))
print("{} {} {}". format(first_name, last_name, age))