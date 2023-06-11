import streamlit as st
import numpy as np
import pandas as pd
from scipy.stats import t

def perform_parameter_test(sample_data, population_mean, alpha):
    sample_mean = np.mean(sample_data)
    sample_std = np.std(sample_data, ddof=1)
    sample_size = len(sample_data)
    
    # Menghitung t-score dan p-value
    t_score = (sample_mean - population_mean) / (sample_std / np.sqrt(sample_size))
    p_value = t.sf(np.abs(t_score), sample_size-1) * 2
    
    # Membandingkan p-value dengan tingkat signifikansi (alpha)
    if p_value < alpha:
        result = "Reject Null Hypothesis"
    else:
        result = "Fail to Reject Null Hypothesis"
    
    # Menghasilkan hasil uji estimasi
    result_dict = {
        'Sample Mean': sample_mean,
        'Sample Size': sample_size,
        't-Score': t_score,
        'p-Value': p_value,
        'Significance Level (alpha)': alpha,
        'Result': result
    }
    return result_dict

def main():
    # Judul aplikasi
    st.title("Uji Estimasi Parameter Test")

    # Input variabel
    sample_data = st.text_input("Masukkan data sampel (pisahkan dengan koma):")
    population_mean = st.number_input("Masukkan rata-rata populasi:")
    alpha = st.number_input("Masukkan tingkat signifikansi (alpha):")

    # Konversi data sampel menjadi array
    sample_data = np.fromstring(sample_data, sep=',')

    # Melakukan uji estimasi jika data sampel telah diinput
    if len(sample_data) > 0:
        result = perform_parameter_test(sample_data, population_mean, alpha)

        # Menampilkan hasil uji estimasi dalam tabel
        df_result = pd.DataFrame(result, index=[0])
        st.write("Hasil Uji Estimasi:")
        st.dataframe(df_result)

        # Menghitung p-value berdasarkan alpha
        p_alpha = (1 - alpha) * 100
        st.write(f"p-Value < {alpha}: {p_alpha}%")

if __name__ == "__main__":
    main()
