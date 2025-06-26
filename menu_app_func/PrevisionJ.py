import streamlit as st
from PIL import Image
    
def Read_Image_PJ():
    image_path = "Weather.jpg"
    image = Image.open(image_path)
    shape = image.size
    new_image = image.resize((shape[0], 200))
    return st.image(new_image, use_container_width = True)

def Parameters_PJ(valeurs_defaut = []): 
    col1, col2, col3, col4, col5, col6,  col7, col8 = st.columns(8)   
    
    Param_1 = []
    Param_2 = []
    Param_3 = []

    nom_ligne_1 = ["Temperature", "Temperature r", "Temperature h", "Humidité s",
                   "Humidité r", "Précipitation", "Pression", "Vent moy"]
    nom_ligne_2 = ["Temperature max", "Temperature min", "Vent max", "Vent min",
                   "Irradiation cc", "Irradiation ghi", "Irradiation dni", "Irradiation-diff"]
    nom_ligne_3 = ["Couverture n", "Vent nord", "Vent ouest", "Vent sud", 
                   "Vent est","Autaumn", "Printemps", "Eté"]
    
    if valeurs_defaut != []:
        PJ_val1 = valeurs_defaut[:8]
        PJ_val2 = valeurs_defaut[8:16]
        PJ_val3 = valeurs_defaut[16:]
    elif valeurs_defaut == []:
        PJ_val1 = [0.0]*8
        PJ_val2 = [0.0]*8
        PJ_val3 = [0.0]*8

    for i, col in enumerate([col1, col2, col3, col4, col5, col6,  col7, col8]):
        with col:
            Param_1.append(st.number_input(f"{nom_ligne_1[i]}", value = PJ_val1[i])) #min_value = PJ_val1[i]
            Param_2.append(st.number_input(f"{nom_ligne_2[i]}", value = PJ_val2[i])) # min_value = PJ_val2[i]
            Param_3.append(st.number_input(f"{nom_ligne_3[i]}", value = PJ_val3[i])) #min_value = PJ_val3[i]
        
    return Param_1 + Param_2 + Param_3

def VPrevision_PJ(liste = []):
    
    col1, col2, col3, col4, col5, col6, col7, col8= st.columns(8)  
    nom = ["Vent min", "Vent moy", "Vent max", "Couverture n", "Temperature", "GHI", "DNI", "DHI"]

    if liste == []:
        liste = [0]*8
    
    for i, col in enumerate([col1, col2, col3, col4, col5, col6, col7, col8]):
        with col:
            Toggle = st.toggle(nom[i], key = i, value = True)
            if Toggle:
                st.number_input("", value = liste[i], key = 1000+i)
            elif Toggle == False :
                st.number_input("", value = liste[i], key = 1000+i, disabled = True)





            