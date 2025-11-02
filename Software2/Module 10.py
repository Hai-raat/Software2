import random

class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
        print(f"Elevator is now at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
        print(f"Elevator is now at floor {self.current_floor}")

    def go_to_floor(self, destination):
        print(f"\nMoving elevator to floor {destination}")
        while self.current_floor < destination:
            self.floor_up()
        while self.current_floor > destination:
            self.floor_down()
        print(f"Elevator reached floor {self.current_floor}")


class Building:
    def __init__(self, bottom, top, number_of_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = [Elevator(bottom, top) for _ in range(number_of_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        print(f"\nRunning elevator {elevator_number} to floor {destination_floor}")
        self.elevators[elevator_number].go_to_floor(destination_floor)


    def fire_alarm(self):
        print("\n  FIRE ALARM! All elevators returning to the bottom floor.")
        for i, elevator in enumerate(self.elevators):
            print(f"Returning Elevator {i} to floor {self.bottom}")
            elevator.go_to_floor(self.bottom)



class Car:
    def __init__(self, name):
        self.name = name
        self.speed = 0
        self.distance = 0

    def drive(self):
        self.distance += self.speed

    def accelerate(self):
        change = random.randint(-10, 15)
        self.speed += change
        if self.speed < 0:
            self.speed = 0


class Race:
    def __init__(self, name, kilometers, cars):
        self.name = name
        self.kilometers = kilometers
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate()
            car.drive()

    def print_status(self):
        print(f"\nRace Status: {self.name}")
        print(f"{'Car':<15}{'Speed (km/h)':<15}{'Distance (km)':<15}")
        for car in self.cars:
            print(f"{car.name:<15}{car.speed:<15}{car.distance:<15}")
        print("-" * 40)

    def race_finished(self):
        return any(car.distance >= self.kilometers for car in self.cars)



if __name__ == "__main__":

    print(" ( Elevator and Building Simulation ) ")
    b1 = Building(1, 10, 3)
    b1.run_elevator(0, 5)
    b1.run_elevator(1, 8)
    b1.fire_alarm()

    print("\n ( Race Simulation )")
    cars = [Car(f"Car {i+1}") for i in range(10)]
    race = Race("Grand Demolition Derby", 8000, cars)

    hours = 0
    while not race.race_finished():
        race.hour_passes()
        hours += 1
        if hours % 10 == 0:
            race.print_status()

    print("\n Race Finished!")
    race.print_status()