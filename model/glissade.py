from datetime import datetime
from Battery.SpindlerBattery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine


class Glissade(Car):
    def __int__(self,engine,battery):
        super().__int__(engine,battery)
    def need_service(self):
        return self.engine.need_service() or self.battery.need_service()


if __name__ == '__main__':
    engine = CapuletEngine("2022-01-01",100000, 50000)
    battery = SpindlerBattery("2023-01-01")
    car = Glissade(engine,battery)
    print(car.need_service())
