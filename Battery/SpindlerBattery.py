from Battery.BatteryInterface import BatteryInterface
from datetime import datetime

class SpindlerBattery(BatteryInterface):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def need_service(self):
        last_service_date = datetime.strptime(self.last_service_date, '%Y-%m-%d').date()
        today = datetime.today().strftime('%Y-%m-%d')
        today = datetime.strptime(today, '%Y-%m-%d').date()
        diff = (today - last_service_date).days
        if diff > 300:
            return True
        else:
            return False

