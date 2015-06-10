## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass
    
## Dog is a class that is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## From Dog get the name attribute and set it to name
        self.name = name
        
## Cat is-a class that is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## From Cat get the name attribute and set it to name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## From Person get the name attribute and set it to name
        self.name = name
        
        ## Person has-a pet of some kind
        self.pet = None
        
## Employee is class that is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## WTF does this do???
        super(Employee, self).__init__(name)
        ## From self get the salary attribute and set it to salary
        self.salary = salary
        
## Fish is-a object
class Fish(object):
    pass
    
## Salmon is-a Fish
class Salmon(Fish):
    pass
    
## Halibut is-a Fish
class Halibut(Fish):
    pass
    
    
## Rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## From mary get the pet attribute and set it to satan
mary.pet = satan

## Set frank to an instance of class Employee with parameters "Frank, and 120000
frank = Employee("Frank", 120000)

## From Frank get the pet attribute and set it to rover
frank.pet = rover

## Set flipper to an instance of class Fish
flipper = Fish()

## Set crouse to an instance of Salmon
crouse = Salmon()

## set harry to an instance of Halibut()
harry = Halibut()
