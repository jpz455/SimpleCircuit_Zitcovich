# **SimpleCircuit_Zitcovich**

## **Project Overview**
This repository contains a **simple circuit power flow simulator** designed to analyze a DC circuit. Users can define attributes for various components, including a voltage source, a resistor, and a load. The program computes the nodal voltages and currents in the circuit using user-provided input parameters.

The goal of this simulator is to model a basic electrical circuit and calculate the following:  
- **Nodal voltages** at specified buses  
- **Current flow** through the circuit components  

The simulator supports real-world scenarios such as evaluating power flow for simple setups like powering an LED with a power supply and a current-limiting resistor.

---

## **Key Features**
- **User-defined components**:
  - Voltage source
  - Resistor
  - Load (real power and nominal voltage)
  - Buses for nodal voltage calculation
- **DC power flow analysis**:
  - Dynamic calculation of nodal voltages
  - Current flow computation through the circuit

---

## **Problem Statement / Real-World Application**
This program simulates a simple DC circuit with the following configuration:  
1. **Voltage Source**: Supplies power to the circuit.  
2. **Series Resistor**: Limits the current flowing through the circuit.  
3. **Load**: Consumes power and is connected to ground, terminating the circuit.  

Users can define:  
- The voltage of the source  
- The resistance of the series resistor  
- The real power and nominal voltage of the load  

The simulator then calculates the **power flow**, including nodal voltages at user-defined buses and the current flowing through the circuit.  

### **Applications**
This circuit can represent numerous real-world scenarios, such as:  
- An LED powered by a bench-top power supply with a current-limiting resistor  
- Any basic circuit requiring a voltage source, a resistor, and a load  

---

## **Equations Used**
The program relies on fundamental electrical engineering principles:

1. **Ohm's Law**:  
   V = I × R  

2. **Power Equation**:  
   P = I × V  

3. **Conductance (from resistance)**:  
   G = 1 / R  

4. **Conductance (from power and voltage)**:  
   G = V² / P  

5. **DC Power Flow – Kirchhoff's Voltage Law (KVL) Loop**:  
   I = V_source / (R_series + R_load)  

   - **I**: Total current flowing through the circuit  
   - **V_a = V_s**: Voltage source is connected to Bus A  
   - **V_b = I × R_load**: Load is connected to Bus B  

---

## **How It Works**
1. The user defines input parameters for:  
   - Voltage source  
   - Series resistor  
   - Load (real power and nominal voltage)  
   - Additional buses for nodal voltage calculation  

2. The program calculates:  
   - **Nodal voltages** at each bus  
   - **Current flow** throughout the circuit  

3. The output provides insights into the circuit's behavior, helping users analyze power flow.

---

## **Future Enhancements**
- Support for AC circuit power flow analysis  
- Multi-load configurations with parallel or series connections  
- Integration of reactive components (inductors and capacitors)  
- Visualization tools for circuit diagrams and voltage/current graphs  

---
