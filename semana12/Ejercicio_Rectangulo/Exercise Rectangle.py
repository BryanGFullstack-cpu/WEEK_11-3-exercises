#ejercicio 1 rectangulo



class Rectangle:
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("There is a negative value, the values must be positive")

        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)


try:
    height = float(input("insert height: "))
    width = float(input("insert width: "))

    rectangle = Rectangle(width, height)

    print("Area:", rectangle.get_area())
    print("Perimeter:", rectangle.get_perimeter())

except ValueError as e:
    print(e)
