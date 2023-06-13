from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
    @abstractmethod
    def need_service(self):
        pass
