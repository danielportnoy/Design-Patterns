from abc import ABC, abstractmethod


class Transporter(ABC):

    @abstractmethod
    def transport(self, item: str):
        pass


class Car(Transporter, ABC):

    @abstractmethod
    def drive(self):
        pass


class Sedan(Car):

    def transport(self, item: str):
        print(f'Transported {item} by Sedan')

    def drive(self):
        print(f'Sedan driving')


class Truck(Car):

    def transport(self, item: str):
        print(f'Transported {item} by Truck')

    def drive(self):
        print(f'Truck driving')


class Ship(Transporter, ABC):

    @abstractmethod
    def sail(self):
        pass


class CargoShip(Ship):

    def transport(self, item: str):
        print(f'Transported {item} by cargo ship')

    def sail(self):
        print(f'CargoShip sailing')


class Yacht(Ship):

    def transport(self, item: str):
        print(f'Transported {item} by yacht')

    def sail(self):
        print(f'Yacht sailing')


class NotSupportedTransporter(Exception):
    pass
