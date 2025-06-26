import sqlite3

stockage = "Stockage.db"

def SideBarData(Date):
    command = f"""SELECT * FROM SideBarTable WHERE Date = {Date}""" # ORDER BY ID DESC
    with sqlite3.connect(stockage) as conn:
        cursor = conn.cursor()
        data = cursor.execute(command).fetchall() # ID INT, Date TEXT, Pays TEXT, Ville TEXT, Lat FLOAT, Lon FLOAT
        return list(data[-1])
    
def G_ConventionnelData(Date):
    command1 = f"""SELECT ROW_NUMBER() OVER(ORDER BY ID DESC) R, ID, Nombre FROM G_ConventionnelTable WHERE Date = {Date}""" #ORDER BY Nombre ASC
    command2 = f"""SELECT * FROM G_ConventionnelTable WHERE Date = {Date}""" #ORDER BY Nombre ASC
    with sqlite3.connect(stockage) as conn:
        cursor = conn.cursor()
        n = cursor.execute(command1).fetchall()
        n = n[-1][-1]
        data = cursor.execute(command2).fetchall() # Date TEXT, ID INT, Puissance FLOAT, Temps INT, Duree TEXT, Nombre INT
        return data[-n:]
    
def G_PhotovoltaiqueData(Date):
    command = f"""SELECT * FROM G_PhotovoltaiqueTable WHERE Date = {Date}""" # ORDER BY ID DESC
    with sqlite3.connect(stockage) as conn:
        cursor = conn.cursor()
        data = cursor.execute(command).fetchall() # 
        return list(data[-1])
    
def G_EolienneData(Date):
    command = f"""SELECT * FROM G_EolienneTable WHERE Date = {Date}""" # ORDER BY ID DESC
    with sqlite3.connect(stockage) as conn:
        cursor = conn.cursor()
        data = cursor.execute(command).fetchall() # 
        return list(data[-1])
    
def MeteoParamJData(Date):
    command = f"""SELECT * FROM MeteoParamJ WHERE Date = {Date}""" # ORDER BY ID DESC
    with sqlite3.connect(stockage) as conn:
        cursor = conn.cursor()
        data = cursor.execute(command).fetchall() # 
        return list(data[-1])
    
def MeteoParamHData(Date):
    command = f"""SELECT * FROM MeteoParamJTable WHERE Date = {Date}""" # ORDER BY ID DESC
    with sqlite3.connect(stockage) as conn:
        cursor = conn.cursor()
        data = cursor.execute(command).fetchall() # 
        return list(data[-1])
    
def PredJData(Date):
    command = f"""SELECT * FROM PredJTable WHERE Date = {Date}""" # ORDER BY ID DESC
    with sqlite3.connect(stockage) as conn:
        cursor = conn.cursor()
        data = cursor.execute(command).fetchall() # 
        return list(data[-1])
    
def PredHData(Date):
    command = f"""SELECT * FROM PredHTable WHERE Date = {Date} ORDER BY Heure ASC"""
    with sqlite3.connect(stockage) as conn:
        cursor = conn.cursor()
        data = cursor.execute(command).fetchall() # 
        return data
    
def SDateData():
    command = f"""SELECT * FROM SDateTable""" #ORDER BY ID DESC"""
    with sqlite3.connect(stockage) as conn:
        cursor = conn.cursor()
        data = cursor.execute(command).fetchall() # 
        return list(data[-1])

def EnergieJData(Date):
    command = f"""SELECT * FROM EnergieJTable WHERE Date = {Date}""" # ORDER BY ID DESC
    with sqlite3.connect(stockage) as conn:
        cursor = conn.cursor()
        data = cursor.execute(command).fetchall() # 
        return list(data[-1])