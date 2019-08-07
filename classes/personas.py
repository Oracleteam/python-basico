class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello my name is {} and im {} yo".format(self.name, self.name))


if __name__ == '__main__':
    persons = Person("Raul", 15)
    persons.say_hello()
