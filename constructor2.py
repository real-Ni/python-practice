class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"{self.name} talks")

person1 = Person("Aarushi")
person1.talk()