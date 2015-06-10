# List
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

# 'stuff' is a new list with items from 'ten_things' each now in single-quotes
stuff = ten_things.split(' ')
# 'more_stuff' is a list with each item in double-quotes
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# while the length of list 'stuff' does not equal 10
while len(stuff) != 10:
    # 'next_one' equals each individual item in 'more_stuff'
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    # adds 'next_one' item to 'stuff'
    stuff.append(next_one)
    # prints the number of items using the length of 'stuff' list
    print "There's %d items now." % len(stuff)
print more_stuff
