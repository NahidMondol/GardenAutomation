import psycopg2

class GardenDatabase:
    DB_HOST = "192.168.0.41"
    DB_NAME = "gardendb"
    DB_USER = "pi"
    DB_PASSWORD = "6201"
    conn = None

    def __init__(self):
        self.DB_HOST = "192.168.0.41"
        self.DB_NAME = "gardendb"
        self.DB_USER = "pi"
        self.DB_PASSWORD = "6201"
        #self.conn = psycopg2.connect(dbname = self.DB_NAME, user = self.DB_USER, password = self.DB_PASSWORD, host = self.DB_HOST)


    def convertCelsiusToFahrenheit(tempInCelsius):
        return ((tempInCelsius * 9/5) + 32)


    def getAll(self):
        try:
            conn = psycopg2.connect(dbname = self.DB_NAME, user = self.DB_USER, password = self.DB_PASSWORD, host = self.DB_HOST)
            cur = conn.cursor()
            cur.execute("SELECT * FROM general;")
            list = cur.fetchall()
            conn.close()
            return list
        finally:
            if conn is not None:
                conn.close()


    def insertData(self, temperature, humidity):
        try:
            conn =  psycopg2.connect(dbname = self.DB_NAME, user = self.DB_USER, password = self.DB_PASSWORD, host = self.DB_HOST)
            cur = conn.cursor()
            cur.execute("INSERT INTO general (recorded_timestamp, temperature, soil_humidity) VALUES (current_timestamp, %s, %s);", (GardenDatabse.convertCelsiusToFahrenheit(temperature), humidity))
            conn.commit()
            conn.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


    def getTimeTempAndHumidity(self):
        try:
            conn =  psycopg2.connect(dbname = self.DB_NAME, user = self.DB_USER, password = self.DB_PASSWORD, host = self.DB_HOST)
            cur = conn.cursor()
            cur.execute("SELECT general_id, recorded_timestamp, temperature, soil_humidity FROM general;")
            list = cur.fetchall()
            for item in list:
                print("ID {}\nTime {}\nTemperature {}\nHumidity {}".format(item[0], item[1], GardenDatabase.convertCelsiusToFahrenheit(item[2]), item[3]))
            conn.close()
            return list
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


db = GardenDatabase()
db.getTimeTempAndHumidity()
#cur = conn.cursor()
#
#cur.execute("SELECT * FROM general;")
#
#list = cur.fetchall()
#
#print(list)
#
#
#conn.close()
