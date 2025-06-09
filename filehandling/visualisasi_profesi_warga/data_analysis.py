import pandas as pd
import matplotlib.pyplot as plt

def plot_profesi_distribution(file_path):
  # Membaca data dan mengelempokan data berdasarkan profesi denga pandas
  df = pd.read_excel(file_path, sheet_name='Sheet1')
  groupedData = df.groupby('Profesi').size().reset_index(name='Jumlah')

  # Membuat pie chart dengan matplotlib

  # data untuk pie chart
  labels = groupedData['Profesi']
  sizes = groupedData['Jumlah']

  # membuat pie chart
  plt.figure(figsize=(10, 10))
  plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)

  # Judul chart
  plt.title('Distribusi jumlah orang berdasarkan profesi')

  # tampilkan diagram
  plt.show()

def comparison_of_education_and_gender(file_path):
  # read file 
  df = pd.read_excel(file_path, sheet_name='Sheet1')

  # grouping data base on last education and gender
  pivot_table = df.pivot_table(index='Pendidikan_Terakhir', columns='Jenis_Kelamin', aggfunc='size', fill_value=0)

  # create a bar chart
  plt.figure(figsize=(14, 10))
  pivot_table.plot(kind='bar', stacked=False, colormap=plt.cm.Paired)

  # title
  plt.title('Jumlah orang berdasarkan pendidikan terakhir dan jenis kelamin')
  plt.xlabel('Pendidikan_Terakhir')
  plt.ylabel('Jenis_Kelamin')

  # rotation
  plt.xticks(rotation=45, ha='right')

  # show bar 
  plt.tight_layout()
  plt.show()

# fungsi untuk mengkategorikan penghasilan
def kategorikan_penghasilan(df):
  # Mengkategorikan penghasilan ke dalam rentang tertentu
  bins = [0, 1000000 , 3000000, 10000000, float('inf')]
  labels = ['Rendah', 'Sedang', 'Tinggi', 'Sangat Tinggi']
  df['Kategori_Penghasilan'] = pd.cut(df['Penghasilan_Per_Bulan'], bins=bins, labels=labels, right=True)

def distribusi_penghasilan(file_path):
  # Membaca data dan mengelempokan data berdasarkan penghasilan
  df = pd.read_excel(file_path, sheet_name='Sheet1')
  kategorikan_penghasilan(df)
  groupedData = df.groupby('Kategori_Penghasilan').size().reset_index(name='Jumlah')

  # Membuat pie chart dengan matplotlib
  labels = groupedData['Kategori_Penghasilan']
  sizes = groupedData['Jumlah']

  plt.figure(figsize=(10, 10))
  plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
  plt.title('Distribusi jumlah orang berdasarkan kategori penghasilan')
  plt.show()