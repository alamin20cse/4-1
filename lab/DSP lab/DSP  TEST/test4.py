import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
z = sp.symbols('z')

x = [1,2,5,0,6,3]
Xz = sum(x[n] * z**(-n) for n in range(len(x)))

print(Xz)
Xz_poly = sp.together(Xz * z**(len(x)-1)).as_numer_denom()[0]
print(Xz_poly)
coeffs = sp.Poly(Xz_poly, z).all_coeffs()
coeffs = [complex(c) for c in coeffs]
print(coeffs)
zeros = np.roots(coeffs)
print('zeros : ',zeros)
poles = [0] * (len(x)-1)
print('poles : ',poles)



