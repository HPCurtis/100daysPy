# Unlimited positional arguements.
# Using *args to add any number of arguements to function
# of note this is processed byu python as tuple.
def add(*args):
    res = 0
    for i in args:
        res += i
    return(res)

print(add(2, 2, 2))


# Key word arguements
# Pytohn processes as the dictionary data structure (type).
class Car:
    def __init__(self, **kw):

        # kw is dictionary and the use of the .get method avoids the error if not presently provided.
        self. model = kw.get('model')
        self.make = kw.get('make')

my_car = Car(make = "Volkswagen", model = "Up")
print(my_car.make)