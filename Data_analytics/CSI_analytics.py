import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load CSV dengan penanganan koma dan baris rusak
df = pd.read_csv('../Dataset/Dataset_Cyber_Security_Indexes_Cleaned.csv', quotechar='"', on_bad_lines='skip')

# Paksa CEI dan NCSI menjadi numerik, abaikan baris error
df['CEI'] = pd.to_numeric(df['CEI'], errors='coerce')
df['NCSI'] = pd.to_numeric(df['NCSI'], errors='coerce')

# Hapus baris yang memiliki NaN setelah konversi
df = df.dropna(subset=['CEI', 'NCSI'])

# Ambil data numerik yang sudah bersih
x = df['CEI']
y = df['NCSI']

# Linear regression
slope, intercept, r, p, std_err = stats.linregress(x, y)

# Model fungsi
def model(x):
    return slope * x + intercept

y_model = list(map(model, x))

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, y_model, color='red', label=f'Regression Line\ny = {slope:.2f}x + {intercept:.2f}\n$R^2$ = {r**2:.3f}')
plt.xlabel('CEI (Cybersecurity Exposure Index)')
plt.ylabel('NCSI (National Cyber Security Index)')
plt.title('Linear Regression: CEI vs NCSI')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
