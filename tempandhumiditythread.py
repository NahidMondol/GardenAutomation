import threading
import time
from tempandhumidity import TemperatureAndHumidity

class TemperatureAndHumidityThread(threading.Thread):

    sensor = None
    currentTemp = None
    currentHumidity = None

    def __init__(self, threadID):
       self.sensor = TemperatureAndHumidity()
       threading.Thread.__init__(self)
       self.threadID = threadID


    def run(self):
        print("Starting TempAndHumidity Thread")
        #while True:
        self.currentTemp = self.sensor.getTemperature()
        self.currentHumidity = self.sensor.getHumidity()
        print(self.currentTemp)
        print(self.currentHumidity)


threadOne = TemperatureAndHumidityThread(1)
threadOne.start()
