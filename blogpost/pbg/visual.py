import pandas as pd
import matplotlib.pyplot as plt

# Data untuk tabel dan grafik
data = {
    "Tahun": [2021, 2022, 2023, 2024],
    "Total Pendapatan (M)": [2399.82, 2345.09, 2291.88, 2479.31],
    "Total Belanja (M)": [2234.95, 2343.43, 2368.32, 2748.31],
    "PAD (M)": [300.40, 261.45, 299.32, 504.51],
    "TKDD (M)": [1844.52, 1909.11, 1795.84, 1797.61],
    "Pendapatan Lainnya (M)": [254.90, 174.54, 196.72, 177.19],
    "Belanja Pegawai (M)": [845.32, 864.93, 892.76, 1250.42],
    "Belanja Barang dan Jasa (M)": [499.42, 524.49, 593.56, 564.08],
    "Belanja Modal (M)": [175.52, 230.17, 231.03, 293.11],
    "Belanja Lainnya (M)": [714.68, 723.84, 650.97, 640.70],
    "Pembiayaan (M)": [172.74, 316.31, 368.62, 292.35]
}

# Membuat DataFrame dari data
df = pd.DataFrame(data)

# Menampilkan tabel
print("Tabel Total Pendapatan dan Belanja:")
print(df[["Tahun", "Total Pendapatan (M)", "Total Belanja (M)"]])

print("\nTabel Struktur Pendapatan:")
print(df[["Tahun", "PAD (M)", "TKDD (M)", "Pendapatan Lainnya (M)"]])

print("\nTabel Struktur Belanja:")
print(df[["Tahun", "Belanja Pegawai (M)", "Belanja Barang dan Jasa (M)", "Belanja Modal (M)", "Belanja Lainnya (M)"]])

print("\nTabel Pembiayaan:")
print(df[["Tahun", "Pembiayaan (M)"]])

# Membuat grafik
plt.figure(figsize=(14, 10))

# Grafik Total Pendapatan dan Belanja
plt.subplot(2, 2, 1)
plt.plot(df["Tahun"], df["Total Pendapatan (M)"], marker='o', label="Total Pendapatan")
plt.plot(df["Tahun"], df["Total Belanja (M)"], marker='o', label="Total Belanja")
plt.title("Total Pendapatan dan Belanja (2021-2024)")
plt.xlabel("Tahun")
plt.ylabel("Jumlah (Miliar)")
plt.legend()
plt.grid()

# Grafik Struktur Pendapatan
plt.subplot(2, 2, 2)
plt.bar(df["Tahun"], df["PAD (M)"], label="PAD")
plt.bar(df["Tahun"], df["TKDD (M)"], bottom=df["PAD (M)"], label="TKDD")
plt.bar(df["Tahun"], df["Pendapatan Lainnya (M)"], bottom=df["PAD (M)"] + df["TKDD (M)"], label="Pendapatan Lainnya")
plt.title("Struktur Pendapatan (2021-2024)")
plt.xlabel("Tahun")
plt.ylabel("Jumlah (Miliar)")
plt.legend()
plt.grid()

# Grafik Struktur Belanja
plt.subplot(2, 2, 3)
plt.bar(df["Tahun"], df["Belanja Pegawai (M)"], label="Belanja Pegawai")
plt.bar(df["Tahun"], df["Belanja Barang dan Jasa (M)"], bottom=df["Belanja Pegawai (M)"], label="Belanja Barang dan Jasa")
plt.bar(df["Tahun"], df["Belanja Modal (M)"], bottom=df["Belanja Pegawai (M)"] + df["Belanja Barang dan Jasa (M)"], label="Belanja Modal")
plt.bar(df["Tahun"], df["Belanja Lainnya (M)"], bottom=df["Belanja Pegawai (M)"] + df["Belanja Barang dan Jasa (M)"] + df["Belanja Modal (M)"], label="Belanja Lainnya")
plt.title("Struktur Belanja (2021-2024)")
plt.xlabel("Tahun")
plt.ylabel("Jumlah (Miliar)")
plt.legend()
plt.grid()

# Grafik Pembiayaan
plt.subplot(2, 2, 4)
plt.plot(df["Tahun"], df["Pembiayaan (M)"], marker='o', color='red', label="Pembiayaan")
plt.title("Pembiayaan (2021-2024)")
plt.xlabel("Tahun")
plt.ylabel("Jumlah (Miliar)")
plt.legend()
plt.grid()

# Menampilkan grafik
plt.tight_layout()
plt.show()

df['Surplus/Defisit (M)'] = df['Total Pendapatan (M)'] - df['Total Belanja (M)']
plt.bar(df['Tahun'], df['Surplus/Defisit (M)'], color=df['Surplus/Defisit (M)'].apply(lambda x: 'green' if x >= 0 else 'red'))
plt.title("Surplus/Defisit APBD (2021-2024)")
plt.xlabel("Tahun")
plt.ylabel("Surplus/Defisit (Miliar)")
plt.grid(axis='y')
plt.show()

df['Pertumbuhan Pendapatan (%)'] = df['Total Pendapatan (M)'].pct_change() * 100
df['Pertumbuhan Belanja (%)'] = df['Total Belanja (M)'].pct_change() * 100
plt.plot(df['Tahun'], df['Pertumbuhan Pendapatan (%)'], marker='o', label="Pertumbuhan Pendapatan")
plt.plot(df['Tahun'], df['Pertumbuhan Belanja (%)'], marker='o', label="Pertumbuhan Belanja")
plt.title("Pertumbuhan Pendapatan dan Belanja (YoY %)")
plt.xlabel("Tahun")
plt.ylabel("Pertumbuhan (%)")
plt.legend()
plt.grid()
plt.show()

# Rata-rata komponen pendapatan
avg_pendapatan = df[['PAD (M)', 'TKDD (M)', 'Pendapatan Lainnya (M)']].mean()
plt.pie(avg_pendapatan, labels=avg_pendapatan.index, autopct='%1.1f%%', startangle=90)
plt.title("Rata-rata Komposisi Pendapatan (2021-2024)")
plt.show()

# Rata-rata komponen belanja
avg_belanja = df[['Belanja Pegawai (M)', 'Belanja Barang dan Jasa (M)', 'Belanja Modal (M)', 'Belanja Lainnya (M)']].mean()
plt.pie(avg_belanja, labels=avg_belanja.index, autopct='%1.1f%%', startangle=90)
plt.title("Rata-rata Komposisi Belanja (2021-2024)")
plt.show()

import seaborn as sns

# Hitung korelasi
corr = df.corr()

# Buat heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Heatmap Korelasi Antar Komponen APBD")
plt.show()

plt.bar(df['Tahun'] - 0.2, df['PAD (M)'], width=0.4, label='PAD')
plt.bar(df['Tahun'] + 0.2, df['TKDD (M)'], width=0.4, label='TKDD')
plt.title("Perbandingan PAD dan TKDD (2021-2024)")
plt.xlabel("Tahun")
plt.ylabel("Jumlah (Miliar)")
plt.legend()
plt.grid(axis='y')
plt.show()