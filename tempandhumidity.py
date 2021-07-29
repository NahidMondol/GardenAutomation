import time
import board
import adafruit_sht4x


class TemperatureAndHumidity:
    sht = None

    def __init__(self):
        """Initialize the class by setting sht variable to obtain
           the I2C pins which contain the SHT40
        """
        self.sht = adafruit_sht4x.SHT4x(board.I2C())


    def getTemperature(self):
        """Return the current temperature obtained from the SHT40"""
        return self.sht.temperature


    def getHumidity(self):
        """Return the current relative humidity obtained from the SHT40"""
        return self.sht.relative_humidity

#
#stats = TemperatureAndHumidity()
#
#while True:
#    print(stats.getTemperature())
#    print(stats.getHumidity())
#    time.sleep(1)
