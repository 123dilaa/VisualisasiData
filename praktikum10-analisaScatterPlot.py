import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Data dummy
data = {
    'Suhu': [20, 22, 24, 26, 28, 30, 32, 34, 36],
    'Penjualan_Cokelat': [50, 60, 70, 80, 90, 100, 110, 120, 130],
    'Penjualan_Vanila': [60, 70, 80, 90, 100, 110, 120, 130, 140],
    'Penjualan_Stroberi': [48, 56, 60, 70, 80, 90, 100, 110, 120],
    'Kelembapan': [65, 70, 75, 80, 85, 90, 95, 100, 100]
}

# Konversi data ke DataFrame
df = pd.DataFrame(data)

# Judul aplikasi
st.title('Analisis Penjualan Es Krim Berdasarkan Suhu')

st.markdown(
    """
    <style>
    .title {
        text-align: center;
        color: #d13661;
        font-size: 36px;
        font-family: 'Arial Rounded MT Bold', sans-serif;
        margin-bottom: 30px;
    }

    .box {
        background-color: #ffe0f0;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(214, 51, 132, 0.2);
        width: 70%;
        margin: 0 auto;
    }

    .anggota {
        font-size: 20px;
        font-weight: 500;
        font-family: 'Segoe UI', sans-serif;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Judul
st.markdown('<div class="title"> Daftar Nama Anggota Kelompok</div>', unsafe_allow_html=True)

# Daftar nama dalam box
st.markdown(
    """
    <div class="box">
        <div class="anggota">1. Wulan Ramadani</div>
        <div class="anggota">2. Siti Fadila Siregar</div>
        <div class="anggota">3. Zahra Pahrani</div>
    </div>
    """,
    unsafe_allow_html=True
)


# Pilih jenis es krim
jenis_eskrim = st.selectbox('Pilih Jenis Es Krim:', ['Cokelat', 'Vanila', 'Stroberi'])

# Menentukan kolom penjualan berdasarkan pilihan
if jenis_eskrim == 'Cokelat':
    penjualan = df['Penjualan_Cokelat']
elif jenis_eskrim == 'Vanila':
    penjualan = df['Penjualan_Vanila']
else:
    penjualan = df['Penjualan_Stroberi']

# Tampilkan tabel data
st.subheader('Data Penjualan dan Suhu')
st.dataframe(df)

# Membuat Scatter Plot
fig, ax = plt.subplots()
scatter = ax.scatter(df['Suhu'], penjualan, c=df['Kelembapan'], s=100, cmap='coolwarm', alpha=0.7)
ax.set_title(f'Hasil Penjualan {jenis_eskrim} vs Suhu dan Kelembapan')
ax.set_xlabel('Suhu (°C)')
ax.set_ylabel(f'Penjualan Es Krim ({jenis_eskrim})')
fig.colorbar(scatter, label='Kelembapan (%)')

# Tampilkan scatter plot di Streamlit
st.pyplot(fig)

# Ringkasan hubungan
st.subheader('Analisis Hubungan')
st.write(f'**Grafik menunjukkan hubungan antara suhu, kelembapan, dan penjualan es krim jenis **{jenis_eskrim}**.')
