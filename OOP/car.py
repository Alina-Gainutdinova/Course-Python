class Car:
    def __init__(self, brand, model, fuel: int) -> None:
        self.brand = brand
        self.model = model
        self.fuel = fuel

    def start(self):
        print('Машина на старте')

    def drive(self, volume):
        if volume < 0:
            print('Объем топлива не может быть отрицательным')
            return
        self.fuel -= volume

    def show_volume_fuel(self):
        print(f'Объем топлива: {self.fuel} литров')


car_1 = Car('Mercedes', 'W123', 3000)
car_1.show_volume_fuel()
car_1.drive(20)
car_1.show_volume_fuel()
car_1.drive(-10)
car_1.show_volume_fuel()
