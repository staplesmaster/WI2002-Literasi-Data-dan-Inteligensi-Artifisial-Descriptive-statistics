import pandas as pd

# Load data
df = pd.read_csv("Dataset/Dataset_Global_Cybersecurity_Threats_Noisy.csv")

# Simpan jumlah awal
initial_rows = len(df)

# Hapus duplikat
df = df.drop_duplicates()
after_dedup_rows = len(df)
deleted_duplicates = initial_rows - after_dedup_rows

# Hapus baris yang mengandung NA
df = df.dropna()
after_deNA_rows = len(df)
deleted_na = after_dedup_rows - after_deNA_rows

# Pastikan kolom Year numerik
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

# Hapus baris dengan Year > 2025
df = df[df['Year'] <= 2025]
final_rows = len(df)
deleted_Years = after_deNA_rows - final_rows

# Total yang dihapus
total_deleted = deleted_duplicates + deleted_na + deleted_Years

# Cetak hasil
print(f"Total awal: {initial_rows}")
print(f"Duplikat yang dihapus: {deleted_duplicates}")
print(f"Baris yang mengandung NA dihapus: {deleted_na}")
print(f"Baris dengan Year > 2025: {deleted_Years}")
print(f"Total baris akhir: {final_rows}")
print(f"Total baris yang dihapus: {total_deleted}")

# Simpan hasil
df.to_csv('Dataset/Dataset_Global_Cybersecurity_Threats_Cleaned.csv', index=False)

#python3 Data_Cleaning/Dataset_Global_Cybersecurity_Threats.py