import streamlit as st
import folium
from streamlit_folium import folium_static
import requests
import json
import pandas as pd
import numpy as np


def Display_Image_IS():
    col1, col2 = st.columns(2)
        
    with col1.container(height=550, border = False):
        st.html("Pays")
        map1 = folium.Map(location=[15.67, 18.63], zoom_start=3)
        folium.Marker([12.17, 15.00], popup="Ndjaména, Tchad").add_to(map1)
        folium_static(map1)

    with col2.container(height=550, border = False) :
        st.html("Ville")
        map2 = folium.Map(location=[12.17, 15.00], zoom_start=12)
        folium_static(map2)

def Display_Data_IS(date_start = "20250101", date_end = "20250101", h = 11):
    col1, col2 = st.columns(2, border=True)
        
    with col1 :
        st.html("Données journalières")
    with col2 :
        st.html("Données Horaires")

    with col1 :
        df1 = Read_Data_IS(step = "daily", data_type = "ag", date_start = date_start, date_end = date_end)
        df2 = Read_Data_IS(step = "daily", data_type = "re", date_start = date_start, date_end = date_end)
        mess = "Erreur de récupération des données, site en panne"
        if type(df1) == str or type(df2) == str:
            st.html(mess)
        else :
            direction_c1 = MakeDirection(df1.iloc[0, -1])
            Saison_c1 = MakeSeason(date_start)
            valeurs_c1 = list(df1.iloc[0, :-1]) + list(df2.iloc[0, :]) + list(direction_c1.values()) + [Saison_c1]
            Noms_c1 = ["Temperature", "Temperature relative", "Temperature humide", "Humidité spécifique", "Humidité relative", "Précipitation", 
                    "Pression", "Vent moyenne", "Temperature maximale",  "Temperature minimale", "Vent maximale", "Vent minimale", "Irradiance ciel clair", 
                    "GHI", "GNI", "DHI", "Couverture nuageuse", "Vent Nord", "Vent Ouest", "Vent  Sud", "Vent Est", "Saison"]
            for i,j in enumerate(valeurs_c1):
                st.html(f"{Noms_c1[i]} : {j}")

            if Saison_c1 == "Winter":
                valeurs_c1 = valeurs_c1[:-1] + [0, 0, 0]
            elif Saison_c1 == "Spring":
                valeurs_c1 = valeurs_c1[:-1] + [1, 0, 0]
            elif Saison_c1 == "Summer":
                valeurs_c1 = valeurs_c1[:-1] + [0, 1, 0]
            elif Saison_c1 == "Autumn":
                valeurs_c1 = valeurs_c1[:-1] + [0, 0, 1]
        
    with col2 :
        h = int(h)
        df3 = Read_Data_IS(step = "hourly", data_type = "ag", date_start = date_start, date_end = date_end)
        df4 = Read_Data_IS(step = "hourly", data_type = "re", date_start = date_start, date_end = date_end)
        if type(df3) == str or type(df4) == str:
            st.html(mess)
        else : 
            direction_c2 = MakeDirection(df3.iloc[h, -1])
            Saison_c2 = MakeSeason(date_start)
            valeurs_c2 = list(df3.iloc[h, :-1]) + list(df4.iloc[h, :]) + list(direction_c2.values()) + [Saison_c2]
            Noms_c2 = ["Temperature", "Temperature relative", "Temperature humide", "Humidité spécifique", "Humidité relative", 
                    "Précipitation", "Pression", "Vent moyenne", "Irradiance ciel clair", "GHI", "GNI", "DHI", "Couverture nuageuse", 
                    "Vent Nord", "Vent Ouest", "Vent  Sud", "Vent Est", "Saison"]
            for i,j in enumerate(valeurs_c2):
                st.html(f"{Noms_c2[i]} : {j}")

            if Saison_c2 == "Winter":
                valeurs_c2 = valeurs_c2[:-1] + [0, 0, 0]
            elif Saison_c2 == "Spring":
                valeurs_c2 = valeurs_c2[:-1] + [1, 0, 0]
            elif Saison_c2 == "Summer":
                valeurs_c2 = valeurs_c2[:-1] + [0, 1, 0]
            elif Saison_c2 == "Autumn":
                valeurs_c2 = valeurs_c2[:-1] + [0, 0, 1]
    
    #return valeurs_c1, valeurs_c2
     
def Read_Data_IS(step = "daily", data_type = "ag", date_start = "20250101", date_end = "20250101"):
    lat = 12.15
    lon = 15.05
    parameters_ag = ["T2M", "T2MDEW", "T2MWET", "QV2M", "RH2M", "PRECTOTCORR", "PS", "WS2M", "T2M_MAX", "T2M_MIN", "WS2M_MAX", "WS2M_MIN", "WD2M"]
    parameters_re = ["CLRSKY_SFC_SW_DWN", "ALLSKY_SFC_SW_DWN", "ALLSKY_SFC_SW_DNI", "ALLSKY_SFC_SW_DIFF", "ALLSKY_KT"]
    if step == "hourly":
        parameters_ag = ["T2M", "T2MDEW", "T2MWET", "QV2M", "RH2M", "PRECTOTCORR", "PS", "WS2M", "WD2M"]
    lien_root = f"https://power.larc.nasa.gov/api/temporal/{step}/point?start={date_start}&end={date_end}&latitude={lat}&longitude={lon}&community={data_type}&parameters="
    lien = ""
    if data_type == "ag":
        parameters = parameters_ag
        for i, param in enumerate(parameters):
            if i == 0:
                lien += f"{param}%"
            else:
                lien += f"2C{param}%"
    elif data_type == "re":
        parameters = parameters_re
        for i, param in enumerate(parameters):
            if i == 0:
                lien += f"{param}%"
            else:
                lien +=f"2C{param}%"
    lien = lien_root + lien[:-1] + "&format=json&user=MyApp&header=true&time-standard=utc"

    try:
        response = requests.get(lien)
        response.raise_for_status()  

        data = response.json()

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération du fichier JSON : {e}")
        data = 0

    except json.JSONDecodeError as e:
        print(f"Erreur lors du décodage du JSON : {e}")
        data = 1
    finally:            
        if type(data) != int:
            valeurs = []
            for i in parameters :
                valeurs.append(list(data['properties']['parameter'][i].values()))
            
            return pd.DataFrame(np.array(valeurs).T)
        else : return "Erreur de récupération des données, site en panne"

def MakeDirection(x):
    North = 0
    West = 0
    South = 0
    Est = 0
    if 0 < x <= 90:
        Est = 1
        North = 1
    
        West = 0
        South = 0
            
    elif 90 < x <= 180:
        North = 1
        West = 1
    
        South = 0
        Est = 0
        
    elif 180 < x <= 270:
        West = 1
        South = 1
            
        Est = 0
        North = 0
        
    else :
        South = 1
        Est = 1
    
        North = 0
        West = 0
            
    return {"North Wind": North, "West Wind": West, "South Wind": South, "Est Wind": Est}

def MakeSeason(x):
    x = x.strip()
    x = x[:4] + "-" + x[4:6] + "-" + x[6:]  
    x = pd.to_datetime(x, format="%Y-%m-%d")
    if pd.to_datetime(str(x.year) + "-01-01", format = "%Y-%m-%d") <= x < pd.to_datetime(str(x.year) + "-03-21", format = "%Y-%m-%d") :
        return "Winter"
    elif pd.to_datetime(str(x.year) + "-03-21", format = "%Y-%m-%d") <= x < pd.to_datetime(str(x.year) + "-06-21", format = "%Y-%m-%d") :
        return "Spring"
    elif pd.to_datetime(str(x.year) + "-06-21", format = "%Y-%m-%d") <= x < pd.to_datetime(str(x.year) + "-09-21", format = "%Y-%m-%d") :
        return "Summer"
    elif pd.to_datetime(str(x.year) + "-09-21", format = "%Y-%m-%d") <= x < pd.to_datetime(str(x.year) + "-12-21", format = "%Y-%m-%d") :
        return "Autumn"
    elif pd.to_datetime(str(x.year) + "-12-21", format = "%Y-%m-%d") <= x <= pd.to_datetime(str(x.year) + "-12-31", format = "%Y-%m-%d") :
        return "Winter"
    

def Render_Data_IS(step = "daily", h = 0, date_start = "20250101", date_end = "20250101"):  

    if step == "daily":
        h = 0    
    h= int(h)
    df1 = Read_Data_IS(step = step, data_type = "ag", date_start = date_start, date_end = date_end)
    df2 = Read_Data_IS(step = step, data_type = "re", date_start = date_start, date_end = date_end)
    if type(df1) == str:
        return df1
    elif type(df2) == str :
        return df2
    else :
        if 0 <= df1.iloc[h, -1] < 361 :
            direction_c1 = MakeDirection(df1.iloc[h, -1])
            Saison_c1 = MakeSeason(date_start)
            valeurs_c1 = list(df1.iloc[h, :-1]) + list(df2.iloc[h, :]) + list(direction_c1.values()) + [Saison_c1]

            if Saison_c1 == "Winter":
                valeurs_c1 = valeurs_c1[:-1] + [0, 0, 0]
            elif Saison_c1 == "Spring":
                valeurs_c1 = valeurs_c1[:-1] + [0, 1, 0]
            elif Saison_c1 == "Summer":
                valeurs_c1 = valeurs_c1[:-1] + [0, 0, 1]
            elif Saison_c1 == "Autumn":
                valeurs_c1 = valeurs_c1[:-1] + [1, 0, 0]
                
            return valeurs_c1
        else : return "Erreur de récupération des données, données manquantes ou non conformes"

     