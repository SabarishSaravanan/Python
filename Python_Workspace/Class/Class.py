class Car:
    def __init__(self, make, model, year):
        # Attributes
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    # Method
    def accelerate(self, increment):
        self.speed += increment
        print(f"The car accelerates to {self.speed} mph.")

    # Method
    def brake(self, decrement):
        self.speed -= decrement
        print(f"The car slows down to {self.speed} mph.")

# Create an object (instance) of the Car class

my_car = Car(make="Toyota", model="Camry", year=2022)
# Access attributes
print(f"My car is a {my_car.year} {my_car.make} {my_car.model}.")

# Call methods
my_car.accelerate(20)  # The car accelerates to 20 mph.
my_car.brake(5)        # The car slows down to 15 mph.
