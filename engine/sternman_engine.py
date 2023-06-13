from abc import ABC
from engine.EngineInterface import EngineInterface


class SternmanEngine(EngineInterface):
    def __init__(self, last_service_date, warning_light_is_on):
        self.last_service_date = last_service_date
        self.warning_light_is_on = warning_light_is_on

    def need_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False

if __name__ == '__main__':
    e = SternmanEngine("2022-01-01", True)
    print(e.need_service())