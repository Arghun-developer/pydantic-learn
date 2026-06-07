# class is like a blueprint for creating objects

class Dog:
    # __init__ runs automatically when you create a Dog
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):     #behaviour
        return f"{self.name} is {self.age} years old and says: Woof!"
    
# creating instances from Dog class blueprint


dog1 = Dog(name="Max", age="4")
dog2 = Dog(name="lina", age=7)

# print(dog1.name)
# print(dog1.age)
# print(dog2.name)
# print(dog2.age)
print(dog2.bark())