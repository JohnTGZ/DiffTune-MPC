#!/usr/bin/env python3

# Python implementation of Double_Integrator_System.m

from casadi import * 

def main():
    # Dimensions
    nx = 2 # Num states
    nu = 1 # Num inputs

    # Symbolic variables
    sym_x = SX.sym('x', nx, 1) # States
    sym_u = SX.sym('u', nu, 1) # Controls

    # Dynamics
    ## 1) Continuous time
    Ac = np.array([[0.0, 1.0], 
                   [0.0, -0.05]])
    # % 0.05 is the friction efficient, assumed to be proportional to velocity but in reverse direction
    print(Ac)

    Bc = np.array([[0.0], 
                   [1.0]])
    
    # 2) Discrete time
    Ts = 0.01 # Sampling time
    M = exp
    
if __name__ == '__main__':
    main()
   