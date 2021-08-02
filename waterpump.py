import time
import RPi.GPIO as GPIO

class WaterPump:

    waterPumpPin = 4

    def __init__(self):
        self.setGPIOPin()


    def cleanGPIO(self):
        GPIO.cleanup()


    def setGPIOPin(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.waterPumpPin, GPIO.OUT)


    def activatePump(self):
        GPIO.output(self.waterPumpPin, GPIO.HIGH)
        print("Pump Activated")


    def deactivatePump(self):
        GPIO.output(self.waterPumpPin, GPIO.LOW)
        print("Pump Deactivated")


#pump = WaterPump()
#
#for i in range(3):
#    pump.activatePump()
#    time.sleep(2)
#    pump.deactivatePump()
#    time.sleep(2)
#
#pump.cleanGPIO()
