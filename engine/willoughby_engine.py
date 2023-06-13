from abc import ABC
from engine.EngineInterface import EngineInterface


class WilloughbyEngine(EngineInterface):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def need_service(self):
        return self.current_mileage - self.last_service_mileage > 60000
