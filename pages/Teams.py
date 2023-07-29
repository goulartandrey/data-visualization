import streamlit as st

#Configurações da página
st.set_page_config(
    page_title='Teams',
    page_icon="🏃⚽",
    layout="wide"
)

#CSS para esconder o footer e hamburgues streamlit
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


#Carregando dados e aplicando filtro
df = st.session_state["data"]
clubes = df["Club"].value_counts().index.sort_values(ascending=True)
club = st.sidebar.selectbox("Clube", clubes)
df_filter = df[df["Club"] == club].set_index("Name")


#Display Foto e nome do time
st.image(df_filter.iloc[0]["Club Logo"])
st.markdown(f"## {'Clube'}")


#Colunas para posterior filtragem
columns = ['Photo', 'Age', 'Club', 'Nationality', 'Flag', 'Overall',
             'Value', 'Wage', 'Position', 'Height', 'Weight', 'Release Clause' ]

#Função para pegar apenas a posição do jogador
def clean(x):
    try:
        return x.split('>')[1]
    except:
        return 'NA'

df_filter['Position'] = df_filter['Position'].apply(clean)


#Display do DataFrame na página
st.dataframe(df_filter[columns],
    column_config={
    "Overall":st.column_config.ProgressColumn("Overall", format="%d", min_value=0, max_value=100),
    #"Value":st.column_config.NumberColumn(),
    #"Wage":st.column_config.ProgressColumn("Wage", format="£%f", min_value=0, max_value=100000000),
    "Photo":st.column_config.ImageColumn(),
    "Flag":st.column_config.ImageColumn("Country")
    },
    height=700
)