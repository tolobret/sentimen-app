import model_job as model
import predict_text as predict
import streamlit as st
import time

st.title('Analisis Sentimen Ulasan Pelanggan Warung Wareg')

st.header('Prediksi Sentimen dan Aspek Ulasan')
text = st.text_input('Masukkan Teks Ulasan', 'Makanan enak sekali')
if st.button('Mulai Analisis'):
    if text.strip()=='' :
        st.error('Cek kembali teks ulasan', icon="🚨")
    else:
        with st.spinner('Wait for it...'):
            time.sleep(0.1)
            st.success('Success!')
        
        teks_df = predict.job(text)
        st.table(teks_df)
else:
    st.write('')


st.header('Prediksi Sentimen dan Aspek Ulasan Google Review Terbaru')
if st.button('Mulai Analisis Data Ulasan Terbaru'):    
    with st.spinner('Sedang mengambil teks ulasan ...'):
        data=model.job()
        st.success('Success!')
    st.subheader('Hasil Analisis Data Ulasan Terbaru')
    st.table(data)
else:
    st.write('')