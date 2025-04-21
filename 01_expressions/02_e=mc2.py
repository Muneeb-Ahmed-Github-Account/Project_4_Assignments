def energy():

    c :float = 299792458 

    m = float(input("Enter kilos of mass: "))

    print("e = m*c^2")

    print("Mass = "+ str(m) + " kg")

    print("C = " + str(c) + " m/s")

    print("E = " + str(m * c ** 2) + " joules")

if __name__ == "__main__":
    energy()