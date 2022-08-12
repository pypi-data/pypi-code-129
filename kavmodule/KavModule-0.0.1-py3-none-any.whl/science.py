from Read_CSV import atomic_mass, atomic_num, symbol, element

class science:

    # Pass mass and volume as arguments
    # Returns density

    def density(mass, volume):
        return mass / volume

    # Pass distance and time as arguments
    # Returns speed

    def speed(distance, time):
        return distance / time

    # Pass mass and velocity as arguments
    # Returns momentum

    def momentum(mass, velocity):
        return mass * velocity

    # Pass final and initial velocities and time as arguments
    # Returns acceleration

    def acceleration(final, initial, time):
        return (final - initial) / time

    # Pass mass and acceleration as arguments
    # Returns force

    def force(mass, acceleration):
        return mass * acceleration

    # Pass mass as argument
    # Returns weight

    def weight(mass):
        return mass * 9.8

    # Pass weight as argument
    # Returns mass

    def mass(weight):
        return weight / 9.8

    # Pass work and time as arguments
    # Returns power

    def power(work, time):
        return work / time

    # Pass froce and distance as arguments
    # Returns work

    def work(force, distance):
        return force * distance

    # Pass mass and height as arguments
    # Returns gravitational potential energy

    def GPE(mass, height):
        return mass * 9.8 * height

    # Pass mass and velocity as arguments
    # Returns kinetic energy    

    def ke(mass, velocity):
        return 0.5 * mass * (velocity ** 2)
    
    # Pass Atomic Number as argument
    # Returns Atomic Number, Element Name, Element Symbol, and Atomic Mass
    
    def period_info(number):
        atomic_number = "Atomic Number: " + str(atomic_num[number - 1])
        element_name = "Element: " + str(element[number - 1])
        element_symbol = "Symbol: " + str(symbol[number - 1])
        atom_mass = "Atomic Mass: " + str(atomic_mass[number - 1])
        return atomic_number + "\n" + element_name + "\n" + element_symbol + "\n" + atom_mass