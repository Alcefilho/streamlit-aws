import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st 
import streamlit_wordcloud as wordcloud
from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from wordcloud import WordCloud, STOPWORDS


st.write(f"""
# Welcome!
This app is a demo od linkedin data :fire: :fire: 
# bye
""")
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True, type="csv")
for uploaded_file in uploaded_files:
     bytes_data = uploaded_file.read()
     st.write("filename:", uploaded_file.name)
     st.write(bytes_data)
#uploaded_file = st.file_uploader("text here", type="csv") 
df = pd.read_csv(uploaded_file)
summary = df.dropna(subset=['Position'], axis=0)['Position']
all_summary = ' '.join(s for s in summary)
wordcloud = WordCloud(stopwords=STOPWORDS, background_color='white', width=800, height=640).generate(all_summary)
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()
#plt.imshow(wordcloud)
st.pyplot(fig)
st.write(df)
st.write(f"""
:fire: :fire: 
""")
st.info("""
        :point_left: **To get started, choose a demo on the left sidebar.**
    """)
name = st.text_input('Name')
if not name:
    st.warning('Please input a name.')
    st.stop()
    st.success('Thank you for inputting a name.')


import streamlit as st

add_selectbox = st.sidebar.selectbox(
    "O que você quer averiguar?",
    ("Quem olhou meu perfil?", "Quais são meus amigos?", "Que profissão predomina meus amigos?")
)


#with st.beta_container():
#    st.write("This is inside the container")
#   # You can call any Streamlit command, including custom components:
#    st.bar_chart(np.random.randn(50, 3))
#st.write("This is outside the container")