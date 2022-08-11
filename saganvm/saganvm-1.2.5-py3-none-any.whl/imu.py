from random import random
from .i2c import I2cDevice
from collections import namedtuple
import random
# # LSM9DS0 Gyro Registers
# CTRL_REG1_G = 0x20
# CTRL_REG2_G = 0x21
# CTRL_REG3_G = 0x22
# CTRL_REG4_G = 0x23
# CTRL_REG5_G = 0x24
#
# # LSM9DS0 Accel and Magneto Registers
# CTRL_REG1_XM = 0x20
# CTRL_REG2_XM = 0x21
# CTRL_REG3_XM = 0x22
# CTRL_REG4_XM = 0x23
# CTRL_REG5_XM = 0x24
# CTRL_REG6_XM = 0x25
# CTRL_REG7_XM = 0x26


AccelerometerMeasurement = namedtuple(
    'AccelerometerMeasurement',
    'x y z'
)


GyroscopeMeasurement = namedtuple(
    'GyroscopeMeasurement',
    'x y z'
)


MagnetometerMeasurement = namedtuple(
    'MagnetometerMeasurement',
    'x y z'
)


class Lsm9ds0I2cDevice(I2cDevice):
    """
    This overrides the read method to toggle the high bit in the register address.
    This is needed for multi-byte reads.
    """
    def read(self, cmd, length):
        return 0.0


class Accelerometer(Lsm9ds0I2cDevice):
    # These values come from the LSM9DS0 data sheet p13 table3 in the row about sensitivities.
    acceleration_scale = 0.000732 * 9.80665
    magnetometer_scale = 0.00048

    def configure(self, args):
        pass

    def measure(self):
        """
        :return: acceleration (X, Y, Z triple in m s^-1)
        """
        xvalues = [0.065, 0.072, 0.065, 0.072, 0.072, 0.057, 0.065, 0.086, 0.072, 0.065, 0.086, 0.057, 0.05, 0.057, 0.065, 0.05, 0.043, 0.079, 0.057, 0.065]
        yvalues = [-1.967, -1.974, -1.945, -1.953, -1.981, -1.931, -1.967, -1.902, -1.938, -1.953, -1.924, -1.96, -1.96, -1.974, -1.974, -1.988, -1.974, -1.945, -1.96, -1.953]
        zvalues = [9.727, 9.648, 9.691, 9.712, 9.698, 9.712, 9.705, 9.72, 9.698, 9.705, 9.72, 9.727, 9.698, 9.705, 9.72, 9.734, 9.727, 9.698, 9.705, 9.705]
        i = random.randint(0,19)
        # return AccelerometerMeasurement(0.154337, -2.756531, 10.7677017)
        return AccelerometerMeasurement(xvalues[i], yvalues[i], zvalues[i])

    @property
    def x(self):
        return 0.0

    @property
    def y(self):
        return 0.0

    @property
    def z(self):
        return 9.8


class Magnetometer(Lsm9ds0I2cDevice):
    # These values come from the LSM9DS0 data sheet p13 table3 in the row about sensitivities.
    acceleration_scale = 0.000732 * 9.80665
    magnetometer_scale = 0.00048

    def self_test(self):
        return True

    def configure(self, args):
        return

    def measure(self):
        """
        :return: magnetic field (X, Y, Z triple in mgauss)
        """
        
        xvalues = [-0.183, -0.184, -0.182, -0.182, -0.179, -0.182, -0.176, -0.177, -0.184, -0.186, -0.174, -0.175, -0.18, -0.182, -0.179, -0.177, -0.177, -0.174, -0.177, -0.178]
        yvalues = [0.418, 0.416, 0.416, 0.419, 0.421, 0.42, 0.421, 0.42, 0.417, 0.42, 0.42, 0.423, 0.42, 0.422, 0.43, 0.425, 0.42, 0.42, 0.423, 0.422]
        zvalues = [-0.191, -0.189, -0.185, -0.185, -0.17, -0.189, -0.19, -0.187, -0.187, -0.184, -0.194, -0.185, -0.183, -0.191, -0.186, -0.189, -0.19, -0.182, -0.192, -0.184]
        i = random.randint(0,19)
        # return MagnetometerMeasurement(-0.21344, 0.44022, -0.32132)
        return MagnetometerMeasurement(xvalues[i], yvalues[i], zvalues[i])

    @property
    def x(self):
        return 0.0

    @property
    def y(self):
        return 0.0

    @property
    def z(self):
        return 0.0


class Gyroscope(Lsm9ds0I2cDevice):
    gyroscope_scale = 0.070

    def self_test(self):
        return True

    def configure(self, args):
        return

    def measure(self):
        """
        :return: X, Y, Z triple in degrees per second
        """
        xvalues = [-0.28, -0.35, -0.28, -0.35, 0, -0.35, -0.35, -0.21, -0.28, -0.49, -0.56, -0.35, -0.28, -0.07, -0.42, -0.07, -0.07, -0.35, -0.35, -0.21]
        yvalues = [0.56, 0.35, 0.42, 0.42, 0.35, 0.49, 0.42, 0.42, 0.42, 0.35, 0.21, 0.56, 0.35, 0.49, 0.28, 0.49, 0.42, 0.28, 0.35, 0.42]
        zvalues = [0.49, 0.42, 0.35, 0.28, 0.56, 0.56, 0.49, 0.49, 0.49, 0.49, 0.35, 0.28, 0.49, 0.42, 0.49, 0.49, 0.42, 0.63, 0.42, 0.56]
        i = random.randint(0,19)
        # return GyroscopeMeasurement(366.3100, 22.26, 131.67)
        return GyroscopeMeasurement(xvalues[i], yvalues[i], zvalues[i])

    @property
    def x(self):
        return 0.0

    @property
    def y(self):
        return 0.0

    @property
    def z(self):
        return 0.0