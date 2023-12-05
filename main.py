import sys 
import os
from System import *
import matplotlib.pyplot as plt
import numpy as np

def verif(qubits, Syst):
    for q in qubits:
        if 0 > q or q >= Syst.n:
            raise Exception((f"ERROR! -> Invalid qubit index: {q}"))
        
def analyse_line(word, Syst):  
    basic_Gates = ['X', 'Y', 'Z', 'H']
    controled_Gates = ['CX', 'CY', 'CZ']
    
    if word[0] == "qubits":
        Syst.__init__(int(word[1]))
        print(f"{Syst.n} qubits initialized")
        
    elif word[0] == "R":
        qubit = int(word[1])
        angle = eval(word[2])
        verif([qubit], Syst)
        Syst.execute_rphase(qubit, angle)
        
        
    elif word[0] in basic_Gates:
        qubit = int(word[1])
        verif([qubit], Syst)
        match basic_Gates.index(word[0]):
            case 0: Syst.execute_x(qubit)
            case 1: Syst.execute_y(qubit)
            case 2: Syst.execute_z(qubit)
            case 3: Syst.execute_h(qubit)
            
    elif word[0] in controled_Gates:
        controls = [int(i) for i in word[1:-1]]
        target = int(word[-1])
        verif(controls + [target], Syst)
        match controled_Gates.index(word[0]):
            case 0: Syst.execute_ncx(controls, target)
            case 1: Syst.execute_ncy(controls, target)
            case 2: Syst.execute_ncz(controls, target)

    else:
        print(f"ERROR! -> Unknown command: {word[0]}")


def main(filename):
    Syst = System(0)
    
    with open(filename, 'r') as file:
        lines = file.readlines()

        for l in lines:
            word = l.strip().split()                
            analyse_line(word, Syst)
        
            Syst.printSyst()
            
    number_of_shots=1000
    mesures = Syst.measure(number_of_shots)
    x = [i for i in range(number_of_shots)]
    
    print(np.sum(mesures))

    plt.plot(x, mesures)
    plt.title("Graphique de test")
    plt.xlabel("Axe des x")
    plt.ylabel("Axe des y")
    plt.grid(True)
    plt.show()
            
            
            
#---------INPUTS----------                     
main(sys.argv[1])
#------------------------