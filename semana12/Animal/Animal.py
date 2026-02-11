#animal dog and cat 


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "makes a sound"


class Dog(Animal):
    def speak(self):
        return "Guau"


class Cat(Animal):
    def speak(self):
        return "Miau"


# Ejemplos de uso
if __name__ == "__main__":
    dog = Dog("Firulais")
    cat = Cat("Misu")

    print(dog.speak())  # Guau
    print(cat.speak())  # Miau


    
