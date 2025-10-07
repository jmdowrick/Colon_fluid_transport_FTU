# Using Gawthrop's approach for converting between single channel conductance and maximum P for the GHK equation
import numpy as np

R = 0.008314472
T = 310.0
z = 1.0
F = 96.485
N_A = 6.023e8

Na_o = 145.0
Na_i = 15.0

E_Na = R*T/(z*F)*np.log(Na_o/Na_i)

gamma = 7.5

P_max = (2.0*R*T)/(pow(F, 2.0))*gamma*((1.0-np.exp(z*F*E_Na/(R*T)))/(Na_i-Na_o*np.exp(z*F*E_Na/(R*T))))

P_max_per_fmol = P_max*6.023e8

print(P_max_per_fmol)