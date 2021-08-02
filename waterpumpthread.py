import threading
import time
from waterpump import WaterPump

class WaterPumpThread(threading.Thread):
    """This class will most likely not be needed"""

    stop = False
    threadID = None
    Pump = None
    setPumpActive = False

    def __init__(self, threadID):
       threading.Thread.__init__(self)
       self.threadID = threadID
       self.Pump = WaterPump()


    def run(self, activatePump):
       while not self.stop:
           if activatePump:
               self.Pump.activatePump()
               self.setPumpActive = True
               self.closeThread()
           else:
               self.Pump.deactivatePump()
               self.setPumpActive = False
               self.closeThread()



    def closeThread(self):
       self.stop = True


PumpThread = WaterPumpThread(1)
PumpThread.run(True)
