# Function and Class difference

# A function stands alone
def greet(name):
    return f"Hello {name}"

# A class groups function + data together

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def identity(self):
        return f"Hello, my name is: {self.name}, I'm {self.age} years old!"
    
# print(greet("sahand"))

person1 = Person(name="sahand", age=27)

print(person1.identity())