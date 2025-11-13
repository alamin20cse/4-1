import matplotlib.pyplot as plt
import numpy as np 
import sympy as sp

z=sp.symbols('z')
x = [1,2,5,0,6,3]

Xz=sum(x[k]*z**(-k) for k in range(len(x)))


print(Xz)

Xz_poly=sp.together(Xz*z**(len(x)-1)).as_numer_denom()[0]
print(Xz_poly)

coeffs=sp.poly(Xz_poly,z).all_coeffs()

print(coeffs)

coeffs=[complex(i) for i in coeffs]
print(coeffs)

zeros=np.roots(coeffs)
print(zeros)
poles=[0]*(len(x)-1)
print(poles)
plt.figure(figsize=(8,10))

plt.scatter(np.real(zeros),np.imag(zeros),marker='o')
plt.scatter(np.real(poles),np.imag(poles),marker='x')
plt.show()