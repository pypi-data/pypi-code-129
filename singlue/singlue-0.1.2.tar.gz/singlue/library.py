from math import factorial


def one() -> int:
    return 1


def two() -> int:
    return 2


class Three:
    def __init__(self):
        self.value = 3

    def three(self):
        return self.value


def six() -> int:
    return factorial(3)
