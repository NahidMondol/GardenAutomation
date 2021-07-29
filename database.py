import psycopg2
from config import config

class GardenDatabase:

    def __init__(self):
        pass


    def convertCelsiusToFahrenheit(tempInCelsius):
        return ((tempInCelsius * 9/5) + 32)


    def getAll(self):
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("SELECT * FROM general;")
            list = cur.fetchall()
            cur.close()
            return list
        finally:
            if conn is not None:
                conn.close()


    def insertData(self, temperature, humidity):
        conn = None
        try:
            params = config()
            conn =  psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("INSERT INTO general (recorded_timestamp, temperature, soil_humidity) VALUES (current_timestamp, %s, %s);", (GardenDatabase.convertCelsiusToFahrenheit(temperature), humidity))
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


    def getTimeTempAndHumidity(self):
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("SELECT general_id, recorded_timestamp, temperature, soil_humidity FROM general;")
            list = cur.fetchall()
            for item in list:
                print("ID {}\nTime {}\nTemperature {}\nHumidity {}".format(item[0], item[1], item[2], item[3]))
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
