import time
from tempandhumidity import TemperatureAndHumidity
from soilsensor import SoilSensor
from database import GardenDatabase

def runProgram(status, soilSensor):
    while True:
        #db = GardenDatabase()
        #db.insertData(status.getTemperature(), status.getHumidity())
        print("SHT40- Temperature: {}, Humidity: {}".format(status.getTemperature(), status.getHumidity()))
        print("SoilSensor- Temperature: {}, Moisture: {}".format(soilSensor.getTemperature(), soilSensor.getMoistureLevel()))
        time.sleep(1)
        #db.getTimeTempAndHumidity()


status = TemperatureAndHumidity()
soilSensor = SoilSensor()
#db = GardenDatabase()

#print(db.getAll())
runProgram(status, soilSensor)
