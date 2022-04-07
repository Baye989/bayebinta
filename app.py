import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

import json

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
# def load_lottiefile(filepath: str):
#     with open(filepath, "r") as f:
#         return json.load(f)
#
# lottie_codding = load_lottiefile("w.json.json")
#
#
# st_lottie(
#     lottie_codding,
#     speed=1,
#     reverse=False,
#     loop=True,
#     quality="low",
#     key=None,
#
# )

lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_0yfsb3a1.json")
img_contact_form = Image.open("images/projet2.PNG")
img_lottie_animation = Image.open("images/projet1.PNG")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Bonjour, Nous somme BD-BMS :wave:")
    st.title("Des data analyst sénégalais")
    st.write(
        "Nous somme passionné par la recherche de moyens d'utiliser l'intelligence artificielle pour rendre l'agriculture plus efficace, plus précise"
    )
    st.write("[Voir plus >](https://www.crossdata.tech/les-reponses-de-lintelligence-artificielle-face-aux-enjeux-agricoles/#:~:text=L'IA%20s'av%C3%A8re%20donc,certains%20co%C3%BBts%20de%20production%20etc.)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Ce que nous faisons")
        st.write("##")
        st.write(
            """
            Dans notre entreprises, nous aidons les personnes qui:\n
            -veulent prédir leur rendement.\n
            -veulent détecter la maladie des cultures.\n
            -veulent avoir une visualisation totale de leurs donnéés.\n
            -veulent prédire les précipitations.\n
            -veulent avoir la météo.\n
            -veulent faire l'analyse de données et la science des données.\n
            -veulent vendre ou acheter des produits en ligne...
            
            """
        )
        # st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Nos project")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Machine Learning appliqué dans le secteur agricole")
        st.write(
            """
            Utiliser le Machine Learning pour faire toutes sortes de prédictions dans le secteur agricole.
            """
        )
        # st.markdown("[Tester l'applicqtion...]("")")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Application de e-commerce")
        st.write(
            """
            Acheter des produits seins et frais au sein de notre exploitation.
            """
        )
        # st.markdown("[Entrer dans l'application...]("")")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Entrez en contact avec nous!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/bayebaye398@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Votre Nom et Prénom" required>
        <input type="email" name="email" placeholder="Votre email" required>
        <input type="text" name="call" placeholder="Votre numéro" required>
        <input type="email" name="address" placeholder="Votre adresse" required>
        <textarea name="message" placeholder="Ici votre message" required></textarea>
        <button type="submit">Envoyer</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
