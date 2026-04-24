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

st.write("Technicienne Superieur en Geomatique et Geographe Spécialisée dans la Topographie,la Cartographie,"
         "l'Analyse Spatiale Dessin Plan et la Programmation")



# Diplômes
st.header("Diplômes")
st.write("licence en Geographie à l'université Cheikh Anta diop De Dakar")
st.write("Brevret Technicien Superieur en Geomatique au Centre D'entrepreneuriat Developpement Technique le G15")
st.write("Baccalaureat à l'université Cheikh Anta Diop")

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
