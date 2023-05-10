class Machine():

    def __init__(self):
        print("Machine started!")

    def machine_type(self):
        print("Machine type is vehicle.")

    def drive(self):
        print("Driving a machine.")

# machine1 = Machine()
# machine1.machine_type()
# machine1.drive()


#Truck class inherits Machine class
class Truck(Machine):

    def __init__(self):
        Machine.__init__(self)  #calling Machine class's __init__()
        print("This is a truck.")
    
    def drive(self):    #base class's methods can be overridden
        print("Driving a truck.")
    
    def load(self):     #new methods can be introduced as well
        print("Loading the truck.")

# truck1 = Truck()
# truck1.machine_type()
# truck1.drive()
# truck1.load()


class Car():

    def __init__(self, brand):
        self.brand = brand
    
    def drive(self):
        return 'I drive a ' + self.brand + ' car'

class Bus():

    def __init__(self, brand):
        self.brand = brand
    
    def drive(self):
        return 'I drive a ' + self.brand + ' bus'

volvo = Car('volvo')
ford = Bus('Ford')

# print(ford.drive())
# print(volvo.drive())

# for vehicle in [volvo, ford]:
#     print(type(vehicle))
#     print(vehicle.drive())  #This is an example of polymorphism. Though both volvo and ford share methods with a common name, different versions of that method is executed depending on the class that object belongs to.

#Another example of polymorphism
def vehicle_drive(vehicle):
    print(vehicle.drive())

# vehicle_drive(volvo)
# vehicle_drive(ford)

#abstract class
class Machine2():

    def __init__(self, brand):
        self.brand = brand
    
    # this class is an abstract class because its method is incomplete and it is expected to be implemented in a subclass; so if we want to use this method using an object of this class, python will raise an error
    def drive(self):
        raise NotImplementedError('Implement this method in a subclass.')

machine2 = Machine2(brand='volvo')
#machine2.drive()

class Car2(Machine2):

    # no need to write __init__()
    def drive(self):
        print('I drive a ' + self.brand + ' car')

class Truck2(Machine2):

    # no need to write __init__()
    def drive(self):
        print('I drive a ' + self.brand + ' truck')

daimler = Car2(brand='Daimler')
chevrolet = Truck2(brand='Chevrolet')
daimler.drive()
chevrolet.drive()
