"""
module implementing a class to represent 3D vectors and associated
functions such as scalar and cross products. e.g.::

 >> from trm.utils.vec3 import *
 >> a = Vec3(1,2,-1.5)
 >> b = Vec3(-2,1,0)
 >> c = a + b
 >> sp = dot(a,b)
 >> cp = cross(a,b)

"""

import sys, os, re, copy
import math
import numpy as np

class Vec3(object):
    """
    A simple 3D vector class. Attributes: 'x', 'y' and 'z'. Vec3 objects
    can be added, subtracted, scaled, normalised. Scalar and cross products
    can be taken.

    Examples:

      r = Vec3()       # sets r = (0,0,0)
      r = Vec3(1,2,3)  # sets r = (1,2,3)
      r = a + b        # adds two Vec3s to make another.
      r = a - b        # subtract two Vec3s to make another.
      a =- b           # subtracts b from a in place
      x = r[0]         # gets the x ordinate
      y = r.y          # gets the y ordinate
      r *= 2.          # multiply all ordinates by 2
      print(r.norm())  # Print length of a Vec3
      sp = dot(a,b)    # takes scalar or dot product of two Vec3s
      cv = cross(a,b)  # takes cross product of two Vec3s
      a = -b           # set a to be negative of b

    Argument types are not checked,
    """

    def __init__(self, x=0., y=0., z=0.):
        """
        Initialise a Vec3. Arguments, x,y,z should
        be floats.
        """
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'({self.x},{self.y},{self.z})'

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __add__(self, other):
        temp = copy.copy(self)
        temp += other
        return temp

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __sub__(self, other):
        temp = copy.copy(self)
        temp -= other
        return temp

    def __imul__(self, other):
        self.x *= other
        self.y *= other
        self.z *= other
        return self

    def __mul__(self, other):
        temp = copy.copy(self)
        temp *= other
        return temp

    def __rmul__(self, other):
        temp = copy.copy(self)
        temp *= other
        return temp

    def __itruediv__(self, other):
        self.x /= other
        self.y /= other
        self.z /= other
        return self

    def __truediv__(self, other):
        temp = copy.copy(self)
        temp /= other
        return temp

    def __neg__(self):
        temp = copy.copy(self)
        temp *= -1
        return temp

    def __getitem__(self, i):
        if i == 0:
            return self.x
        elif i == 1:
            return self.y
        elif i == 2:
            return self.z
        else:
            raise ValueError('Index out of range 0:3')

    def sqnorm(self):
        """
        Returns Euclidean length squared of the vector
        """
        return self.x**2 + self.y**2 + self.z**2

    def norm(self):
        """
        Returns Euclidean length of the vector
        """
        return math.sqrt(self.sqnorm())

    def unit(self):
        """
        Returns vector as a unit vector in same direction
        """
        leng = math.sqrt(self.sqnorm())
        if leng == 0.:
            raise ValueError(
                "Vec3.unit: cannot normalise a zero vector"
            )
        return self / leng

    def dot(self, other):
        """
        Returns the scalar or dot product of self with other, a 3-vector
        """
        return self.x*other.x+self.y*other.y+self.z*other.z

    def cross(self, other):
        """
        Computes the vector or cross product of self with other, a 3-vector
        """
        return Vec3(self.y*other.z-self.z*other.y,
                    self.z*other.x-self.x*other.z,
                    self.x*other.y-self.y*other.x)

def dot(a, b):
    """
    Computes the scalar or dot product of two 3-vectors. More
    equal treatment of the two inputs than the class method
    equivalent.
    """
    return a.x*b.x+a.y*b.y+a.z*b.z

def cross(a, b):
    """Computes the vector or cross product of two 3-vectors. More equal
    treatment of the two inputs than the class method equivalent.

    Returns a Vec3 of the result.
    """
    return Vec3(a.y*b.z-a.z*b.y, a.z*b.x-a.x*b.z, a.x*b.y-a.y*b.x)

