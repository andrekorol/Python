# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass


# Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        # Dog has-a name
        self.name = name

    def bark(self):
        print("Roof roof!")

        
# Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        # Cat has-a name
        self.name = name

    def meow(self):
        print("Meow!")

    
# Person is-a object
class Person(object):

    def __init__(self, name):
        # Person has-a name
        self.name = name

        # Person has-a pet of some kind
        self.pet = None
        

# Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        # ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        # Employee has-a salary
        self.salary = salary
        self.children = []
        
    def set_children(self):
        print(f"Enter how many children {self.name} have")
        n = int(input("> "))
        for i in range(0, n):
            print(f"Enter the name of the child of number {i + 1}: ")
            kid = input("> ")
            self.children.append(kid)
             
    def get_children(self):
        for kid in self.children:
            print(kid)

            
# Fish is-a object
class Fish(object):
    pass


# Salmon is-a Fish
class Salmon(Fish):
    pass


# Halibut is-a Fish
class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# mary has-a pet named satan and satan is-a Cat
mary.pet = satan

# frank is-a Employee
frank = Employee("Frank", 120000)

# frank has-a pet named rover and rover is-a Dog
frank.pet = rover

# flipper is-a Fish
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()
