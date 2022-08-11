import time
from .i2c import I2cDevice
from collections import namedtuple
import random

BarometerMeasurement = namedtuple(
    'BarometerMeasurement',
    'temperature pressure humidity'
)

class Barometer(I2cDevice):

    """
    Interface for BME280 pressure and humidity
    """
    def read_raw_measurements(self):
        return 0.0, 0.0, 0.0

    def apply_calibration(self, t_raw, p_raw, h_raw, t_calib=None):
        pass
        return 0.0,0.0,0.0

    def measure(self):
        """
        :return: tuple of: temperature (C), pressure (Pa), humidity (% relative humidity)
        """
        
        tempvalues = [35.6915430212451, 35.6761269152164, 35.6812656169349, 35.6812656169349, 35.6658495126524, 35.6555721112526, 35.645294711017, 35.6555721112526, 35.6555721112526, 35.6761269152164, 35.6658495126524, 35.6812656169349, 35.6915430212451, 35.6812656169349, 35.6658495126524, 35.6761269152164, 35.6812656169349, 35.6761269152164, 35.6915430212451, 35.6761269152164]
        pressurevalues = [99469.5190141597, 99469.953206884, 99465.0235543781, 99465.0235543781, 99462.5744910502, 99466.6979475574, 99465.0548294721, 99472.4644454096, 99469.5811952884, 99469.953206884, 99462.5744910502, 99470.7902790197, 99466.63560648, 99465.0235543781, 99465.4577814496, 99464.186530587, 99465.0235543781, 99467.0698675403, 99475.2858366907, 99464.186530587]
        humidityvalues = [47.9176642820804, 47.9224443612569, 47.9225858247247, 47.9225858247247, 47.9221718864172, 47.921894135535, 47.9371966643314, 47.9426683604026, 47.9270876917519, 47.9328319392383, 47.937752907554, 47.9329735224184, 47.9124703179551, 47.9018104293374, 47.9013971915682, 47.9068629942847, 47.8862288827969, 47.901669205294, 47.8813065332034, 47.8808940493312]
        i = random.randint(0,19)
        #return BarometerMeasurement(26.276, 99528.47055, 48.8976)
        return BarometerMeasurement(tempvalues[i], pressurevalues[i], humidityvalues[i])



    @property
    def temperature(self):
        return 0.0

    @property
    def pressure(self):
        return 0.0

    @property
    def humidity(self):
        return 0.0
