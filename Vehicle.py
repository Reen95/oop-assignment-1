# vehicles.py

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement move()")

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

# Example usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())
