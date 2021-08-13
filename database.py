import psycopg2
from config import config

class GardenDatabase:

    def __init__(self):
        pass


    def getAll(self):
        """select all data from general and return a list of the data"""
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


    def insertData(self, temperature, humidity, moistureLevel):
        """Insert the time, temperature, humidity, and soil_moisture in the database"""
        conn = None
        try:
            params = config()
            conn =  psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("INSERT INTO general (recorded_timestamp, temperature, humidity, soil_moisture) VALUES (current_timestamp, %s, %s, %s);", (temperature, humidity, moistureLevel))
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


    def getTimeTempHumidityAndSoilMoisture(self):
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("SELECT general_id, recorded_timestamp, temperature, humidity, soil_moisture FROM general;")
            list = cur.fetchall()
            for item in list:
                print("ID {}\nTime {}\nTemperature {}\nHumidity {}".format(item[0], item[1], item[2], item[3], item[4]))
            conn.close()
            return list
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


#db = GardenDatabase()
#print(db.getTimeTempHumidityAndSoilMoisture())
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
