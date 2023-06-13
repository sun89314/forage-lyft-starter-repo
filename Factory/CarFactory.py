from Battery.NubbinBattery import NubbinBattery
from Battery.SpindlerBattery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from model.glissade import Glissade
from model.calliope import Calliope

class CarFactory:
    def buildGlissade(self,last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        car = Glissade(engine, battery)
        return car

    def buildCalliope(self,last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        car = Calliope(engine,battery)
        return car
