import time
import busio
from conversions import Conversions
from board import SCL, SDA
from adafruit_seesaw.seesaw import Seesaw

class SoilSensor:

    i2s_bus = None
    ss = None

    def __init__(self):
        """Initialize variables to detect the sensor"""
        self.i2c_bus = busio.I2C(SCL, SDA)
        self.ss = Seesaw(self.i2c_bus, addr=0x36)


    def getMoistureLevel(self):
        """Return the moisture level detected from the sensor"""
        return self.ss.moisture_read()


    def getTemperature(self):
        """Return the temperature detected from the sensor in Fahrenheit"""
        return Conversions.convertCelsiusToFahrenheit(self.ss.get_temp())


#soilSensor = SoilSensor()
#
#while True:
#    print("Moisture: {}, Temperature: {}".format(str(soilSensor.getMoistureLevel()), str(soilSensor.getTemperature())))
#    time.sleep(1)
