import abc


class EngineInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def need_service(self):
        pass
