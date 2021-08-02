import time
from tempandhumiditythread import TemperatureAndHumidityThread
from tempandhumidity import TemperatureAndHumidity
from soilsensor import SoilSensor
from soilsensorthread import SoilSensorThread
from database import GardenDatabase
from waterpump import WaterPump

def runProgram(status, soilSensor):
    while True:
        #db = GardenDatabase()
        #db.insertData(status.getTemperature(), status.getHumidity())
        print("SHT40- Temperature: {}, Humidity: {}".format(status.getTemperature(), status.getHumidity()))
        print("SoilSensor- Temperature: {}, Moisture: {}".format(soilSensor.getTemperature(), soilSensor.getMoistureLevel()))
        #time.sleep(1)
        #db.getTimeTempAndHumidity()


def runProgram(StatusThread, SoilSensorThread, WaterPump):
    StatusThread.start()
    time.sleep(0.1)
    SoilSensorThread.start()


StatusThread = TemperatureAndHumidityThread(1)
SoilSensorThread = SoilSensorThread(2)
Pump = WaterPump()
#db = GardenDatabase()

runProgram(StatusThread, SoilSensorThread, Pump)
