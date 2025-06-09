import sys
import os

# path_folder
module_path = os.path.join(os.path.dirname(__file__), 'visualisasi_profesi_warga')
sys.path.append(module_path)

# modul function
from data_analysis import plot_profesi_distribution, comparison_of_education_and_gender, distribusi_penghasilan

file_path = os.path.join('source', 'Data_Penduduk.xlsx')

plot_profesi_distribution(file_path)
comparison_of_education_and_gender(file_path)
distribusi_penghasilan(file_path)
