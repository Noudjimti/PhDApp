import pandas as pd
import numpy as np
from math import pow, pi, sin, cos #trunc

def HEnergiePV(Param, puissance_rend = (50000*0.8), coef = (0.225/1000), betha = 15,  heure = 0):
    heure = int(heure) + 2
    PUISSANCE = []
    for param in Param : 
        n_jour, hour = DateP(param[0], param[1])
        TEMP = param[2]
        GHI = param[3]
        DNI = param[4]
        DHI = param[5]
        
        #parametres du champ solaire et site rsys = 0.8 coef = 0.225/1000000 #en Mégawatt betha = 15 puissance = 50 #MWc
        albedo = 0.3
        angle_coef = pi/180
        betha = betha*angle_coef
        
        I0 = albedo*GHI*(1 - cos(betha))/2
        I1 = DHI*(1 + cos(betha))/2

        #elements de calcul de I2
        Lst = 15
        Lloc = 15.05
        Lat = 12.15*angle_coef
    
        #az = 0*angle_coef

        T = (360/365)*(n_jour - 1)*angle_coef

        E = 229.2*(0.000075 + 0.001868*cos(T) - 0.032077*sin(T)
                - 0.014615*cos(2*T) - 0.04089*sin(2*T))
        ohm = 4*(Lst - Lloc)/60 + hour + E/60     
        omega = 15*(12 - ohm)*angle_coef

        dec = (0.006918 - 0.399912*cos(T) + 0.070257*sin(T)
                    - 0.006758*cos(2*T) + 0.000907*sin(2*T)
                    - 0.002697*cos(3*T) + 0.00148*sin(3*T))

        costheta = (cos(Lat - betha)*cos(dec)*cos(omega) +
                    sin(Lat - betha)*sin(dec))
        
        if 0 > costheta :
            costheta = 0

        I2 = DNI*costheta
        
        #calcul de I final
        I = (I0 + I1 + I2)/1000

        if TEMP > 25 :
            Pr = (1 - coef*(TEMP - 25))*puissance_rend
        else : Pr = puissance_rend

        PUISSANCE.append(Pr*I)

    return PUISSANCE[:heure]

def DateP(Date, hour):
        year = Date[:4]
        month = Date[4:6]
        day = Date[6:8]
        n_day = (pd.to_datetime(f"{str(year)}-{str(month)}-{str(day)}") - pd.to_datetime(str(year) + "-01-01")).days
        return n_day, int(hour)

def Uniformisation(x):
        if x < 0:
            return 0
        else : return x


def JEnergie_Conv(param):
    E = [i[2]*i[3] for i in param]
    Duree = [i[4] for i in param]
    E_total = sum(E)
    return E, Duree, E_total #Deja en kilo

def HEnergie_Conv(param, heure):
    heure = int(heure) + 2
    X = []
    Y = []
    X1 = []
    Y1 = []
    for ligne in param:
        puissance = [ligne[2]]*ligne[3]
        debut = int(ligne[4][:2])
        pas_temp = np.arange(debut, stop = debut + ligne[3], step = 1).tolist()
        X +=pas_temp
        Y +=puissance
    p = []
    for i in range(24):
        for val in X:
            if val == i:
                p += [Y[i]]
        p = sum(p)
        X1.append(i)
        Y1.append(p)
        p = []

    return Y1[:heure]                
 
def JEnergie_PV(Puissance, coeff, TEMP, GHI):
    return (1 - coeff*(TEMP - 25))*Puissance*GHI #Deja en kilo

def JEnergie_Eolienne(Vprev, Puissance, Hauteur, Vmin, Vmax, h = 24):
    vitesse = Vprev
    puissance = Puissance
    hauteur = Hauteur
    vitesse_min = Vmin
    vitesse_max = Vmax
    puissance_ref = 0
    alpha = 0.2
    hauteur_ref = 2
    vitesse = vitesse * pow((hauteur/hauteur_ref), alpha)

    if (vitesse < vitesse_min) or (vitesse > vitesse_max):
        return puissance_ref
    else:
        Puissance_E = pow(vitesse, 3) * puissance*h

        return Puissance_E/1000
    
def HEnergie_Eolienne(Vprev, Puissance, Hauteur, Vmin, Vmax, heure):
    heure = int(heure) + 2
    vitesse = Vprev
    puissance = Puissance
    hauteur = Hauteur
    vitesse_min = Vmin
    vitesse_max = Vmax
    alpha = 0.2
    hauteur_ref = 2
    Puissance_E = []
    for v in vitesse :
        V = v * pow((hauteur/hauteur_ref), alpha)

        if (V < vitesse_min) or (V > vitesse_max):
            puissance_ref = 0
        else:
            puissance_ref = (pow(V, 3) * puissance)/1000

        Puissance_E.append(puissance_ref)

    return Puissance_E[:heure]
    



    



