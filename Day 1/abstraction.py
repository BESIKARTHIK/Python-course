class Animal:
    def sound(self):
        pass
class Dog(Animal):
        def sound(self):
             print("Barks")
dog = Dog()
dog.sound()