from Battery.BatteryInterface import BatteryInterface
from datetime import datetime

class NubbinBattery(BatteryInterface):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def need_service(self):
        last_service_date = datetime.strptime(self.last_service_date, '%Y-%m-%d').date()
        today =  datetime.today().strftime('%Y-%m-%d')
        today = datetime.strptime(today, '%Y-%m-%d').date()
        diff = (today - last_service_date).days
        if diff > 1000:
            return True
        else:
            return False


if __name__ == '__main__':
    e = NubbinBattery("2023-06-13")
    print(e.need_service())

