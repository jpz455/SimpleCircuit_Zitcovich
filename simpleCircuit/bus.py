class Bus:

    def __init__(self, name: str):
        self.name = name
        self.voltage = None

    def set_bus_voltage(self, bus_v: float):
        self.voltage = bus_v
