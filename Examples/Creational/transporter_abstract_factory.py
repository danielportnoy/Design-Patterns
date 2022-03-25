from Creational.factory import AbstractFactory
from Examples.Creational.transporter_factory import ShipFactory, CarFactory


class TransporterAbstractFactory(AbstractFactory):

    def __init__(self):
        super().__init__()
        self._register('car_factory', CarFactory())
        self._register('ship_factory', ShipFactory())

    def create(self, instance_type):
        if instance_type == 'Sedan' or instance_type == 'Truck':
            return self._factories['car_factory'].create(instance_type)
        if instance_type == 'CargoShip' or instance_type == 'Yacht':
            return self._factories['ship_factory'].create(instance_type)

        raise NotSupportedInstance()


class NotSupportedInstance(Exception):
    pass
