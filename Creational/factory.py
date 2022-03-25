from abc import abstractmethod, ABC


class Factory(ABC):

    @abstractmethod
    def create(self, **kwargs):
        pass


class AbstractFactory(Factory, ABC):

    def __init__(self):
        self._factories = dict()

    @abstractmethod
    def create(self, **kwargs):
        pass

    def _register(self, key: str, factory: Factory):
        self._factories[key] = factory
