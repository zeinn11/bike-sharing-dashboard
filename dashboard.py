import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('main_data.csv', sep=';')

df['dteday'] = pd.to_datetime(df['dteday'])

df['weathersit'] = df['weathersit'].map({
    1: 'Cerah',
    2: 'Berawan',
    3: 'Hujan Ringan',
    4: 'Hujan Lebat'
})

st.title('Dashboard Bike Sharing 🚴')

st.subheader('Trend Penyewaan')
st.line_chart(df.set_index('dteday')['cnt'])

st.subheader('Pengaruh Cuaca')
fig, ax = plt.subplots()
sns.barplot(x='weathersit', y='cnt', data=df, ax=ax)
st.pyplot(fig)
