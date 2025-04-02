class Vehicle:
    def move(self):
        pass
class Car(Vehicle):
    def move(self):
        print("Driving")
class Boat(Vehicle):
    def move(self):
        print("Sailing")
class Plane(Vehicle):
    def move(self):
        print("Flying ")
for obj in [Car(), Boat(), Plane()]:
    obj.move()

