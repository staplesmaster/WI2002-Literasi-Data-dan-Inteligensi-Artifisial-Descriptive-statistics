import pandas as pd

# Load dataset
file_path = "Dataset/Dataset_Cyber_Security_Indexes_Noisy.csv"
df = pd.read_csv(file_path)

# Simpan jumlah baris awal
jumlah_awal = len(df)

# Hapus duplikat
df = df.drop_duplicates()
jumlah_setelah_dedup = len(df)
jumlah_duplikat_dihapus = jumlah_awal - jumlah_setelah_dedup

# Hapus baris yang mengandung nilai kosong (NA)
df = df.dropna()
jumlah_akhir = len(df)
jumlah_na_dihapus = jumlah_setelah_dedup - jumlah_akhir

# Hitung total baris yang dihapus
total_dihapus = jumlah_duplikat_dihapus + jumlah_na_dihapus

# Tampilkan ringkasan hasil
print("=" * 40)
print("📊 Ringkasan Pembersihan Dataset")
print("=" * 40)
print(f"📂 Total baris awal            : {jumlah_awal}")
print(f"❌ Duplikat yang dihapus       : {jumlah_duplikat_dihapus}")
print(f"⚠️  Baris dengan NA yang dihapus : {jumlah_na_dihapus}")
print(f"✅ Total baris akhir           : {jumlah_akhir}")
print(f"🧹 Total baris yang dihapus    : {total_dihapus}")
print("=" * 40)

# Simpan dataset yang telah dibersihkan
output_path = "Dataset/Dataset_Cyber_Security_Indexes_Cleaned.csv"
df.to_csv(output_path, index=False)

#python3 Data_Cleaning/Dataset_Cyber_Security_Indexes.py