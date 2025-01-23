from Circuit import Circuit as Circuit

class Solution:
    def __init__(self,circuit:Circuit):
        self.circuit = circuit

    def do_power_flow(self):
       #assign vsource element
        v_source = self.circuit.vsource

       #get resistance of total circuit by accessing first element of resistor and load dictionaries
        series_resistor = list(self.circuit.resistors.values())[0]
        load_resistor = list(self.circuit.loads.values())[0]
        r_total = series_resistor.r + (1/load_resistor.g)

       #calculate circuit current
        self.circuit.i = v_source.v/r_total

       #set nodal voltages
       #bus a is connected to source voltage
        bus_a = self.circuit.buses[v_source.bus1]
        bus_a.set_bus_voltage(v_source.v)

       #access bus b
        bus_b = self.circuit.buses[list(self.circuit.buses.keys())[1]]

       #solve for b using voltage drop across series resistor
        bus_b.set_bus_voltage(bus_a.voltage - self.circuit.i * series_resistor.r)



