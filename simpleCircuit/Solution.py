from Circuit import Circuit as Circuit

class Solution:
    def __init__(self,circuit:Circuit):
        self.circuit = circuit

    def do_power_flow(self):
        v_source = self.circuit.vsource
        series_resistor = list(self.circuit.resistors.values())[0]
        load_resistor = list(self.circuit.loads.values())[0]

        r_total = series_resistor.r + (1/load_resistor.g)

        self.circuit.i = v_source.v/r_total

        bus_a = self.circuit.buses[v_source.bus1]
        bus_a.set_bus_voltage(v_source.v)
        bus_b = self.circuit.buses[list(self.circuit.buses.keys())[1]]
        bus_b.set_bus_voltage(bus_a.voltage - self.circuit.i * series_resistor.r)

        self.circuit.print_nodal_voltage()
        self.circuit.print_circuit_current()


