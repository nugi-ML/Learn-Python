import streamlit as st
import datetime
import pandas as pd

# Text Input
name = st.text_input(label='Nama lengkap', value='')
st.write('Nama: ',name)

# Text-area
text = st.text_area('Feedback')
st.write('Feedback: ', text)

# Number input
number = st.number_input(label='Umur')
st.write(f'Umur {int(number)} tahun')

# Date Input
date = st.date_input(label='Tanggal lahir', min_value=datetime.date(1900,1,1))
st.write(f'Tanggal lahir {date}')

# File Uploader
uploaded_file = st.file_uploader('Choose a CSV file')
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

# Camera input
picture = st.camera_input('Take a picture')
if picture:
    st.image(picture)