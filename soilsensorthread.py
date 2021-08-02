import time
import threading
from soilsensor import SoilSensor

class SoilSensorThread(threading.Thread):

    stopped = False
    sensor = None
    threadID = None
    moistureLevel = None

    def __init__(self, threadID):
       threading.Thread.__init__(self)
       self.sensor = SoilSensor()
       self.threadID = threadID


    def run(self):
       """Method to run thread and obtain the moisture level"""
       print("Starting SoilSensor Thread")
       while not self.stopped:
          self.moistureLevel = self.sensor.getMoistureLevel()
          print(self.moistureLevel)
          time.sleep(1)


    def stopThread(self):
       self.stopped = True


#thread = SoilSensorThread(1)
#thread.run()
