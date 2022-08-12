import depenv


class Bird(depenv.Injectable):
    def speak(self):
        return "chirp"


class Duck(Bird):
    def speak(self):
        return "quack"


class Parrot(Bird):
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " wanna cracker?"
