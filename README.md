# SimpleCircuit_Zitcovich

PROJECT OVERVIEW
 
 This repository consists of a simple circuit power flow simulator. The user provides various component attributes that allow the program to follow through with a power flow analysis. The output of this program offers nodal voltages and current running through the circuit. The purpose of this program is to simulate a simple circuit consisting of a voltage source, a resistor, and a load. The user can provide voltages for both the voltage source and the load nominal voltage, as well as the load real power (in watts) and the resistance of the serial resistor (in ohms). 

KEY FEATURES

-- User-defined voltage source, resistor, load, and busses
-- DC- power flow solution provided
   -- Calculated nodal voltages incorporating dynamic voltage source
   -- Calculated current flowing through the circuit

PROBLEM/REAL-WORLD APPLICATION
Specifically, the program solves a simple DC circuit. The user can define the value of the voltage source for the circuit. Following that, the user can specify a series resistor that connects the voltage source to a load. Next, the user defines a load that connects to ground, which terminates the circuit. The user can define the real power and voltage of the load. Finally, the user can insert and define buses to calculate the nodal voltages at those buses. With this information, a solution class can solve the power flow to calculate the nodal voltages and current throughout the circuit. 
This circuit can be applied to multiple real-world scenarios. This program can model the power flow in any event where a voltage source and a load are apparent. For example, this can be as simple as an LED being powered through a bench-top power supply, a current-limiting resistor, and then the LED. 
