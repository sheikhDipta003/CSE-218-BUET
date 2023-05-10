class Car():

    machine = "Vehicle" #class object attribute

    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price
    
    def drive(self, serial_number):
        print(f"Driving the {self.brand} car with serial no. {serial_number}")

new_car = Car(brand="Volvo", color="Red", price="1000.0")
print("price = ", new_car.price)
print(f"new_car is a {Car.machine}")
new_car.drive(805)



class BMI():
    divider = 100   #to convert height in cm to height in meter

    def __init__(self,weight_kg=70,height_cm=180):
        self.weight_kg = weight_kg
        self.height_cm = height_cm
        self.example = 2    #attributes don't have to be created with the parameters
    
    #calculate BMI
    def calculate_bmi(self):
        return self.weight_kg / (self.height_cm / BMI.divider)**2

my_bmi = BMI()
print("My height: ", my_bmi.height_cm, "cm")
print("My weight: ", my_bmi.weight_kg, "kg")
print("example = ", my_bmi.example)
print("My BMI: ",my_bmi.calculate_bmi())


