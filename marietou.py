import streamlit as st

# Configuration de la page
st.set_page_config(page_title="CV - Marietou Diop", layout="wide")

# --- SIDEBAR (colonne gauche) ---
with st.sidebar:
    # Appliquer un style CSS pour l'arrière-plan
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            background-color: #0b1a39; /* Bleu foncé */
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## TECHNICIENNE SUPERIEUR EN GEOMATIQUE ET GEOGRAPHE")
    st.write("📍 Adresse : DAKAR / SENEGAL")
    st.write("✉️ Email : mdiop4602@gmail.com")

    # Langues
    st.header("Langues")
    st.markdown("* Français: Avancé")
    st.markdown("* Anglais: Intermédiaire")
    st.divider()

    # Centre d'intérêt
    st.header("Centre d'intérêt")
    st.markdown("* Lecture")
    st.markdown("* Sport")  # Ajout du sport

# --- CONTENU PRINCIPAL ---
st.title("MARIETOU DIOP")

st.title("Profil")
st.write("Technicienne Supérieur en Géomatique et Géographe Spécialisée dans la Topographie, la Cartographie, "
         "l'Analyse Spatiale, Dessin Plan et la Programmation")

# Diplômes
st.header("Diplômes")
st.write("Licence en Géographie à l'université Cheikh Anta Diop de Dakar")
st.write("Brevet Technicien Supérieur en Géomatique au Centre d'Entrepreneuriat Développement Technique le G15")
st.write("Baccalauréat à l'université Cheikh Anta Diop")

# Compétences
st.header("Compétences")
st.write("""
- Informatique bureautique  
- Gestion des ventes (commerce)  
- Modélisation  
- Numérisation  
- Cours de français à domicile  
- Streamlit  
- ArcGIS  
- Analyse spatiale  
- Cartographie  
- Manipulation de données  
- Structuration de bases de données  
""")
