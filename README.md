# Quantum-Emulator by @awendesbois

This project is a quantum emulator. It has to emulate a quantum circuit using usual gates.  

## Overview

This project is seprarate in 2 parts:

1- The "System.py" file:
This file contain the class System which contain all the following gates:
        H
        X  |  CX
        Y  |  CY
        Z  |  CZ

2- The "tests.txt" file:
This file contain a simple circuit to create a GHZ State: 
        1/sqrt(2)(|000> + |111>)

## Usage
1- The circuit guiven has to be writen in a .txt file in that form:
        "qubits n
        gate_1 qubit_1
        gate_2 qubit_1
        ... ...
        gate_m qubit_n"

2- You have to run the following command: 
        py main.py "your filename"

3- You can test a simple circuit (GHZ State)

## Output
The output is the amplitude & phase of each state of the circuit.

Example : "State: |000> - Amplitude: [0.+0.j] - Phase: [0.]"