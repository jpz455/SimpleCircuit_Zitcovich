from bus import bus
from resistor import resistor
from load import load
from vSource import vSource

# Create Bus object
bus1 = bus(name="Bus1", voltage=1.0)
print(f"Bus Created: Name={bus1.name}, Voltage={bus1.voltage}, Is Voltage Source={bus1.is_voltage_source}")

bus1.set_bus_voltage(bus_v=1.05, is_voltage_source=False)
print(f"Updated During Power Flow: Voltage={bus1.voltage}, Is Voltage Source={bus1.is_voltage_source}")

vsource1 = vSource(name="V1", bus1="Bus1", v=1.1)
print(f"Voltage Source Created: Name={vsource1.name}, Voltage={vsource1.v}")

bus1.set_bus_voltage(bus_v=vsource1.v, is_voltage_source=True)
print(f"Bus Voltage Updated by Voltage Source: Voltage={bus1.voltage}, Is Voltage Source={bus1.is_voltage_source}")

resistor1 = resistor(name="R1", bus1="Bus1", bus2="Bus2", r=10.0)
print(f"Resistor Created: Name={resistor1.name}, R={resistor1.r}")

resistor1.calc_g()
print(f"Resistor Conductance: G={resistor1.g}")

load1 = load(name="Load1", bus1="Bus1", p=100, q=50)
print(f"Load Created: Name={load1.name}, P={load1.p}, Q={load1.q}")

load1.calc_g()
print(f"Load Conductance: G={load1.g}")
