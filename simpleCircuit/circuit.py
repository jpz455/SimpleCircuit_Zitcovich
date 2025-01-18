from Bus import Bus as Bus
from Resistor import Resistor as Resistor
from Load import Load as Load
from VSource import VSource as VSource

from typing import Dict

class Circuit:
    def __init__(self,name:str):
        self.name = name
        self.buses: Dict[str,Bus] = {}
        self.resistors: Dict[str,Resistor] = {}
        self.loads: Dict[str,Load] = {}
        self.vsource: VSource = None
        self.i:float = 0.0

    def add_bus(self,bus:Bus):
        self.buses[bus.name] = bus

    def add_resistor_element(self,name:str,bus1:str,bus2:str,r:float):
        self.resistors[name] = Resistor(name,bus1,bus2,r)

    def add_load_element(self,name:str,bus1:str,p:float,v:float):
        self.loads[name] = Load(name, bus1, p, v)

    def add_vsource_element(self,name:str,bus1:str,v:float):
        self.vsource = VSource(name, bus1, v)
        self.buses[bus1].set_bus_voltage(v)

    def set_i(self,i:float):
        self.i=i

    def print_nodal_voltage(self):
        print("Nodal Voltages:")
        for bus_name, bus in self.buses.items():
            print(f"Bus {bus_name}: Voltage = {bus.voltage} V")

    def print_circuit_current(self):
        print(f"Circuit Current: I = {self.i} A")







