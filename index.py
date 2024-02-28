class Car:
    def __init__(self, brand, color, cleanliness):
        self.brand = brand
        self.color = color
        self.cleanliness = cleanliness

    def clean(self):
        self.cleanliness = "clean"
        print("The {} {} is now clean.".format(self.color, self.brand))


class Guy:
    def __init__(self, name):
        self.name = name

    def clean_car(self, car):
        print("{} is cleaning his {} {} car...".format(self.name, car.color, car.brand))
        car.clean()
        print("{} finishes cleaning his {} {} car.".format(self.name, car.color, car.brand))


if __name__ == "__main__":
    my_car = Car("Toyota", "blue", "dirty")
    guy = Guy("John")
    guy.clean_car(my_car)
