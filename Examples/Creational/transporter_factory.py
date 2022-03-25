from Creational.factory import Factory
from Examples.Concrete.transporter import Car, Sedan, Truck, Ship, CargoShip, Yacht, NotSupportedTransporter, \
    Transporter


class TransporterFactory(Factory):

    def create(self, transporter_type: str) -> Transporter:
        pass


class CarFactory(TransporterFactory):

    def create(self, car_type: str) -> Car:
        if car_type == 'Sedan':
            return Sedan()
        if car_type == 'Truck':
            return Truck()
        raise NotSupportedTransporter()


class ShipFactory(TransporterFactory):

    def create(self, ship_type: str) -> Ship:
        if ship_type == 'CargoShip':
            return CargoShip()
        if ship_type == 'Yacht':
            return Yacht()
        raise NotSupportedTransporter()
