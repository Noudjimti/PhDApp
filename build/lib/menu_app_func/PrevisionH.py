import streamlit as st
from PIL import Image

def Read_Image_PH():
    image_path = "Weather.jpg"
    image = Image.open(image_path)
    shape = image.size
    new_image = image.resize((shape[0], 200))
    return st.image(new_image, use_container_width = True)

def Parameters_PH(valeurs_defaut = []):
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)   
    #Parametres = []
    Param_1 = []
    Param_2 = []
    Param_3 = []
   
    nom_ligne_1 = ["Temperature", "Temperature r", "Temperature h", "Humidité s", "Humidité r", "Précipitation", "Pression"]
    nom_ligne_2 = ["Vent moy", "Irradiation cc", "Irradiation ghi", "Irradiation dni", "Irradiation-diff", "Couverture n", "Vent nord"]
    nom_ligne_3 = ["Vent ouest", "Vent sud", "Vent est", "Autaumn", "Printemps", "Eté"]

    if valeurs_defaut != []:
        PJ_val1 = valeurs_defaut[:7]
        PJ_val2 = valeurs_defaut[7:14]
        PJ_val3 = valeurs_defaut[14:]
    elif valeurs_defaut == [] :
        PJ_val1 = [0.0]*7
        PJ_val2 = [0.0]*7
        PJ_val3 = [0.0]*7
    
    for i, col in enumerate([col1, col2, col3, col4, col5, col6, col7]):
        with col:
            Param_1.append(st.number_input(f"{nom_ligne_1[i]}", value = PJ_val1[i], key= i+458)) #min_value = PJ_val1[i]
            Param_2.append(st.number_input(f"{nom_ligne_2[i]}", value = PJ_val2[i], key = 606+i)) #min_value = PJ_val2[i]
            if i != 6:
                Param_3.append(st.number_input(f"{nom_ligne_3[i]}", value = PJ_val3[i], key = i+160)) #min_value = PJ_val3[i],
        
    return Param_1 + Param_2 + Param_3


def VPrevision_PH(liste = []):
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    nom = ["Vent moy", "Temperature", "GHI", "DNI", "DHI"]

    if liste == []:
        liste = [0]*6
    
    for i, col in enumerate([col1, col2, col3, col4, col5]):
        with col:
            Toggle = st.toggle(nom[i], key = i+222, value = True)
            if Toggle:
                st.number_input("", value = liste[i], key = 1010+i)
            elif Toggle == False :
                st.number_input("", value = liste[i], key = 1010+i, disabled = True)


