import streamlit as st
from PIL import Image

def Read_Image_A():
    image_path = "EnR.jpg"
    image = Image.open(image_path)
    shape = image.size
    new_image = image.resize((shape[0], 250))
    return st.image(new_image, use_container_width = True)

def Read_Text_A():
    st.html("""<div><h1>Présentation</h1></div>""")
    with open("A_1.txt", 'r', encoding='Windows-1252', errors='replace') as file:
        A_1 = file.read()
    st.html(f"""<p style="font-size: 20px;">{A_1}<ul style="margin-left: 50px;"><li style="font-size: 20px;">Les données météorologiques
            </li><li style="font-size: 20px;">Les paramètres des différentes sources d’énergies</li></ul></p>""") #style ="background-color: rgb(23, 168, 233)"
def Schema_A():
    st.html("""<p style="font-size: 20px;">La representation du réseau électrique du type de réseaux électriques considérés peut etre resumé au schéma ci-dessous. " \
    "Selon les cas, il peut avoir un ou plusieurs sources d'énergies conventionnelles</p>""")
    image_path = "SchemaElectrique.jpg"
    image = Image.open(image_path)
    shape = image.size
    new_image = image.resize((shape[0], 600))
    return st.image(new_image) #use_container_width = True)