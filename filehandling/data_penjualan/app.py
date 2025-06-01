import pandas as pd 

file_path = 'filehandling\data_penjualan\data_penjualan.xlsx'

# Tugas Perama
df = pd.read_excel(file_path, sheet_name='Penjualan')
print(df.head())

# Tugas kedua
df['Total Harga'] = df['Jumlah'] * df['Harga Satuan']
print(df.head())

# Tugas ketiga
df_elektronik = df[df['Kategori'] == 'Elektronik']
df_elektronik.to_excel('filehandling\data_penjualan\df_elektronik.xlsx', index=False)

# Tugas keempat
total_pendapatan = df.groupby('Kategori')['Total Harga'].sum().reset_index()
total_pendapatan.columns = ['Kategori', 'Total Pendapatan']
total_pendapatan.to_excel("filehandling\data_penjualan\Total_pendaptan.xlsx", index=False)
print(total_pendapatan)

# Tugas kelima
df_sorted = df.sort_values(by='Total Harga', ascending=False)
df_sorted.to_excel('filehandling\data_penjualan\penjualan_terurut.xlsx', index=False)

