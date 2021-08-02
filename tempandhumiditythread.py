import threading
import time
import sys
from tempandhumidity import TemperatureAndHumidity

class TemperatureAndHumidityThread(threading.Thread):

    stop = False
    sensor = None
    currentTemp = None
    currentHumidity = None

    def __init__(self, threadID):
       threading.Thread.__init__(self)
       self.sensor = TemperatureAndHumidity()
       self.threadID = threadID


    def run(self):
        """Obtain the temperature and humidity from the sht40
           until the thread is stopped
        """
        counter = 0
        print("Starting TempAndHumidity Thread")
        while not self.stop:
            self.currentTemp = self.sensor.getTemperature()
            self.currentHumidity = self.sensor.getHumidity()
            print(self.currentTemp)
            print(self.currentHumidity)
            counter += 1
            time.sleep(1)
            if counter >= 10:
                self.closeThread()


    def closeThread(self):
        """Call this method to close the thread"""
        self.stop = True


#threadOne = TemperatureAndHumidityThread(1)
#threadOne.start()
