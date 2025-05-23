import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

#Membandingkan Financial Loss & Number of Affected user

# Load CSV dengan penanganan koma dan baris rusak
df = pd.read_csv('../Dataset/Dataset_Global_Cybersecurity_Threats_Cleaned.csv', quotechar='"', on_bad_lines='skip')

# Paksa CEI dan NCSI menjadi numerik, abaikan baris error
df['Financial Loss (in Million $)'] = pd.to_numeric(df['Financial Loss (in Million $)'], errors='coerce')
df['Number of Affected Users'] = pd.to_numeric(df['Number of Affected Users'], errors='coerce')

# Hapus baris yang memiliki NaN setelah konversi
df = df.dropna(subset=['Financial Loss (in Million $)', 'Number of Affected Users'])

# Ambil data numerik yang sudah bersih
x = df['Financial Loss (in Million $)']
y = df['Number of Affected Users']

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
plt.xlabel('Financial Loss (in Million $)')
plt.ylabel('Number of Affected Users')
plt.title('Linear Regression: Financial Loss vs Number of Affected Users')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
