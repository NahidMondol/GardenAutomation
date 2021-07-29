import threading
import time
from tempandhumidity import TemperatureAndHumidity

class TemperatureAndHumidityThread (threading.Tread):

    currentTemp = None
    currentHumidity = None

    def __init__(self, threadID):
       threading.Thread.__init__(self)
       self.threadID = threadID


    def run(self):
        print("Starting TempAndHumidity Thread")
        #while True:
        self.currentTemp = TemperatureAndHumidity.getTemperature()
        self.currentHumidity = TemperatureAndHumidity.getHumidity()
        print(self.currentTemp)
        print(self.currentHumidity)


threadOne = TemperatureAndHumidityThread(1)

threadOne.start()
