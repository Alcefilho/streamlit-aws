import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import streamlit as st 
import streamlit_wordcloud as wordcloud
from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from wordcloud import WordCloud, STOPWORDS

#############################################################################################
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  Usuario   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
#############################################################################################

#i) Valor da carga distribuída w;
#ii) Limite de escoamento dos arames;
#iii) Módulo de elasticidade dos arames;
#iv) Distância entre os pontos AB, BC e CG;
#v) Os comprimentos dos arrames de EB e DC, sendo que eles podem ter comprimentos diferentes.

#############################################################################################
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  Programa   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
#############################################################################################
#O cliente deseja elaborar a estrutura da imagem abaixo, para suportar um carregamento w de
#2000 kgf/m, sendo que ao ser aplicada a carga a viga AG permaneça na horizontal. Definir as dimensões dos
#elementos e materiais. A barra rígida AG é suportada por um pino em A e dois arames em B e C.

#i)Verificar se os arames ultrapassam o limite de escoamento do aço, caso isso ocorra o programa
#deverá avisar ao usuário que um ou os dois arames atingiram esse limite;
#ii) Informar as deformações dos arames;
#iii) Informar os deslocamentos dos pontos B, C e G
#iv) Informar as reações de apoio nos pontos A, E e D


#############################################################################################
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  Requisito   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
#############################################################################################
#i)Valores negativos da geometria do problema como comprimento e seção transversal;
#ii) Valores negativos de valores de caracterização dos materiais, como módulo de elaticidade
#tensão limite, entre outros;
#iii) Deverão deixar claro quais são as unidades de entrada para cada parâmetro e quais são as
#unidades de saída de seus resultados. Eliminando desta forma compreensões erradas;


st.write(f"""
# Bem Vindo ao REMA
## Programa para ajudar o constutor cívil tomar decisões 
""")
user_input = st.text_input("label goes here")
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