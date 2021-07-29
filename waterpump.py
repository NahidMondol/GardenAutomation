import time
import RPi.GPIO as GPIO

class WaterPump:

    warningMessage = "The GPIO pin has not been specified for this pump"
    waterpump = None

    def __init__(self, pin):
        self.waterpump = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.waterpump, GPIO.OUT)


    def cleanGPIO(self):
        GPIO.cleanup()


    def setGPIOPin(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.waterpump, GPIO.OUT)


    def activatePump(self):
        if self.waterpump is None:
            print(self.warningMessage)
        else:
            GPIO.output(self.waterpump, GPIO.HIGH)
            print("Pump Activated")


    def deactivatePump(self):
        if self.waterpump is None:
            print(self.warningMessage)
        else:
            GPIO.output(self.waterpump, GPIO.LOW)
            print("Pump Deactivated")


#pump = WaterPump(4)
#
#for i in range(10):
#    pump.activatePump()
#    time.sleep(2)
#    pump.deactivatePump()
#    time.sleep(2)
#
#pump.cleanGPIO()
