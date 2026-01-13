import streamlit as st

# Configurazione iniziale
st.set_page_config(page_title="Il mio Diario del Vino", page_icon="🍷")

st.title("🍷 Il mio Diario del Vino")
st.write("L'app è stata creata correttamente!")

# Campi di prova
nome = st.text_input("Nome del vino")
voto = st.slider("Voto", 1, 10, 5)

if st.button("Salva"):
    st.success(f"Hai inserito {nome} con voto {voto}")
