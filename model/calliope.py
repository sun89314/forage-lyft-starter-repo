
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine


class Calliope:
    def __init__(self, engine,battery):
        self.engine = engine
        self.battery = battery

    def need_service(self):
        return self.engine.need_service() or self.battery.need_service()


if __name__ == '__main__':
    e = CapuletEngine("2022-01-01", 30010, 0)
    e2 = WilloughbyEngine("2022-01-01",20000,1)
    # print(e.need_service())
    car = Calliope(e2)
    print(car.need_service());

