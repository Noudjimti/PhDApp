import streamlit as st
import matplotlib.pyplot as plt


def Viz_ParamMJV(params):
    fig, ax = plt.subplots(2, 2, figsize = (6, 8.5))

    ax[0, 0].barh(range(3), params[-3:][::-1], tick_label=["GHI", "DNI", "DHI"][::-1], color = "#C25C10")
    ax[0, 0].set_title("Irradiance")
    
    ax[0, 1].barh(range(3), params[-8:-5], tick_label=["Vmin", "Vmoy", "Vmax"])
    ax[0, 1].set_title("Vitesse vent")
    
    ax[1, 0].pie([1 - params[-5], params[-5]], labels=["Ciel nuageux", "Ciel clair"], autopct='%1.1f%%', colors = ["#1F03EB", "#B2F0F8"])
    ax[1, 0].set_title("Couverture nuageuse Conditions")
    
    ax[1, 1].bar([0], [params[-4]], color="orange", width=0.1)
    ax[1, 1].set_title("Temperature")
    ax[1, 1].set_xticks([])
    
    plt.tight_layout()
    st.pyplot(fig)

def Viz_ParamMHV(params, Heure):
    Heure = int(Heure) + 2
    V_moy = [i[3] for i in params]
    T2M = [i[4] for i in params]
    GHI = [i[5] for i in params]
    DNI = [i[6] for i in params]
    DHI = [i[7] for i in params]

    fig, ax = plt.subplots(5, 1, figsize = (6, 12))
    ax[0].plot(range(Heure), V_moy[:Heure])
    ax[0].set_xlim(0, Heure)
    ax[0].set_ylim(0, max(V_moy) + (max(V_moy)*0.05)) 
    ax[0].set_xlabel("Heure")
    ax[0].set_ylabel("Vitesse du vent")

    ax[1].plot(range(Heure), T2M[:Heure])
    ax[1].set_xlim(0, Heure)
    ax[1].set_ylim(0, max(T2M) + (max(T2M)*0.05)) 
    ax[1].set_xlabel("Heure")
    ax[1].set_ylabel("Temperature")

    ax[2].plot(range(Heure), GHI[:Heure])
    ax[2].set_xlim(0, Heure)
    ax[2].set_ylim(0, max(GHI) + (max(GHI)*0.05)) 
    ax[2].set_xlabel("Heure")
    ax[2].set_ylabel("GHI")

    ax[3].plot(range(Heure), DNI[:Heure])
    ax[3].set_xlim(0, Heure)
    ax[3].set_ylim(0, max(DNI) + (max(DNI)*0.05)) 
    ax[3].set_xlabel("Heure")
    ax[3].set_ylabel("DNI")

    ax[4].plot(range(Heure), DHI[:Heure])
    ax[4].set_xlim(0, Heure)
    ax[4].set_ylim(0, max(DHI) + (max(DHI)*0.05)) 
    ax[4].set_xlabel("Heure")
    ax[4].set_ylabel("DHI")
    plt.tight_layout()
    st.pyplot(fig)

def Viz_EnergyJV(params):
    fig, ax = plt.subplots(figsize = (5, 6))
    plt.pie(params, labels = ["Energie Conventionnelle", "Energie PV", "Energie Eolienne"], 
            autopct='%1.1f%%', shadow= True, explode= (0, 0.2, 0.2), radius=1.90)
    
    plt.text(2, 2, f"Energie Totale Journaliere : {sum(params)/1000 : .2f} MWh")
    #plt.title(f"Energie Totale Journaliere : {sum(params)/1000 : .2f} MWh")

    plt.tight_layout()
    st.pyplot(fig)

def Viz_EnergyHV(param1, param2, param3, heure): #param3
    heure = int(heure) + 2
    fig, ax = plt.subplots(4, 1, figsize = (5, 5)) #3

    Total = [(param1[i] + param2[i] + param3[i]) for i in range(heure)]
    ax[0].plot(range(heure), Total, color = "#39DDC2CC")
    ax[0].fill_between(range(heure), Total, color = "#39DDC2CC")
    ax[0].set_xlim(0, heure) 
    ax[0].set_xlabel("Heure")
    ax[0].set_ylabel("Sum (kWh)")

    ax[1].plot(range(heure), param1)
    ax[1].fill_between(range(heure), param1)
    ax[1].set_xlim(0, heure) 
    ax[1].set_xlabel("Heure")
    ax[1].set_ylabel("Conv (kWh)")

    ax[2].plot(range(heure), param2, color = "#C25C10")
    ax[2].fill_between(range(heure), param2, color = "#C25C10")
    ax[2].set_xlim(0, heure)
    ax[2].set_xlabel("Heure")
    ax[2].set_ylabel("PV (kWh)")

    ax[3].plot(range(heure), param3, color = "#10C21F")
    ax[3].fill_between(range(heure), param3, color = "#10C21F")
    ax[3].set_xlim(0, heure)
    ax[3].set_xlabel("Heure")
    ax[3].set_ylabel("Eol (kWh)")

    plt.tight_layout()
    st.pyplot(fig)




































"""
date = datetime.now().strftime('%Y%m%d%H')
    s1 = SideBarData(date)
    st.html(s1)
    s2 = G_ConventionnelData(date)
    st.html(s2)
    s3 = G_PhotovoltaiqueData(date)
    st.html(s3)
    s4 = G_EolienneData(date)
    st.html(s4)
    s5 = MeteoParamJData(date)
    st.html(s5)
    s6 = MeteoParamHData(date)
    st.html(s6)
(20, '2025060722', 'Cameroun', '', 0.0, 0.0)
[(11, '2025060722', 0.0, 0, '0000', 1)]
(8, '2025060722', 0.0001, 0.01)
(1, '2025060722', 0.0, 0.0, 0.0, 0.01)
(2, '2025060722', 23.75, 0.03, 11.89, 3.94, 24.59, 0.0, 97.85, 4.44, 35.41, 14.35, 5.99, 2.52, -999.0, -999.0, -999.0, -999.0, -999.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0)
(3, '2025060722', 0.0, 0.0, 0.0, 0.0, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01, 0.0, 0.0, 0.0, 0.01, 0.0, 0.0, 0.0, 0.0)
"""