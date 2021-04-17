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

uploaded_file = st.file_uploader("text here", type="csv") 
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
