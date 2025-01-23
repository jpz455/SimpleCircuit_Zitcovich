# Circuit Power Flow Simulator

## Project Overview

This project contains a simple circuit power flow simulator designed to analyze a DC circuit. Users can define attributes for various components, including a voltage source, a resistor, and a load. The program computes the nodal voltages and currents in the circuit using user-provided input parameters. The goal of this simulator is to model a basic electrical circuit and calculate the following:
- Nodal voltages at specified buses
- Current flow through the circuit components

## How It Works

1. The user defines input parameters for:
   - Voltage source
   - Series resistor
   - Load (real power and nominal voltage)
   - Additional buses for nodal voltage calculation
2. The program calculates:
   - Nodal voltages at each bus
   - Current flow throughout the circuit
3. The output provides insights into the circuit's behavior, helping users analyze power flow.

## Classes and Methods

### Bus Class

**Attributes**:
- `name`: (str) The name of the bus.
- `voltage`: (float) The voltage at the bus.

**Methods**:
- `__init__(self, name: str)`: Initializes a bus with the specified name.
- `set_bus_voltage(self, bus_v: float)`: Sets the voltage for the bus.

---

### Resistor Class

**Attributes**:
- `name`: (str) The name of the resistor.
- `bus1`: (str) The name of the first bus the resistor is connected to.
- `bus2`: (str) The name of the second bus the resistor is connected to.
- `r`: (float) The resistance of the resistor (in ohms).
- `g`: (float) The conductance of the resistor, calculated as 1 / r.

**Methods**:
- `__init__(self, name: str, bus1: str, bus2: str, r: float)`: Initializes the resistor with its name, buses, and resistance.
- `calc_g(self)`: Calculates the conductance from the resistance.

---

### Load Class

**Attributes**:
- `name`: (str) The name of the load.
- `bus1`: (str) The bus to which the load is connected.
- `p`: (float) The active power of the load (in watts).
- `v`: (float) The voltage at the load (in volts).
- `g`: (float) The conductance of the load, calculated as p / v^2.

**Methods**:
- `__init__(self, name: str, bus1: str, p: float, v: float)`: Initializes the load with its name, bus, power, and voltage.
- `calc_g(self)`: Calculates the conductance of the load.

---

### VSource Class

**Attributes**:
- `name`: (str) The name of the voltage source.
- `bus1`: (str) The bus to which the voltage source is connected.
- `v`: (float) The voltage of the source (in volts).

**Methods**:
- `__init__(self, name: str, bus1: str, v: float)`: Initializes the voltage source with its name, bus, and voltage.

---

### Circuit Class

**Attributes**:
- `name`: (str) The name of the circuit.
- `buses`: (dict) A dictionary storing buses, where keys are bus names and values are Bus objects.
- `resistors`: (dict) A dictionary storing resistors, where keys are resistor names and values are Resistor objects.
- `loads`: (dict) A dictionary storing loads, where keys are load names and values are Load objects.
- `vsource`: (VSource) The voltage source object in the circuit.
- `i`: (float) The current in the circuit.

**Methods**:
- `__init__(self, name: str)`: Initializes the circuit with the given name and empty component dictionaries.
- `add_bus(self, bus: Bus)`: Adds a bus to the circuit.
- `add_resistor_element(self, name: str, bus1: str, bus2: str, r: float)`: Adds a resistor element to the circuit.
- `add_load_element(self, name: str, bus1: str, p: float, v: float)`: Adds a load element to the circuit.
- `add_vsource_element(self, name: str, bus1: str, v: float)`: Adds a voltage source to the circuit and sets the voltage of the bus.
- `set_i(self, i: float)`: Sets the current in the circuit.
- `print_nodal_voltage(self)`: Prints the voltage at each bus in the circuit.
- `print_circuit_current(self)`: Prints the current in the circuit.

---

### Solution Class

**Attributes**:
- `circuit`: (Circuit) The circuit object to solve for.

**Methods**:
- `__init__(self, circuit: Circuit)`: Initializes the solution with the provided circuit.
- `do_power_flow(self)`: Solves for the power flow in the circuit. It calculates the total resistance, current, and nodal voltages.

## Problem Statement / Real-World Application

This program simulates a simple DC circuit with the following configuration:
1. **Voltage Source**: Supplies power to the circuit.
2. **Series Resistor**: Limits the current flowing through the circuit.
3. **Load**: Consumes power and is connected to ground, terminating the circuit.

### Applications
This circuit can represent numerous real-world scenarios, such as:
- An LED powered by a bench-top power supply with a current-limiting resistor.
- Any basic circuit requiring a voltage source, a resistor, and a load.

---

## Relevant Equations

1. **Ohm's Law**:  
   `V (volts) = I (amps) * R (ohms)`

2. **Power Equation**:  
   `P (watts) = I (amps) * V (volts)`

3. **Conductance (from resistance)**:  
   `G (siemens) = 1 / R (ohms)`

4. **Conductance (from power and voltage)**:  
   `G (siemens) = V^2 (volts) / P (watts)`

5. **DC Power Flow – Kirchhoff's Voltage Law (KVL) Loop**:  
   `I = V_source / (R_series + R_load)`

   - `I`: Total current flowing through the circuit
   - `V_A = V_source`: Voltage source is connected to Bus A
   - `V_B = I * R_load`: Load is connected to Bus B
  
 ---  

## Example Case

### Problem Definition

The user can define the voltage source value, resistance, load voltage, load real power, and define the buses accordingly. The program calculates the current running through this circuit as well as the voltages at bus A and bus B.

### How the Solution Works:

1. **Calculate the total resistance**:
   Given the series resistance and calculated conductance of the load, the total resistance of the circuit can be calculated and stored.
   
2. **Calculate the circuit current**:
   Given the user-defined voltage source and total resistance, the total current can be calculated using the relevant equation provided previously.
   
3. **Determine and calculate the bus voltage**:
   - **Bus A**: User-defined due to the adjacency to the voltage source.
   - **Bus B**: Calculated by the difference between bus A and the calculated voltage using the total circuit current and the load resistance.

### Specific Case:
- **Vsource** = 200 V
- **Resistor1** = 25 ohms
- **Load**: Power = 1500 W; Voltage = 400 V

#### Calculate Total Resistance:

1. **Calculate Total Resistance**:  
   `R_TOT = 25 ohms + (400^2 / 1500) = 131.67 ohms`

2. **Calculate Circuit Current**:  
   `I = 200 V / 131.67 ohms = 1.5189 A`

#### Determine and Calculate Bus Voltage:
- **Bus A** = 200 V
- **Bus B** = 200 - (1.5189 × 25) = 200 - 37.9725 = 162.025 V

