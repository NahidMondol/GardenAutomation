import time
import queue
from tempandhumiditythread import TemperatureAndHumidityThread
from tempandhumidity import TemperatureAndHumidity
from soilsensor import SoilSensor
from soilsensorthread import SoilSensorThread
from database import GardenDatabase
from databasethread import GardenDatabaseThread
from waterpump import WaterPump

def runProgram(status, soilSensor, waterPump):
    while True:
        #db = GardenDatabase()
        #db.insertData(status.getTemperature(), status.getHumidity(), soilSensor.getMoistureLevel())
        print("SHT40- Temperature: {}, Humidity: {}".format(status.getTemperature(), status.getHumidity()))
        print("SoilSensor- Temperature: {}, Moisture: {}".format(soilSensor.getTemperature(), soilSensor.getMoistureLevel()))
        #time.sleep(1)
        #db.getTimeTempHumidityAndSoilMoisture()


def runProgram(StatusThread, SoilSensorThread, DatabaseThread, WaterPump):
    StatusThread.start()
    time.sleep(0.1)
    SoilSensorThread.start()
    #time.sleep(0.1)
    #dataQueue = queue.Queue()
    #DatabaseThread.start()


StatusThread = TemperatureAndHumidityThread(1)
SoilSensorThread = SoilSensorThread(2)
DatabaseThread = GardenDatabaseThread(3, StatusThread.currentTemp, StatusThread.currentHumidity, SoilSensorThread.moistureLevel)
Pump = WaterPump()

runProgram(StatusThread, SoilSensorThread, DatabaseThread, Pump)
