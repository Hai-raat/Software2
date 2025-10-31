import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.traveled_distance = 0

    def acceleration(self, change_speed):
            self.current_speed += change_speed
            if self.current_speed > self.maximum_speed:
                self.current_speed = self.maximum_speed
            elif self.current_speed < 0:
                self.current_speed = 0

    def drive(self, hours_spent):
        self.traveled_distance += self.current_speed * hours_spent

    def __str__(self):
        return (f"{self.registration_number:8} | {self.maximum_speed:14} | {self.current_speed:15} | {self.traveled_distance:18.1f}")

car1 = Car("ABC-123", 142)
print("Registration | Maximum Speed(km/h) | Current Speed | Traveled Distance(km)")
print("." * 75)
print(car1)

car1.acceleration(30)
car1.acceleration(70)
car1.acceleration(50)
print(f"Current speed after acceleration: {car1.current_speed:.1f} km/h")

car1.acceleration(-200)
print(f"Final speed after the emergency brake: {car1.current_speed:.1f} km/h")

car1.current_speed = 60
car1.traveled_distance = 2000
car1.drive(1.5)
print(f"Traveled distance after 1 and half hours: {car1.traveled_distance:.1f} km")

cars = []
for i in range(1, 11):
    registration_number = f"ABC-{i}"
    maximum_speed = random.randint(100, 200)
    cars.append(Car(registration_number, maximum_speed))

race_ongoing = True
hours_spent = 0

while race_ongoing:
    hours_spent += 1
    for car in cars:
        change_speed = random.randint(-10, 15)
        car.acceleration(change_speed)
        car.drive(1)

        if car.traveled_distance > 10000:
            race_ongoing = False


print("Race completed! Results after", hours_spent, "hours.")
print("Registration | Maximum Speed (km/h) | Current Speed | Traveled Distance(km)")
print("." * 75)
for car in cars:
    print(car)