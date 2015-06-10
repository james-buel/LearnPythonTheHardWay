## class Parent implicitly inherits from the Python object class
class Parent(object):

    ## This function defines 'override' function with self as argument (attribute)
    def override(self):
        print "PARENT override()"
        
    ## This function defines the 'implicit' function with self as argument(attribute)
    def implicit(self):
        print "PARENT implicit()"
        
    ## This function defines the 'altered' function with self as an argument (attribute)
    def altered(self):
        print "PARENT altered()"

## class Child inherits from Parent class
class Child(Parent):

    ## This function overrides the Parent class function 'override' with self as argument (attribute)
    def override(self):
        print "CHILD override()"
        
    ## This function overrides the Parent class function 'altered' with self as argument (attribute)
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        ## return a proxy of 'altered()' that delegates method calls to Child class and self
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"
        
## set dad as an instance of 'Parent' class
dad = Parent()

## set son to an instance of 'Child' class
son = Child()


## from dad get the 'implicit' function and call it with parameters 'self' 
dad.implicit()

## from son get the 'implicit' function and call it with parameters 'self'
son.implicit()


## from dad get the 'override' function and call it with parameters 'self'
dad.override()

## from son get the 'override' function and call it with parameters 'self'
son.override()


## from dad get the 'altered' function and call it with parameters 'self'
dad.altered()

## from son get the 'altered' function and call it with parameters 'self'
son.altered()
