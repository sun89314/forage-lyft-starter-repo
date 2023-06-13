import abc


class BatteryInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def need_service(self):
        pass