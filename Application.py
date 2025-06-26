import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from PIL import Image

from menu_app_func.Accueil import Read_Image_A, Read_Text_A, Schema_A
from menu_app_func.Meteo_Site import Display_Image_IS, Display_Data_IS, Render_Data_IS 
from menu_app_func.Configuration import Read_Image_C, G_Conventionnel, G_Photovoltaique, G_Eolienne
from menu_app_func.PrevisionJ import Read_Image_PJ, Parameters_PJ, VPrevision_PJ
from menu_app_func.PrevisionH import Parameters_PH, VPrevision_PH
from menu_app_func.VarMeteorologie import ModelePJ, ModelePH
from menu_app_func.Stockage import SideBarTable, G_ConventionnelTable, G_PhotovoltaiqueTable, G_EolienneTable, PredJTable, PredHTable, SDateTable #MeteoParamJTable, MeteoParamHTable
from menu_app_func.Recup_Stockage import SideBarData, G_ConventionnelData, G_PhotovoltaiqueData, G_EolienneData, PredJData, PredHData, SDateData #MeteoParamJData, MeteoParamHData
from menu_app_func.Visualisation import Viz_ParamMJV, Viz_ParamMHV, Viz_EnergyJV, Viz_EnergyHV
from datetime import datetime, timedelta 
from menu_app_func.EHFunction import JEnergie_Conv, JEnergie_PV, JEnergie_Eolienne, HEnergie_Conv, HEnergie_Eolienne, HEnergiePV


#APP
st.set_page_config(page_title="E-Forecast", page_icon="AppLogo.jpg", layout = "wide")
st.markdown("""<style>div.stButton > button {background-color: #5698E0;}</style>""", unsafe_allow_html=True)

#Side bar
st.sidebar.write("Données géographique site")
st.sidebar.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
Pays = ["Cameroun", "Congo", "Gabon", "Guinée Equatorial", "Tchad","RCA"]
villes_Tchad = ["Abeché", "N'Djaména", "Moundou", "Sarh"]
Selection_Pays = st.sidebar.selectbox('Pays', Pays)

if Selection_Pays == "Tchad":
    Selection_Ville = st.sidebar.selectbox('Ville', villes_Tchad)
else : 
    st.sidebar.selectbox('Ville', "")
    Selection_Ville = ""
Lat = st.sidebar.number_input("Entrez la latitude du site", min_value = 0.0)
Lon = st.sidebar.number_input("Entrez la longitude du site", min_value = 0.0)
STime = st.sidebar.text_input("Référenciel pour les prévisions (AAAAMMJJ HH)", value = f"{datetime.now().strftime('%Y%m%d %H')}")
SPrev_time = pd.to_datetime(STime.replace(" ", ""), format="%Y%m%d%H")
SPrev_time = SPrev_time + timedelta(days=1)
SBT_val = st.sidebar.button("Upload Data", key = 12500, use_container_width = True, icon = ":material/cloud_download:") #✅
if SBT_val :
    SideBarTable(f"{datetime.now().strftime('%Y%m%d%H')}", Selection_Pays, Selection_Ville, Lat, Lon)
    SDateTable(SPrev_time.strftime("%Y%m%d %H"), STime)

#Menu
Main_Menu = option_menu(None, ["Accueil", "Météo site", "Configuration", "Prévision","Visualisation", "Apropos"],
    icons=["house", "info-circle", "diagram-3-fill","graph-up-arrow", "display", "book"], 
    menu_icon="cast", default_index=0, styles = {"container" : {"width": "100%"}}, orientation="horizontal") #"Stockage"---"database-fill"

#Accueil
if Main_Menu == "Accueil" :
    Read_Image_A()
    Read_Text_A()
    Schema_A()

#Météo site
if Main_Menu == "Météo site":
    message_IS1 = "Cartographie du site" 
    message_inter = "Si vous souhaitez télécharger les données d'un jour antérieur veuillez modifier les valeurs suivantes en gardant le motif AAAAMMJJ HH"
    st.html(f"<div><h2 style='text-align: center; background-color: #0099ff;'>{message_IS1}</h2></div>")
    MDate = SDateData()
    Display_Image_IS()
    message_IS2 = "Données météorologique du site"
    st.html(f"<div><h2 style='text-align: center; background-color: #0099ff;'>{message_IS2}</h2></div>")
    Display_Data_IS(date_start = MDate[-1][:-3], date_end = MDate[-1][:-3], h = MDate[-1][-2:])
    #On enregistre pour l'instant pas ces données dans la database

#Configuration
if Main_Menu == "Configuration":

    col1, col2, col3 = st.columns(3)
    CDate = SDateData()
    CDate = CDate[1][:-3]

    with col1 :
        #st.header("G Conventionnelle")
        st.image(Read_Image_C("Conv.jpg"), use_container_width = True)
        st.write("Merci d'entrer les parametres de la centrale thermique")
        Puissance_GC = G_Conventionnel()
        if Puissance_GC[3] != 0:
            GConv_val = st.button("Upload Data", key = 12501, use_container_width = True, icon = ":material/cloud_download:")
            if GConv_val :
                G_ConventionnelTable(CDate, Puissance_GC[0], Puissance_GC[1], Puissance_GC[2], Puissance_GC[3])
        
    with col2 :
        #st.header("G Photovoltaique")
        st.image(Read_Image_C("Solaire.jpg"), use_container_width = True)
        st.write("Merci d'entrer les parametres de la centrale PV")
        Puissance_GPV = G_Photovoltaique()
        if Puissance_GPV[-1] != 0:
            GPV_val = st.button("Upload Data", key = 12502, use_container_width = True, icon = ":material/cloud_download:")
            if GPV_val :
                G_PhotovoltaiqueTable(CDate, Puissance_GPV[0], Puissance_GPV[1], Puissance_GPV[-1])
        
    with col3 :        
        #st.header("G Eolienne")
        st.image(Read_Image_C("Eolienne.jpg"), use_container_width = True)
        st.write("Merci d'entrer les parametres de la centrale éolienne")
        Puissance_GEolienne = G_Eolienne()
        if Puissance_GEolienne[-1] != 0:
            GEol_val = st.button("Upload Data", key = 12503, use_container_width = True, icon = ":material/cloud_download:")
            if GEol_val :
                G_EolienneTable(CDate, Puissance_GEolienne[0], Puissance_GEolienne[1], Puissance_GEolienne[2], Puissance_GEolienne[3])

#Prévision
if Main_Menu == "Prévision":
    message_PJ1 = "Prédiction des paramètres météorologiques journaliers"
    message_PJ2 = "Prédiction des paramètres météorologiques horaires"
    Read_Image_PJ()
    PJ_col1, PJ_col2 = st.columns(2)
    PJ_col3, PJ_col4 = st.columns(2)
    PJ_col5, PJ_col6 = st.columns(2)
    m = st.markdown("""<style> div.stButton > button:first-child {background-color: #0099ff;} </style>""", unsafe_allow_html=True)

    with PJ_col1:
        PJ_tog1 = st.toggle("Prevision Météorologique Journalière")
    with PJ_col2:
        PJ_tog2 = st.toggle("Prevision Météorologique Horaire")
    PDate = SDateData()

    if PJ_tog1:
        with PJ_col3:
            PJ_B1 = st.toggle("Recuperez Automatiquement les Données journalières") #use_container_width = True
        with PJ_col4:
            PJ_B2 = st.toggle("Entrez Manuellement les Données journalières")
        st.html(f"<div><h2 style='text-align: center; background-color: #0099ff;'>{message_PJ1}</h2></div>")
        data_PJ = 0
        if PJ_B1:
            Render_Data_J = Render_Data_IS("daily", date_start = PDate[-1][:-3], date_end = PDate[-1][:-3])
            if type(Render_Data_J) != str:
                data_PJ = Parameters_PJ(Render_Data_J) #Parametre météorologique input 
            else :
                st.html(f"{Render_Data_J}")
        elif PJ_B2:
            data_PJ = Parameters_PJ() #Parametre météorologique input
        if type(data_PJ) != int:
            if data_PJ[-1] == data_PJ[-2] == data_PJ[-3] == 0: #la prise en compte de l'hiver
                data_PJ = data_PJ + [1]
            else : data_PJ = data_PJ + [0]
            PMJ_val = st.button("Upload Data", key = 12504, use_container_width = True, icon = ":material/cloud_download:")
            if PMJ_val :
                #MeteoParamJTable(PDate[-1][:-3], data_PJ) #format %Y%m%d date J
                resultat_PJ = ModelePJ(data_PJ)
                PredJTable(PDate[-2][:-3], resultat_PJ) #Prev_timeJ "%Y%m%d date J + 1
                VPrevision_PJ(resultat_PJ) #Parametre météorologique outputresultat_PJ

    if PJ_tog2:
        with PJ_col5:
            PJ_B3 = st.toggle("Recuperez Automatiquement les Données horaires")
        with PJ_col6:
            PJ_B4 = st.toggle("Entrez Manuellement les Données horaires")
        st.html(f"<div><h2 style='text-align: center; background-color: #0099ff';>{message_PJ2}</h2></div>")
        data_PH = 1
        if PJ_B3:
            Render_Data_H = Render_Data_IS("hourly", date_start = PDate[-1][:-3], date_end = PDate[-1][:-3], h = PDate[1][-2:])
            if type(Render_Data_H) != str:
                data_PH = Parameters_PH(Render_Data_H) #Parametre météorologique input
            else :
                st.html(f"{Render_Data_H}") 
        elif PJ_B4:
            data_PH = Parameters_PH() #Parametre météorologique input 
        if type(data_PH) != int:
            PMH_val = st.button("Upload Data", key = 12505, use_container_width = True, icon = ":material/cloud_download:")
            if PMH_val :
                #MeteoParamHTable(PDate[-1].replace(" ", ""), data_PH) 
                resultat_PH = ModelePH(data_PH)
                Prev_Heure = PDate[-1][-2:]
                Prev_Date = PDate[-1][:-3]
                if Prev_Heure == "23":
                    Prev_Heure = -1
                    Prev_Date = PDate[-2][:-3]
                PredHTable(Prev_Date, (int(Prev_Heure) + 1), resultat_PH)
                VPrevision_PH(resultat_PH)

#Visualisation
if Main_Menu == "Visualisation":
    message_prev = "Prévisons du (AAAAMMJJ HH)"
    Viz_time = SDateData()

    col1, col2 = st.columns([1, 2])
    col1 = col1.container(height=700, border = False)
    col2 = col2.container(height=700, border = False)

    col3, col4 = st.columns([1, 2])
    col3 = col3.container(height=850, border = False)
    col4 = col4.container(height=850, border = False)

    with col1:
        st.html("<div><h2 style='text-align: center; background-color: #0099ff;'>Etat Journalier de l'atmosphere<div><h2>")
    with col2:
        st.html("<div><h2 style='text-align: center; background-color: #0099ff;'>Etat Journalier de la production énergétique<div><h2>")

    with col3:
        st.html("<div><h2 style='text-align: center; background-color: #0099ff;'>Etat Horaire de l'atmosphere<div><h2>")
    with col4:
        st.html("<div><h2 style='text-align: center; background-color: #0099ff;'>Etat Horaire de la production énergétique<div><h2>")
    
    with col1:
        ParamMJV_data = PredJData(Viz_time[-1][:-3])
        Viz_ParamMJV(ParamMJV_data)

    with col2:
        Data_Conv = G_ConventionnelData(Viz_time[-1][:-3])
        EConv = JEnergie_Conv(Data_Conv)

        Data_PV = G_PhotovoltaiqueData(Viz_time[-1][:-3])
        #Data_Meteo_PV = PredJData(Viz_time[-2][:-3])
        EPV = JEnergie_PV(Data_PV[2], Data_PV[-2], ParamMJV_data[-4], ParamMJV_data[-3])

        Data_Eolienne = G_EolienneData(Viz_time[-1][:-3])
        #Data_Meteo_Eolienne = PredJData(Viz_time[-2][:-3])
        Eolienne = JEnergie_Eolienne(ParamMJV_data[3], Data_Eolienne[-4], Data_Eolienne[-3], Data_Eolienne[-2], Data_Eolienne[-1])
        Viz_EnergyJV([EConv[-1], EPV, Eolienne])
    
    with col3:
        ParamMHV_data = PredHData(Viz_time[-1][:-3])    
        Viz_ParamMHV(ParamMHV_data, Viz_time[-1][-2:])
    
    with col4:
        h = Viz_time[-1][-2:]
        HEConv = HEnergie_Conv(Data_Conv, h)
        Data_Meteo_PV =[[i[1], i[2], i[4], i[5], i[6], i[7]]  for i in ParamMHV_data]
        Data_Meteo_Eolienne = [i[3] for i in ParamMHV_data]
        HData_PV = HEnergiePV(Data_Meteo_PV, Data_PV[-3], Data_PV[-2], Data_PV[-1], h)
        HData_Eolienne = HEnergie_Eolienne(Data_Meteo_Eolienne, Data_Eolienne[-4], Data_Eolienne[-3], Data_Eolienne[-2], Data_Eolienne[-1], h)
        
        Viz_EnergyHV(HEConv, HData_PV, HData_Eolienne, h)
        
#Apropos
if Main_Menu == "Apropos":
    col1, col2 = st.columns([1, 2])

    col1 = col1.container(height=800)
    col2 = col2.container(height=800)
    
    with col1:
        st.html("<div><h2 style='text-align: center; background-color: #0099ff;'>Identité</div></h2>")
    with col2:
        st.html("<div><h2 style='text-align: center; background-color: #0099ff;'>Questions - Responses - Courantes</div></h2>")

    with col1:
        with open("App_Identification.txt", 'r', encoding='utf-8') as file:
            file = file.readlines()
            for ligne in file:
                st.html(f"""<p style="font-size: 20px;">{ligne}</p>""")
        logo_path = "AppLogo.jpg"
        image = Image.open(logo_path)
        st.image(image, use_container_width = True)

    with col2:    
        st.html("""
        <div><details style="font-size: 20px;">
            <summary >Actualisation des onglets et données</summary>
            <p style="font-size: 20px;">Toutes les fois ou l'utilisateur clique sur un élément de l'application, le code source est entierement exécuté.</p>
        </details></div>""")

        st.html("""
        <div><details style="font-size: 20px;">
            <summary>L'étandu actuel de l'application</summary>
            <p style="font-size: 20px;">Les modèles de deep learning employés dans cette application ne couvrent pour l'instant que les données de la ville de N'Djamena.</p>
        </details></div>""")

        st.html("""
        <div><details style="font-size: 20px;">
            <summary>La récupération automatique des données</summary>
            <p style="font-size: 20px;">Le site POWER Hourly API de la NASA peut par moment ne pas fonctionner. Entrez les données manuellement est l'approche attendue dans cette sitution.</p>
        </details></div>""")

        st.html("""        
        <div><details style="font-size: 20px;">
            <summary>La qualité des données</summary>
            <p style="font-size: 20px;">Garbage in grabage out : la qualité des données entrées conditionnent les performances des modèles</p>
        </details></div>
        """)

        st.html("""        
        <div><details style="font-size: 20px;">
            <summary>L'onglet Visualisation ne renvoie aucun graphique</summary>
            <p style="font-size: 20px;">Si l'onglet visualisation n'affiche aucun graphique, assurez vous que la date de référence de prévision ait des des données relatives disponible récuperées soit sur le site de la NASA ou entrées manuellement et stockées dans la base de données </p>
        </details></div>
        """)

        st.html("""        
        <div><details style="font-size: 20px;">
            <summary>Visualisation par defaut</summary>
            <p style="font-size: 20px;">Vous visualiserez par defaut les prévisions journalières et horaires du '20240302' de 0h à 18h. 
                Deux génrateurs conventionels de couples puissances et rendements respectives  de (12000 kW, 0.8) et (15000 kW et 0.9). 
                Un Champ solaire d'une capacité de 4000 kWc avec un rendement de 0.8 et une inclinaison des modules à 15° plein Sud. 
                Deux éolienne d'une hauteur de 100 m, 80 m de diametre, un rendement de 0.8, un Cp de 0.45 et des vitesses min et max de 3.5 m/s et 20 m/s</p>
        </details></div>
        """)
        st.html("""<p style="font-size: 20px;">Votre TUTORIEL pour une utilisation réussie sera disponible très bientôt...</p>""")