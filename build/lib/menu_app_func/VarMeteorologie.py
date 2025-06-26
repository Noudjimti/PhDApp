import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from joblib import load

def ModelePJ(data = []):

    chemin = ["WS2M_MIN", "WS2M", "WS2M_MAX", "Index", "TEMP", "GHI", "DNI", "DIFF"]
    resultat = []
    scaler = load("Day_Models\\scaler.pkl")
    data = np.reshape(data, (1, -1))
    data = scaler.transform(data)
    data = data.reshape((1, 1, 25))
    for i in chemin:
        Model = load_model(f"Day_Models\\DNN_{i}.keras")
        resultat_int = Model.predict(data)
        resultat.append(resultat_int.tolist()[0][0])
    
    return resultat


def ModelePH(data = []):
    data = {"T2M" : data[0], "T2MWET" : data[2], "RH2M" : data[4], "PS" : data[6], 
            "WS2M" : data[7], "GHI" : data[9], "DNI" : data[10], "DIFF" : data[11]}
    #name = ["T2M", "T2MWET", "RH2M", "PS", "WS2M", "GHI", "DNI", "DIFF"]
    chemin = ["WS2M", "T2M", "GHI", "DNI", "DIFF"]
    resultat = []

    for i in chemin:

        if i in ["GHI", "DNI", "DIFF"]:
            df = [data[key] for key in ['GHI', 'DNI', 'DIFF', 'T2M', 'T2MWET', 'RH2M', 'WS2M']]
            df = np.reshape(df, (1, -1))
            scaler = load("Hour_Models\\scaler_GHI.pkl")
            df = scaler.transform(df)
        elif i == "T2M":
            df = [data[key] for key in ['GHI', 'DNI', 'DIFF', 'T2M', 'T2MWET', 'RH2M', 'PS']]
            df = np.reshape(df, (1, -1))
            scaler = load("Hour_Models\\scaler_T2M.pkl")
            df = scaler.transform(df)
        elif i == "WS2M":
            df = [data[key] for key in ['GHI', 'DNI', 'DIFF', 'T2MWET', 'RH2M', 'PS', 'WS2M']]
            df = np.reshape(df, (1, -1))
            scaler = load("Hour_Models\\scaler_WS2M.pkl")
            df = scaler.transform(df)

        df = df.reshape((1, 1, 7))
        Model = load_model(f"Hour_Models\\DNN_{i}.keras")
        resultat_int = Model.predict(df)
        resultat.append(resultat_int.tolist()[0][0])
    
    return resultat

