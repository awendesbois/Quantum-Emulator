import numpy as np
import math
import copy

        
        
class System:
    def __init__(self, n):
        self.n = n
        
        #List of the state in binary
        self.states = [list('0' * (n - len(bin(i)[2:])) + bin(i)[2:]) for i in range(2**n)]
        
        #List of the amplitude of each state
        self.amplitudes = np.zeros(shape=(2**n,1)) + 0j        
        if n !=0 : self.amplitudes[0][0] = 1 + 0j  
        
        self.phase = np.zeros(shape=(2**n,1))
    
    def measure(self, number_shots):
        probas_normalised = np.abs(self.amplitudes)**2 
        return np.random.choice(len(self.amplitudes), p=probas_normalised.flatten(), size=number_shots)
    
    def printSyst(self):
        print("STATE OF SYSTEM: --------------------------")
        print(f"n: {self.n}")
        for i in range(len(self.states)):
            state = ""
            for q in self.states[i]: state += q
            print(f"State: |{state}> - Amplitude: {self.amplitudes[i]} - Phase: {self.phase[i]}")
        print("----------------------------------------")
    
    def execute_gate(self, doorname, door, target, phase=False):
        print(f"\nApplying {doorname} gate to qubit {target}:")
        I2 = np.eye(2)
        if target == 0: res = door
        else: res = I2
        for k in range(1, self.n):
            if k == target:
                res = np.kron(door,res)
            else:
                res = np.kron(I2,res)

        if phase:
            self.phase = res@self.phase
        else:
            self.amplitudes = res@self.amplitudes
        
        
    def execute_Cgate(self, doorname, door, controls, target):
        print(f"Applying C{doorname} gate from qubit {controls} to qubit {target}")
        P0 = np.array([[1, 0],[0, 0]])
        P1 = np.array([[0, 0],[0, 1]])
        I2 = np.eye(2)
        res = np.zeros(2**self.n)

        control = controls[0]
        
        #Case P0
        if control == 0: res1 = P0
        else: res1 = I2
        
        for k in range(1, self.n):
            if k == control:
                res1 = np.kron(res1, P0)
            else:
                res1 = np.kron(res1, I2)

        
        #Case P1

        if target == 0: res2 = door
        elif control == 0: res2 = P1
        else: res2 = I2   
            
        for k in range(1, self.n):
            if k == target:
                res2 = np.kron(res2, door)
            elif k == control:
                res2 = np.kron(res2, P1)
            else:
                res2 = np.kron(res2, I2)
                    
        res = res1 + res2

        self.amplitudes = res@self.amplitudes 
        
        #Problem for multiple controled Qbits 
        
            
    def execute_h(self, target):
        H2 = 1/math.sqrt(2) * np.array([[1, 1],[1, -1]])
        self.execute_gate('H', H2, target)   
        
    def execute_x(self, target):
        X = np.array([[0, 1],[1, 0]])
        self.execute_gate('X', X, target) 
    
    def execute_y(self, target):
        Y = np.array([[0, 0 - 1j],[0 + 1j, 0]])
        self.execute_gate('Y', Y, target)
        
    def execute_z(self, target):
        Z = np.array([[1, 0],[0, -1]])
        self.execute_gate('Z', Z, target) 

    #In "ncgate" fonction we use only the first control qubit of the list
    def execute_ncx(self, controls, target):
        X = np.array([[0 ,1], [1, 0]])
        self.execute_Cgate('X', X, controls, target)
        
    def execute_ncy(self, controls, target):
        Y = np.array([[0, 0 - 1j],[0 + 1j, 0]])
        self.execute_Cgate('Y', Y, controls, target)
        
    def execute_ncz(self, controls, target):
        Z = np.array([[1, 0],[0, -1]])
        self.execute_Cgate('Z', Z, controls, target)
        
    # Portes de rotation: A travailler
    def execute_rphase(self, target, angle):
        R = np.array([[1, 0],[0, np.exp(1j*angle)]])
        self.execute_gate('R', R, target, True)