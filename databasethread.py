import time
import threading
import queue
from database import GardenDatabase

class GardenDatabaseThread(threading.Thread):

    threadID = None
    stopped = False
    GardenDatabase = None
    temperature = None
    humidity = None
    moistureLevel = None

    def __init__(self, threadID, *args):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.GardenDatabase = GardenDatabase()
        self.temperature = args[0]
        self.humidity = args[1]
        self.mositureLevel = args[2]


    def run(self):
        print("Running Database Thread")
        while not self.stopped:
            self.GardenDatabase.insertData(self.temperature, self.humidity, self.moistureLevel)
            print("Inserted Data")
            time.sleep(10)


    def stopThread(self):
        self.stopped = True


#thread = GardenDatabaseThread(1)
#thread.run(1, 2, 3)
