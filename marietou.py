import streamlit as st

# Configuration de la page
st.set_page_config(page_title="CV - Marietou Diop", layout="wide")

# --- SIDEBAR (colonne gauche) ---
with st.sidebar:

    st.markdown("## MARIETOU DIOP")
    st.write("TECHNICIENNE SUPERIEUR EN GEOMATIQUE ET GEOGRAPHE")
    st.write("📍 Adresse : DAKAR / SENEGAL")
    st.write("✉️ Email : mdiop4602@gmail.com")
    
# --- CONTENU PRINCIPAL ---
st.title("MARIETOU DIOP")

st.write("technicienne superieur en geomatique et geographe spécialisée dans la topographie,la cartographie,"
         "l'analyse spatiale dessin plan et la programmation")



# Diplômes
st.header("Diplômes")
st.write("licence en geographie à l'université cheikh Anta diop de dakar")
st.write("brevret technicien superieur en geomatique au centre d'entrepreneuriat developpement technique le G15")
st.write("baccalaureat à l'université cheikh anta diop")

# Compétences
st.header("Compétences")
st.write("""
- Informatique : Bonne maîtrise de Word (saisie de texte)  
- Gestion des ventes (commerce)  
- Cours de français à domicile
- Streamlit
- ArcGIS
- Analyse spatiale
- Cartographie thématique
- Word
- Power point
- Excel
- Manipulation de données
- Structuration de bases de données
""")
