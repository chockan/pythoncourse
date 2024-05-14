
#single inheritance


# class Vehicle:
#     def Vehicle_info(self):
#         print('Inside Vehicle class')

# # Derived class
# class Car(Vehicle):
#     def car_info(self):
#         print('Inside Car class')

# # Create object of Car
# c = Car()

# # access Vehicle's info using car object
# c.Vehicle_info()
# c.car_info()




# Example 1: Multiple Inheritance

# # Base class 1
# class Person:
#     def person_info(self, name, age):
#         print('Inside Person class')
#         print('Name:', name, 'Age:', age)

# # Base class 2
# class Company:
#     def company_info(self, company_name, location):
#         print('Inside Company class')
#         print('Name:', company_name, 'location:', location)

# # Derived class
# class Employee(Person, Company):
#     def Employee_info(self, salary, skill):
#         print('Inside Employee class')
#         print('Salary:', salary, 'Skill:', skill)

# # Create object of Employee
# emp = Employee()

# # access data
# emp.person_info('Milaan', 33)
# emp.company_info('Google', 'Atlanta')
# emp.Employee_info(19000, 'Machine Learning')


#Multilevel inheritance
# Base class
# class Vehicle:
#     def Vehicle_info(self):
#         print('Inside Vehicle class')

# # Child class
# class Car(Vehicle):
#     def car_info(self):
#         print('Inside Car class')

# # Child class
# class SportsCar(Car):
#     def sports_car_info(self):
#         print('Inside SportsCar class')

# # Create object of SportsCar
# s_car = SportsCar()

# # access Vehicle's and Car info using SportsCar object
# s_car.Vehicle_info()
# s_car.car_info()
# s_car.sports_car_info()


#hiearachical inheritance
# Example 1:

# class Vehicle:
#     def info(self):
#         print("This is Vehicle")

# class Car(Vehicle):
#     def car_info(self, name):
#         print("Car name is:", name)

# class Truck(Vehicle):
#     def truck_info(self, name):
#         print("Truck name is:", name)

# obj1 = Car()
# obj1.info()
# obj1.car_info('BMW')

# obj2 = Truck()
# obj2.info()
# obj2.truck_info('Ford')

#hybrid inheritance
# Example 1:

# class Vehicle:
#     def vehicle_info(self):
#         print("Inside Vehicle class")

# class Car(Vehicle):
#     def car_info(self):
#         print("Inside Car class")

# class Truck(Vehicle):
#     def truck_info(self):
#         print("Inside Truck class")

# # Sports Car can inherits properties of Vehicle and Car
# class SportsCar(Car, Vehicle):
#     def sports_car_info(self):
#         print("Inside SportsCar class")

# # create object
# s_car = SportsCar()

# s_car.vehicle_info()
# s_car.car_info()
# s_car.sports_car_info()


#super keyword
class Animal:
    def __init__(self, Animal):
        print(Animal, 'is an animal.');

class Mammal(Animal):  # Mammal derived to Animal
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
        super().__init__(mammalName)
    
class NonWingedMammal(Mammal):  # NonWingedMammal derived from Mammal (derived from Animal)
    def __init__(self, NonWingedMammal):
        print(NonWingedMammal, "can't fly.")
        super().__init__(NonWingedMammal)

class NonMarineMammal(Mammal):  # NonMarineMammal derived from Mammal (derived from Animal)
    def __init__(self, NonMarineMammal):
        print(NonMarineMammal, "can't swim.")
        super().__init__(NonMarineMammal)

class Dog(NonMarineMammal, NonWingedMammal):  # Dog derived from NonMarineMammal and NonWingedMammal
    def __init__(self):
        print('Dog has 4 legs.');
        super().__init__('Dog')
    
d = Dog()
print('')
bat = NonMarineMammal('Bat')




