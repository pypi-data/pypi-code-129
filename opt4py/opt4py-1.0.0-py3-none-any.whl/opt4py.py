from __future__ import annotations


class Option:
    """
    A container class that handles seamlessly NoneType checks in a monadic way.
    """

    def __init__(self, value=None):
        """
        Initializes a new Option object with a given value (defaults to None).
        :param value: Value stored at first inside the Option.
        """
        self.value = value

    def is_none(self) -> bool:
        """
        Checks if the Option's value is None.
        :return: True if the Option is None.
        """
        return self.value is None

    def is_some(self) -> bool:
        """
        Checks if the Option contains something (opposite of is_none()).
        :return: True if the Option is not None.
        """
        return self.value is not None

    def unwrap(self):
        """
        Unwraps the Option object into only its value.
        :return: The Option's value.
        """
        return self.value

    def unwrap_or(self, default):
        """
        Unwraps the Option object into only its value. If it is None, return a default value.
        :param default: Value used if the Option is_none().
        :return: The Option's value or default.
        """
        if self.is_some():
            return self.value
        return default

    def map(self, f) -> Option:
        """
        Maps a method to the Option's value if it is not None.
        :param f: Method to map.
        :return: A new Option with the value mapped using method f.
        """
        if self.is_some():
            return Option(f(self.value))
        return Option()

    def __add__(self, other) -> Option:
        if self.is_some():
            if isinstance(other, Option):
                return Option(self.value + other.value)
            return Option(self.value + other)
        return Option()

    def __sub__(self, other) -> Option:
        if self.is_some():
            if isinstance(other, Option):
                return Option(self.value - other.value)
            return Option(self.value - other)
        return Option()

    def __mul__(self, other) -> Option:
        if self.is_some():
            if isinstance(other, Option):
                return Option(self.value * other.value)
            return Option(self.value * other)
        return Option()

    def __truediv__(self, other) -> Option:
        if self.is_some():
            if isinstance(other, Option):
                return Option(self.value / other.value)
            return Option(self.value / other)
        return Option()

    def __floordiv__(self, other) -> Option:
        if self.is_some():
            if isinstance(other, Option):
                return Option(self.value // other.value)
            return Option(self.value // other)
        return Option()

    def __mod__(self, other) -> Option:
        if self.is_some():
            if isinstance(other, Option):
                return Option(self.value % other.value)
            return Option(self.value % other)
        return Option()

    def __pow__(self, other) -> Option:
        if self.is_some():
            if isinstance(other, Option):
                return Option(self.value ** other.value)
            return Option(self.value ** other)
        return Option()

    def __rshift__(self, other) -> Option:
        if self.is_some():
            if isinstance(other, Option):
                return Option(self.value >> other.value)
            return Option(self.value >> other)
        return Option()

    def __lshift__(self, other) -> Option:
        if self.is_some():
            if isinstance(other, Option):
                return Option(self.value << other.value)
            return Option(self.value << other)
        return Option()

    def __and__(self, other) -> Option:
        if self.is_some():
            if isinstance(other, Option):
                return Option(self.value & other.value)
            return Option(self.value & other)
        return Option()

    def __or__(self, other) -> Option:
        if self.is_some():
            if isinstance(other, Option):
                return Option(self.value | other.value)
            return Option(self.value | other)
        return Option()

    def __xor__(self, other) -> Option:
        if self.is_some():
            if isinstance(other, Option):
                return Option(self.value ^ other.value)
            return Option(self.value ^ other)
        return Option()

    __radd__ = __add__
    __rsub__ = __sub__
    __rmul__ = __mul__
    __rtruediv__ = __truediv__
    __rfloordiv__ = __floordiv__
    __rmod__ = __mod__
    __rpow__ = __pow__
    __rrshift__ = __rshift__
    __rlshift__ = __lshift__
    __rand__ = __and__
    __ror__ = __or__
    __rxor__ = __xor__

    def __neg__(self):
        if self.is_some():
            return Option(-self.value)
        else:
            return Option()

    def __pos__(self):
        if self.is_some():
            return Option(+self.value)
        else:
            return Option()

    def __invert__(self):
        if self.is_some():
            return Option(~self.value)
        else:
            return Option()

    def __iadd__(self, other) -> Option:
        return Option(self + other)

    def __isub__(self, other) -> Option:
        return Option(self - other)

    def __imul__(self, other) -> Option:
        return Option(self * other)

    def __idiv__(self, other) -> Option:
        return Option(self / other)

    def __ifloordiv__(self, other) -> Option:
        return Option(self // other)

    def __imod__(self, other) -> Option:
        return Option(self % other)

    def __ipow__(self, other) -> Option:
        return Option(self ** other)

    def __irshift__(self, other) -> Option:
        return Option(self >> other)

    def __ilshift__(self, other) -> Option:
        return Option(self << other)

    def __iand__(self, other) -> Option:
        return Option(self & other)

    def __ior__(self, other) -> Option:
        return Option(self | other)

    def __ixor__(self, other) -> Option:
        return Option(self ^ other)

    def __lt__(self, other) -> Option:
        if self.is_some():
            if isinstance(other, Option):
                return self.value < other.value
            return self.value < other
        return False

    def __gt__(self, other) -> Option:
        if self.is_some():
            if isinstance(other, Option):
                return self.value > other.value
            return self.value > other
        return False

    def __le__(self, other) -> Option:
        if self.is_some():
            if isinstance(other, Option):
                return self.value <= other.value
            return self.value <= other
        return False

    def __ge__(self, other) -> Option:
        if self.is_some():
            if isinstance(other, Option):
                return self.value >= other.value
            return self.value >= other
        return False

    def __eq__(self, other) -> Option:
        if self.is_some():
            if isinstance(other, Option):
                return self.value == other.value
            return self.value == other
        return False

    def __ne__(self, other) -> Option:
        if self.is_some():
            if isinstance(other, Option):
                return self.value != other.value
            return self.value != other
        return False

    def __repr__(self):
        return f"Option({self.value})"
