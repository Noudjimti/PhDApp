import streamlit as st
from PIL import Image
import numpy as np
import datetime
from math import pi, pow

    
def Read_Image_C(Path):
        image = Image.open(Path)
        image = image.resize((300, 150))
        return image


def G_Conventionnel(): 
    
    Altitude_C = st.number_input("Entrez l'altitude de la ville (m)", min_value = 0.0)
    Nombre_C = st.number_input("Entrez le nombre de groupe", min_value = 0)
        
    Transformateur_C = []
    Puissance_C = []
    Temps_C = []
    Duree_C = []
   
    for i in range(Nombre_C):
        message = f"Les parametres du groupe {i+1}"
        st.html(f"<div><h2>{message}</h2></div>")
        Puissance_C.append(st.number_input(f"Entrez la puissance active du groupe {i+1} (kW)", min_value = 0.0))
        Transformateur_C.append(st.number_input(f"Entrez le rendement du transformateur {i+1}", min_value = 0.0))
        Temps_C.append(st.number_input(f"Entrez le temps de fonctionnement prévu pour le groupe {i+1} (H)", min_value = 0))
        duree_c = st.time_input(f"Entrez l'heure de début de fonctionnement du groupe {i+1}", datetime.time(0), step=(900*4))
        Duree_C.append(duree_c.strftime("%H%M"))
        
    Transformateur_C = np.array(Transformateur_C)
    Puissance_C = np.array(Puissance_C)  
    if Altitude_C > 1000:
        return (1 - 0.01*(Altitude_C - 1000)/100)*Puissance_C*Transformateur_C,  Temps_C, Duree_C, Nombre_C
    else : return Puissance_C*Transformateur_C,  Temps_C, Duree_C, Nombre_C


def G_Photovoltaique():
    
    Puissance_P = st.number_input("Entrez la puissance crete de la centrale (kWp)", min_value = 0.0)
    rendement_P = st.number_input("Entrez le rendement de conversion de la centrale solaire", min_value = 0.0)
    Coef_Temp_P = st.number_input("Entrez le coefficient de déplétion de la puissance (kW/°C)", min_value = 0.0)
    Betha = st.number_input("Entrez l'angle d'inclinaison des modules (°)", min_value = 0.0)

    return Puissance_P*rendement_P, Coef_Temp_P, Betha
    
    
def G_Eolienne():
    
    Nombre_E = st.number_input("Entrez le nombre de mats", min_value = 0)
    Diametre_E = st.number_input("Entrez le diametre des pales (m)", min_value = 0.0)
    rendement_E = st.number_input("Entrez le rendement de conversion de la centrale éolienne", min_value = 0.0)
    Coef_E = st.number_input("Entrez le coefficient cp", min_value = 0.0)
    Hauteur_E = st.number_input("Entrez la hauteur (m)", min_value = 0.0)
    Vmin_E = st.number_input("Entrez la vitesse minimale de fonctionnement (m/s)", min_value = 0.0)
    Vmax_E = st.number_input("Entrez la vitesse maximale de fonctionnement (m/s)", min_value = 0.0)
    ro = 1.3

    return (Nombre_E*(pi*pow(Diametre_E, 2)/4)*Coef_E*rendement_E*ro)/2, Hauteur_E, Vmin_E, Vmax_E
