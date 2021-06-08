import numpy as np
import pandas as pd
import time
import math
import streamlit as st 
from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import streamlit as st
import streamlit as st
import base64

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



def download_link(object_to_download, download_filename, download_link_text):
    if isinstance(object_to_download,pd.DataFrame):
        object_to_download = object_to_download.to_csv(index=False)
    # some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(object_to_download.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'

def alert():
    return(st.warning('Não aceitamos valores em branco ou negativos'))





name = st.sidebar.selectbox(
    'Conversor de unidades',
    ('Unidades de Força e Pressão', 'Unidades de Comprimento')
)
             
if name == "Unidades de Comprimento":
    if st.sidebar.checkbox('Metros para Milíetros'):
        number1 = st.sidebar.number_input('Insira o valor em Metros')
        st.sidebar.write(f''' **{number1*1000}** Milímetros''')
    if st.sidebar.checkbox('Milímetros para Metros'):
        number2 = st.sidebar.number_input('Insira o valor em Milímetros')
        st.sidebar.write(f''' **{number2/1000}** Metros''')
        
if name == "Unidades de Força e Pressão":
    if st.sidebar.checkbox('Newtons/metro² para Pascal'):
        number3 = st.sidebar.number_input('Insira o valor em N/m²')
        st.sidebar.write(f''' **{number3*1}** Pa''')
    if st.sidebar.checkbox('Newtons para KiloNewtons'):
        number4 = st.sidebar.number_input('Insira o valor em N')
        st.sidebar.write(f''' **{number4/1000}** KN''')
    if st.sidebar.checkbox('Pascal para GigaPascal'):
        number5 = st.sidebar.number_input('Insira o valor em GigaPascal')
        st.sidebar.write(f''' **{number5/1000000000}** Pascal''') 
    if st.sidebar.checkbox('Pascal para MegaPascal'):
        number6 = st.sidebar.number_input('Insira o valor em MegaPascal')
        st.sidebar.write(f''' **{number6*1000000}** Pascal''')       
    if st.sidebar.checkbox('GigaPascal para Pascal'):
        number7 = st.sidebar.number_input('Insira o valor em GigaPascal')
        st.sidebar.write(f''' **{number7*1000000000}** Pascal''') 
    if st.sidebar.checkbox('MegaPascal para Pascal'):
        number8 = st.sidebar.number_input('Insira o valor em MegaPascal')
        st.sidebar.write(f''' **{number8*1000000}** Pascal''')           
            
    
#if st.sidebar.button('Código fonte'):
     
expander = st.sidebar.beta_expander("Autores do REMA")
expander.write(""" **Alcebiades Alves Barbosa Filho** \n
               Engenharia Física Mat: 201402442""")
expander.write("""**Ana Paula Moura Saran** \n 
               Engenharia de Computação Mat:201703703""")
expander.write(""" **Luiz Yokoyama Felix de Souza ** \n
                Engenharia de Computação Mat: 201602428""")
st.write(f"""
# Bem Vindo ao REMA
## Programa para ajudar o constutor civíl tomar decisões 
""")

st.write('''![fig](https://figrema.s3.amazonaws.com/rema-fig.jpg)''')

for i in range(1):
    diam = st.number_input("Por favor insira o valor (em metros) do diâmetro dos arames",step=1e-5,format="%.5f")
    if not diam or diam < 0:
        alert()
        st.stop() 
             
    carga_dist = st.number_input('Insira o valor (em KN/metro) da carga distribuída w',step=1)
    if not carga_dist or carga_dist < 0:
        alert()
        st.stop()

    escoamento = st.number_input('Por favor insira o valor (em MegaPascal) do limite de escoamento dos arames')
    if not escoamento or escoamento < 0:
        alert()
        st.stop()
         
    elasticidade = st.number_input('Por favor insira o valor (em GigaPascal) do Módulo de elasticidade dos arames')
    if not elasticidade or elasticidade < 0:
        alert()
        st.stop()
        
    a = st.number_input("Por favor insira o valor (em metros) da distância entre os pontos AB")
    if not a or a < 0:
        alert()
        st.stop()
        
    b = st.number_input("Por favor insira o valor (em metros) da distância entre os pontos BC")
    if not b or b < 0:
        alert()
        st.stop()
        
    c = st.number_input("Por favor insira o valor (em metros) da distância entre os pontos CG")
    if not c or c < 0:
        alert()
        st.stop()
        
    e = st.number_input("Por favor insira o valor (em metros) da distância entre os pontos EB")
    if e < 0 or not e:
        alert()
        st.stop() 
           
    d = st.number_input("Por favor insira o valor (em metros) da distância entre os pontos DC")
    if not d or d < 0 or d > e:
        st.warning('Lembrando que o comprimento DC tem que ser menor ou igual ao comprimento EB')
        alert()
        st.stop()  
       
#Conversão de unidades
carga_dist = carga_dist*1000 # Kilo
escoamento = escoamento*1000000 # Mega
elasticidade = elasticidade*1000000000 # Giga


        
ag = a+b+c; E = elasticidade; A = math.pi*diam**2/4; L_ab = a; L_ag = ag; L_eb = e

W = carga_dist; Fc = (((L_eb*W*(L_ag**2))/2) - L_ab*A*E*(d-e))/(a*d)+(e*(a+b)); Fb = (A*E*(d-e)+(d*Fc))/e; Fa = (W*L_ag-Fb-Fc)

temp_c = Fc/A; temp_b = Fb/A

my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.001)
    my_bar.progress(percent_complete + 1)

if temp_c > E and temp_b > E :
    st.warning("Os dois arames (DC e EB) ultrapassaram o limite de escoamento, tente novamente")
    st.stop() 
    
if temp_c > E  :
    st.warning("O arame DC ultrapassou o limite de escoamento, tente novamente")
    st.stop()
    
if temp_b > E :
    st.warning("O arame EB ultrapassou o limite de escoamento, tente novamente")
    st.stop()
        
else:
    st.warning("O arame não ultrapassou o limite")  

D_b=(Fb*L_eb)/(A*E); D_c=(Fc*d)/(A*E); D_g=(D_c*L_ag)/(a+b); E_eb=D_b/e;E_dc=D_c/d

st.write(f'''### Os deslocamentos dos pontos B, C e G são:
* Ponto B = **{round(D_b,5)}** m 
* Ponto C = **{round(D_c,5)}** m 
* Ponto G = **{round(D_g,5)}** m \n
---
### As deformações dos arames de apoio são: 
* Arame EB = **{round(E_eb,5)}** sem unidades  
* Arame DC = **{round(E_dc,5)}** sem unidades \n
---
### As reações de apoio são:
* No ponto A = **{abs(round(Fa,2))}** N 
* No ponto E = **{abs(round(Fb,2))}** N 
* No ponto D = **{abs(round(Fc,2))}** N
''')
   
output = f'''\t RESULTADO DO RELATÓRIO DO REMA \n
Os deslocamentos dos pontos B, C e G são:
B = {round(D_b,5)} m C = {round(D_c,5)} m G = {round(D_g,5)} m \n
As deformações dos arames de apoio são: 
Arame EB = {round(E_eb,5)} sem unidades Arame DC D = {round(E_dc,5)} sem unidades \n
As reações de apoio são:
No ponto A = {abs(round(Fa,2))} N E = {abs(round(Fb,2))} N D = {abs(round(Fc,2))} N
'''

if st.button('Download'):
    tmp_download_link = download_link(output, 'Resultado.txt', 'Clique aqui para baixar o resultado dessa análise em txt')
    st.markdown(tmp_download_link, unsafe_allow_html=True)