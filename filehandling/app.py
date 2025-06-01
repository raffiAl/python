import pandas as pd
a = 3
b = 10
try:
  print(b/a)
except ZeroDivisionError:
  print("error: zero division")
print('program selesai')
