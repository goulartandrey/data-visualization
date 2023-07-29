import streamlit as st
import pandas as pd

#Configuração da página
st.set_page_config(
    page_title='Home',
    page_icon="🏚",
    layout="wide"
)

#CSS para esconder o footer e o hamburguer streamlit
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .css-e3xfei {display: block; position: relative;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

#Guardando o DatFrame com os dados no state
if "data" not in st.session_state:
    df = pd.read_csv("datasets/FIFA23_official_data.csv")
    st.session_state["data"] = df


#Display da s informações na Home Page
st.write("# FIFA OFFICIAL DATASET! ⚽")
st.subheader("The dataset contains +17k unique players, general information and all KPIs the famous videogame offers. As the esport scene keeps rising espacially on FIFA, I thought it can be useful for the community (kagglers and/or gamers)")
st.sidebar.markdown("desenvolvido por [Goulart](https://github.com/goulartandrey)")
