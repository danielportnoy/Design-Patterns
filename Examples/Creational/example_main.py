from Examples.Creational.transporter_abstract_factory import TransporterAbstractFactory


def main():
    transporter_factory = TransporterAbstractFactory()
    item = 'item'
    sedan_obj = transporter_factory.create("Sedan")

    sedan_obj.transport(item)
    sedan_obj.drive()

    yacht_obj = transporter_factory.create("Yacht")

    yacht_obj.transport(item)
    yacht_obj.sail()


if __name__ == '__main__':
    main()
