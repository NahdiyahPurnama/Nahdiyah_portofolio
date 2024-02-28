import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("Analisis Kualitas Udara di Indonesia dengan Standar ISPU")
    st.header("Pendahuluan")
    st.text("Kualitas udara sangat mempengaruhi kualitas kehidupan mahluk hidup dan lingkungan.")  
    st.text("Salah satu upaya pengendalian pencemaran udara yaitu memberi informasi tentang ") 
    st.text("kualitas udara. ISPU (Indeks Standar Pencemaran Udara) merupakan standar penggambaran ")
    st.text("kualitas udara. Dengan informasi yang diberikan kepada masyarakat dapat mengetahui")
    st.text("kualitas udara di daerah tersebut dan dapat melakukan tindakan untuk mencegah")
    st.text("dari dampak polusi udara.")

    st.header("Analisis")
    st.subheader("Presentase Polutan di Indonesia")
    
    # Membaca file CSV menggunakan path relatif
    df = pd.read_csv('ispunew.csv')
    
    # Data untuk pie chart
    labels = 'pm10', 'pm25', 'so2', 'co', 'o3', 'no2'
    sizes = [1.7, 1.3, 2.7, 87.8, 3.6, 2.9]
    
    # Membuat pie chart
    fig, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Memastikan pie chart digambar sebagai lingkaran

    # Menampilkan pie chart
    st.pyplot(fig)
    
    # Data untuk analisis ke-2
    st.header("Analisis")
    st.subheader("Presentase Polutan di Indonesia")
    
    top_10_highest = df.nlargest(10, 'index_ISPU')
    top_10_lowest = df.nsmallest(10, 'index_ISPU')

    # Membalik urutan data agar nilai tertinggi menjadi bar paling atas untuk 10 tertinggi
    top_10_highest = top_10_highest[::-1]

    # Membuat subplot untuk stasiun dengan index ISPU tertinggi
    fig, ax = plt.subplots(1, 2, figsize=(20, 8))

    bars1 = ax[0].barh(top_10_highest['id_stasiun'], top_10_highest['index_ISPU'], color='skyblue')
    ax[0].set_xlabel('Index ISPU')
    ax[0].set_title('Top 10 Stasiun dengan Nilai Index ISPU Tertinggi')

    # Menampilkan nilai index ISPU disamping bar
    for bar, value in zip(bars1, top_10_highest['index_ISPU']):
        ax[0].text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{value}', ha='left', va='center')

    # Membalik urutan data agar nilai tertinggi menjadi bar paling bawah untuk 10 terendah
    top_10_lowest = top_10_lowest[::-1]

    # Membuat subplot untuk stasiun dengan index ISPU terendah
    bars2 = ax[1].barh(top_10_lowest['id_stasiun'], top_10_lowest['index_ISPU'], color='lightgreen')
    ax[1].set_xlabel('Index ISPU')
    ax[1].set_title('Top 10 Stasiun dengan Nilai Index ISPU Terendah')

    # Menampilkan nilai index ISPU disamping bar
    for bar, value in zip(bars2, top_10_lowest['index_ISPU']):
        ax[1].text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{value}', ha='left', va='center')

    plt.tight_layout()  # Mengatur layout agar tidak tumpang tindih

    # Menampilkan plot menggunakan st.pyplot()
    st.pyplot(fig)

if __name__ == "_main_":
    main()