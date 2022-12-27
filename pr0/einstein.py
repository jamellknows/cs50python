def einstein():
    import math
    mass = int(input("What is the mass of the object in kg? "))
    mass = math.ceil(mass)
    c = 3 *10**8
    return int(mass * c **2)