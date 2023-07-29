import streamlit as st

#Configurações da página
st.set_page_config(
    page_title='Players',
    page_icon="🏃‍♂️",
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
clubes = df['Club'].value_counts().index.sort_values(ascending=True)
club = st.sidebar.selectbox("Clube", clubes)
df_players = df[df['Club'] == club]
players = df_players["Name"].value_counts().index.sort_values(ascending=True)
player = st.sidebar.selectbox("Players", players)
player_stats = df[df['Name'] == player].iloc[0]


st.image(player_stats['Photo'])
st.title(f"{player_stats['Name']}")

st.markdown(f"**Clube** {player_stats['Club']}")
st.markdown(f"**Posição** {player_stats['Position'].split('>')[1]}")


col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade** {player_stats['Age']}")
col2.markdown(f"**Altura** {player_stats['Height']}")
col3.markdown(f"**Peso** {player_stats['Weight']}")

st.divider()
st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

col1, col2, col3 = st.columns(3)
col1.metric(label="Valor de mercado", value=player_stats['Value'])
col2.metric(label="Remuneração semanal", value=player_stats['Wage'])
col3.metric(label="Rescisão", value=player_stats['Release Clause'])