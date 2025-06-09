import sys

# path_folder
module_path = r'filehandling\visualisasi_profesi_warga'
sys.path.append(module_path)

# modul function
from data_analysis import plot_profesi_distribution
from data_analysis import comparison_of_education_and_gender

file_path = r'source\Data_Penduduk.xlsx'

plot_profesi_distribution(file_path)
comparison_of_education_and_gender(file_path)

