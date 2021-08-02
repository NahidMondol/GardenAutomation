import time
import threading
from soilsensor import SoilSensor

class SoilSensorThread(threading.Thread):

    stopped = False
    sensor = None
    threadID = None

    def __init__(self, threadID):
       threading.Thread.__init__(self)
       self.sensor = SoilSensor()
       self.threadID = threadID


    def run(self):
       counter = 0
       while not self.stopped:
          print(self.sensor.getMoistureLevel())
          counter += 1
          if counter >= 5:
              self.stopThread()


    def stopThread(self):
       self.stopped = True


thread = SoilSensorThread(1)

thread.run()
