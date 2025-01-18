from Circuit import Circuit
from Bus import Bus
from Solution import Solution
from Resistor import Resistor
from Load import Load
from VSource import VSource


my_circuit = Circuit("Test Circuit")

# Add buses
bus_a = Bus("BusA")
bus_b = Bus("BusB")
my_circuit.add_bus(bus_a)
my_circuit.add_bus(bus_b)

v_source = VSource("VSource1","BusA",100)
my_circuit.add_vsource_element(v_source.name,v_source.bus1,v_source.v)

resistor_ab = Resistor("Rab","BusA","BusB",5)
my_circuit.add_resistor_element(resistor_ab.name,resistor_ab.bus1,resistor_ab.bus2,resistor_ab.r)

load_b = Load("Lb","BusB",2000,100)
my_circuit.add_load_element(load_b.name,load_b.bus1,load_b.p,load_b.v)

solution = Solution(my_circuit)
solution.do_power_flow()


