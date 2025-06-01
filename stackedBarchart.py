import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Stacked Vertical Bar Chart")

# NAMA ANGGOTA

st.subheader("Anggota Kelompok:")
st.markdown("""
1. **Wulan Ramadani** 
2. **Zahra Paharani**  
3. **Siti Fadila Siregar** 
""")
# Data
stores = ['Store A', 'Store B', 'Store C']
male_population = [150, 200, 180]
female_population = [120, 230, 170]

# Grafik
fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, male_population, label='Male', color='blue')
ax.bar(x, female_population, bottom=male_population, label='Female', color='pink')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_title('Population by Gender and Store')
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend()

# Tampilkan di Streamlit
st.pyplot(fig)


st.subheader('membuat Stacked Vertical Bar chart dengan Matplotlib')

# # Data Transaksi
# stores = ['Store A', 'Store B', 'Store C']
# product_a_sales = [200, 250, 300]
# product_b_sales = [150, 200, 250]

# fig, ax = plt.subplots()
# x = np.arange(len(stores))
# ax.bar(x, product_a_sales, label='Product A', color='blue')
# ax.bar(x, product_b_sales, label='Product B', color='green')

# ax.set_xlabel('stor')
# ax.set_ylabel('Sales')
# ax.set_title('Sales Transaction by Store')
# ax.set_xticklabels(x)
# ax.set_xticklabels(stores)
# ax.legend()

# # Tampilkan 
# st.pyplot(fig)


# st.subheader("Kustomisasi Stacked Vertical Bar Chart")

# # for i in range(len(x)):
# #     plt.text(x[i], product_a_sales[i] / 2, str(product_a_sales[i]), ha='center', color='white')
# #     plt.text(x[i], product_a_sales[i] + product_b_sales[i] / 2, str(product_b_sales[i]), ha='center', color='blue')

# for i in range(len(x)):
#     # Label untuk Product A (biru)
#     plt.text(x[i], product_a_sales[i] / 2, str(product_a_sales[i]), ha='center', color='white')

#     # Label untuk Product B (hijau)
#     plt.text(x[i], product_a_sales[i] + product_b_sales[i] / 2, str(product_b_sales[i]), ha='center', color='black')


# st.pyplot(fig)

# Data Transaksi
stores = ['Store A', 'Store B', 'Store C']
product_a_sales = [200, 250, 300]
product_b_sales = [150, 200, 250]

fig, ax = plt.subplots()
x = np.arange(len(stores))

# Stacked Bar Chart
ax.bar(x, product_a_sales, label='Product A', color='blue')
ax.bar(x, product_b_sales, bottom=product_a_sales, label='Product B', color='green')

ax.set_xlabel('Store')
ax.set_ylabel('Sales')
ax.set_title('Sales Transaction by Store')
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend()

# Label tengah batang
for i in range(len(x)):
    # Tengah batang Product A
    plt.text(x[i], product_a_sales[i] / 2, str(product_a_sales[i]), ha='center', color='white')
    # Tengah batang Product B (di atas Product A)
    plt.text(x[i], product_a_sales[i] + product_b_sales[i] / 2, str(product_b_sales[i]), ha='center', color='black')

# Tampilkan
st.pyplot(fig)

