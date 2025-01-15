class bus:
    numBus = 0
    def __init__(self, name: str, voltage: float = 0.0):
        self.name = name
        self.voltage = voltage  # Initial voltage
        self.is_voltage_source = False  # Flag to check if a voltage source is connected
        bus.numBus += 1

    def set_bus_voltage(self, bus_v: float, is_voltage_source: bool = False):
        self.voltage = bus_v
        self.is_voltage_source = is_voltage_source