import sqlite3

stockage = "Stockage.db"

class SideBarTable :
    ID = 0
    def __init__(self, Date, Pays, Ville, Lat, Lon):
        SideBarTable.ID +=1
        self.Date = Date
        self.Pays = Pays
        self.Ville = Ville
        self.Lat = Lat
        self.Lon = Lon
        self.command = """CREATE TABLE IF NOT EXISTS
        SideBarTable(ID INT, Date TEXT, Pays TEXT, Ville TEXT, Lat FLOAT, Lon FLOAT)"""

        with sqlite3.connect(stockage) as conn:
            cursor = conn.cursor()
            cursor.execute(self.command)
            cursor.execute("""INSERT OR REPLACE INTO SideBarTable VALUES (?, ?, ?, ?, ?, ?)""", 
                           (SideBarTable.ID, self.Date, self.Pays, self.Ville, self.Lat, self.Lon))
            conn.commit()
        conn.close()
    
class G_ConventionnelTable:
    ID = 0
    def __init__(self, Date, Puissance, Temps, Duree, Nombre):
        G_ConventionnelTable.ID +=1
        self.Puissance = Puissance
        self.Temps = Temps
        self.Duree = Duree
        self.Nombre = Nombre
        self.Date = Date #datetime.now().strftime('%Y%m%d%H') #A surveiller plustard
        self.command = """CREATE TABLE IF NOT EXISTS 
        G_ConventionnelTable(ID INT, Date TEXT, Puissance FLOAT, Temps INT, Duree TEXT, Nombre INT)"""

        with sqlite3.connect(stockage) as conn:
            cursor = conn.cursor()
            cursor.execute(self.command)
            for i in range(self.Nombre):
                cursor.execute("""INSERT OR REPLACE INTO G_ConventionnelTable (ID, Date, Puissance, Temps, Duree, Nombre) VALUES (?, ?, ?, ?, ?, ?)""", 
                            (G_ConventionnelTable.ID, self.Date, self.Puissance[i], self.Temps[i], self.Duree[i], i+1)) #self.Nombre
            conn.commit()
        conn.close() 

class G_PhotovoltaiqueTable:
    ID = 0
    def __init__(self, Date, Puissance, Coef, Betha):
        G_PhotovoltaiqueTable.ID +=1
        self.Puissance = Puissance
        self.Coef = Coef
        self.Betha = Betha
        self.Date = Date #datetime.now().strftime('%Y%m%d%H')
        self.command = """CREATE TABLE IF NOT EXISTS G_PhotovoltaiqueTable (ID INT, Date TEXT, Puissance FLOAT, Coef FLOAT, Betha FLOAT)"""

        with sqlite3.connect(stockage) as conn:
            cursor = conn.cursor()
            cursor.execute(self.command)
            cursor.execute("""INSERT OR REPLACE INTO G_PhotovoltaiqueTable (ID, Date, Puissance, Coef, Betha) VALUES (?, ?, ?, ?, ?)""", 
                           (G_PhotovoltaiqueTable.ID, self.Date, self.Puissance, self.Coef, self.Betha))
            conn.commit()
        conn.close()
        
class G_EolienneTable:
    ID = 0
    def __init__(self, Date, Puissance, Hauteur, Vent_min, Vent_max):
        G_EolienneTable.ID +=1
        self.Puissance = Puissance
        self.Hauteur = Hauteur
        self.Vent_min = Vent_min
        self.Vent_max = Vent_max
        self.Date = Date#datetime.now().strftime('%Y%m%d%H')
        command = """CREATE TABLE IF NOT EXISTS G_EolienneTable(ID INT, Date TEXT, Puissance FLOAT, Hauteur FLOAT, Vent_min FLOAT, Vent_max FLOAT)"""

        with sqlite3.connect(stockage) as conn:
            cursor = conn.cursor()
            cursor.execute(command)
            cursor.execute("""INSERT OR REPLACE INTO G_EolienneTable VALUES (?, ?, ?, ?, ?, ?)""", 
                           (G_EolienneTable.ID, self.Date, self.Puissance, self.Hauteur, self.Vent_min, self.Vent_max)) 
            conn.commit()
        conn.close()

class MeteoParamJTable:
    ID = 0
    def __init__(self, Date, Meteoparams):
        MeteoParamJTable.ID +=1
        self.Meteoparams = Meteoparams
        self.Date = Date #datetime.now().strftime('%Y%m%d%H')
        command = """CREATE TABLE IF NOT EXISTS
        MeteoParamJTable(ID INT, Date TEXT, Temp FLOAT, Temp_r FLOAT, Temp_h FLOAT, Humi_s FLOAT, Humi_r FLOAT, Precip FLOAT, Pression FLOAT, 
        V_moy FLOAT, Temp_max FLOAT, Temp_min FLOAT, V_max FLOAT, V_min FLOAT, I_cc FLOAT, Ghi FLOAT, Dni FLOAT, Diff FLOAT, Couv_n FLOAT, 
        V_n FLOAT, V_o FLOAT, V_s FLOAT, V_e FLOAT, Autaumn FLOAT, Printemps FLOAT, Ete FLOAT, Hiver FLOAT)"""

        with sqlite3.connect(stockage) as conn:
            cursor = conn.cursor()
            cursor.execute(command)
            cursor.execute("""INSERT OR REPLACE INTO MeteoParamJTable VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", 
                        tuple([MeteoParamJTable.ID, self.Date] + self.Meteoparams))
            conn.commit()
        conn.close() 
    
class MeteoParamHTable:
    ID = 0
    def __init__(self, Date, Meteoparams):
        MeteoParamHTable.ID +=1
        self.Meteoparams = Meteoparams
        self.Date = Date, #datetime.now().strftime('%Y%m%d%H')
        command = """CREATE TABLE IF NOT EXISTS
        MeteoParamHTable(ID INT, Date TEXT, Temp FLOAT, Temp_r FLOAT, Temp_h FLOAT, Humi_s FLOAT, Humi_r FLOAT, Precip FLOAT, Pression FLOAT, 
        V_moy FLOAT, I_cc FLOAT, Ghi FLOAT, Dni FLOAT, Diff FLOAT, Couv_n FLOAT, V_n FLOAT, V_o FLOAT, V_s FLOAT, V_e FLOAT, Autaumn FLOAT, Printemps FLOAT, Ete FLOAT)"""

        with sqlite3.connect(stockage) as conn:
            cursor = conn.cursor()
            cursor.execute(command)
            cursor.execute("""INSERT OR REPLACE INTO MeteoParamHTable VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", 
                        tuple([MeteoParamHTable.ID, self.Date] + self.Meteoparams)) 
            conn.commit()
        conn.close()

class PredJTable:
    ID = 0
    def __init__(self, Date, Pred):
        PredJTable.ID +=1
        self.Pred = Pred
        self.Date = Date #datetime.now().strftime('%Y%m%d%H')
        command = """CREATE TABLE IF NOT EXISTS
        PredJTable(ID INT, Date TEXT, V_min FLOAT, V_moy FLOAT, V_max FLOAT, C_n FLOAT, Temp FLOAT, GHI FLOAT, DNI FLOAT, DHI FLOAT)"""

        with sqlite3.connect(stockage) as conn:
            cursor = conn.cursor()
            cursor.execute(command)
            cursor.execute("""INSERT OR REPLACE INTO PredJTable VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", 
                        tuple([PredJTable.ID, self.Date] + self.Pred)) 
            conn.commit()
        conn.close()

class PredHTable:
    ID = 0
    def __init__(self, Date, Heure, Pred):
        PredHTable.ID +=1
        self.Pred = Pred
        self.Date = Date #datetime.now().strftime('%Y%m%d')
        self.Heure = Heure
        command = """CREATE TABLE IF NOT EXISTS
        PredHTable(ID INT, Date TEXT, Heure INT, V_moy FLOAT, Temp FLOAT, GHI FLOAT, DNI FLOAT, DHI FLOAT)"""

        with sqlite3.connect(stockage) as conn:
            cursor = conn.cursor()
            cursor.execute(command)
            cursor.execute("""INSERT OR REPLACE INTO PredHTable VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", 
                        tuple([PredHTable.ID, self.Date, self.Heure] + self.Pred)) 
            conn.commit()
        conn.close()

class SDateTable:
    ID = 0
    def __init__(self, Date, PassDate):
        SDateTable.ID +=1
        self.Date = Date
        self.PassDate = PassDate
        command = """CREATE TABLE IF NOT EXISTS SDateTable(ID INT, Date TEXT, PassDate TEXT)"""

        with sqlite3.connect(stockage) as conn:
            cursor = conn.cursor()
            cursor.execute(command)
            cursor.execute("""INSERT OR REPLACE INTO SDateTable VALUES (?, ?, ?)""",
                           tuple([SDateTable.ID, self.Date, self.PassDate])) 
            conn.commit()
        conn.close()

class EnergieJTable: 
    ID = 0
    def __init__(self, Date, Conv, PV, Eolienne):
        EnergieJTable.ID +=1
        self.Date = Date #%Y%m%d%
        self.Conv = Conv
        self.PV = PV
        self.Eolienne = Eolienne
        command = """CREATE TABLE IF NOT EXISTS
        EnergieJTable(ID INT, Date TEXT, Conv FLOAT, PV FLOAT, Eolienne FLOAT)"""

        with sqlite3.connect(stockage) as conn:
            cursor = conn.cursor()
            cursor.execute(command)
            cursor.execute("""INSERT OR REPLACE INTO EnergieJTable VALUES (?, ?, ?, ?, ?)""", 
                        tuple([EnergieJTable.ID, self.Date, self.Conv,  self.PV,  self.Eolienne])) 
            conn.commit()
        conn.close()
