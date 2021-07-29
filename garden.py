import time
from tempandhumidity import TemperatureAndHumidity
from database import GardenDatabase

def runProgram(status):
    while True:
        db = GardenDatabase()
        db.insertData(status.getTemperature(), status.getHumidity())
        print(status.getTemperature())
        print(status.getHumidity())
        time.sleep(5)
        db.getTimeTempAndHumidity()


status = TemperatureAndHumidity()
#db = GardenDatabase()

#print(db.getAll())
runProgram(status)
