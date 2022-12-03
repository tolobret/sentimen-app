import model_job as model
import predict_text as predict
import streamlit as st
import time
import webbrowser

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

# url = 'https://datastudio.google.com/reporting/defe47e1-3401-4820-97a2-93ac0c6d19b0'
link=' ### Buka Halaman Dashboard Analisis : [Dashboard](https://datastudio.google.com/reporting/defe47e1-3401-4820-97a2-93ac0c6d19b0)'
st.markdown(link,unsafe_allow_html=True)
# if st.button('Buka Halaman Dashboard Analisis'):
#     webbrowser.open_new_tab(url)
st.caption('Update data dashboard membutuhkan waktu 15-60 menit atau klik refresh data pada tombol option (⋮)')

if st.button('Mulai Analisis Data Ulasan Terbaru'):    
    with st.spinner('Sedang mengambil teks ulasan ...'):
        data=model.job()
        st.success('Success!')
    st.subheader('Hasil Analisis Data Ulasan Terbaru')
    st.table(data)
else:
    st.write('')

