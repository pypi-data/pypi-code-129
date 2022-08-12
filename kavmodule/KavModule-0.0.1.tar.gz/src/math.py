from cmath import sqrt
from codecs import backslashreplace_errors


class math:

    # Pass 2 arguments
    # Returns sum

    def add(x, y):
        return x + y
    
    # Pass 2 arguments
    # Returns difference

    def subtract(x, y):
        return x - y
    
    # Pass 2 arguments
    # Returns product

    def multiply(x, y):
        return x * y
    
    # Pass 2 arguements
    # Returns quotient

    def divide(x, y):
        return x / y
    
    # Pass 2 arguments
    # Returns result

    def exponentiate(x, y):
        return x ** y
    
    # Pass a list as argument
    # Returns mean

    def mean(list):
        sum = sum(list)
        
        return sum / len(list)
    
    # Pass a list as argument
    # Returns median
    # LIST MUST BE ORDERED

    def median(list):
        isEven = False
        
        if len(list) % 2 == 0:
            isEven = True
        
        if isEven == True:
            median_place = len(list) / 2
        else:
            median_place = (len(list) + 1) / 2
        
        return int(list[int(median_place - 1)]) + 0.5
    
    # Pass a list as argument
    # Returns range

    def range(list):
        max = max(list)
        min = min(list)

        return max - min
    
    # Pass target outcomes and total outcomes as arguments
    # Returns probability as a decimal

    def probability(target, total):
        return target / total

    # Pass coordinates as arguments
    # Returns distance between coordinates
    # PASS COORDINATES AS (X1, Y1, X2, Y2)

    def distance(x1, y1, x2, y2):
        x_diff = (x1 - x2)
        x_diff_squared = math.exponentiate(x_diff, 2)

        y_diff = (y1 - y2)
        y_diff_squared = math.exponentiate(y_diff, 2)

        xy_sum = x_diff_squared + y_diff_squared
        xy_sum_root = sqrt(xy_sum)
        
        return xy_sum_root

    # Pass coordinates as arguments
    # Returns slope
    # PASS COORDINATES AS (X1, Y1, X2, Y2)

    def slope(x1, y1, x2, y2):
        y_diff = (y2 - y1)

        x_diff = (x2 - x1)

        return y_diff / x_diff
    
    # Pass coordinates as arguments
    # Returns y-intercept
    # PASS COORDINATES AS (X1, Y1, X2, Y2)
    # FUNCTION MUST BE LINEAR

    def y_intercept(x1, y1, x2, y2):
        slope = math.slope(x1, y1, x2, y2)
        
        step1 = slope(x1)
        
        if step1 > 0:
            y_intercept = y1 - step1
        else:
            y_intercept = y1 + step1
        
        return y_intercept
    
    # Pass coordinates as arguments
    # Returns midpoint
    # PASS COORDINATES AS (X1, Y1, X2, Y2)
    # RETURN FORM WILL BE A TUPLE

    def midpoint(x1, y1, x2, y2):
        x_sum = x1 + x2
        y_sum = y1 + y2

        x_coor = x_sum / 2
        y_coor = y_sum / 2

        return (x_coor, y_coor)
    
    # Pass b and a values of quadratic equation as arguments
    # Returns sum of solutions

    def sum_of_solutions(b, a):
        return -b / a
    
    # Pass c and a values of quadratic equation as arguments
    # Returns product of solutions

    def product_of_solutions(c, a):
        return c / a
    
    # Pass b and a values of quadratic equation as arguements
    # Returns x-coordinate of vertex of parabola

    def x_vert_parab(b, a):
        return (-b) / (2 * a)
    
    # Pass two sides of a triangle as arguments
    # Returns hypotenuse
    # TRIANGLE MUST BE A RIGHT TRIANGLE

    def find_hypot(a, b):
        c_squared = (a ** 2) + (b ** 2)
        return sqrt(c_squared)
    
    # Pass two measures of the rectangle as arguments
    # Returns perimeter

    def perim_rect(x, y):
        double_x = 2 * x
        double_y = 2 * y

        return double_x + double_y
    
    # Pass radius as an argument
    # Returns area of circle

    def area_circ(r):
        return 3.14 * (r **2)
    
    # Pass radius as an argument
    # Returns circumference

    def circumference(r):
        return 2 * 3.14 * r

    # Pass base and height as arguments
    # Returns area of triangle

    def area_tri(base, height):
        return 0.5 * base * height

    # Pass radians as arguement
    # Returns degrees

    def toDegrees(rad):
        return rad * (180 / 3.14)
    
    # Pass degrees as argument
    # Returns radians

    def toRadians(deg):
        return deg * (3.14 / 180)