import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

z=sp.symbols('z')
x = [1,2,5,0,6,3]
Xz=sum(x[i]*z**(-i) for i in range(len(x)))
print(Xz.simplify())
Xz_pole=sp.together(Xz*z**(len(x)-1))
print(Xz_pole)
coffies=sp.Poly(Xz_pole,z).all_coeffs()
print(coffies)
coffies=[complex(i) for i in coffies]
print(coffies)
zeros=np.roots(coffies)
print(zeros)
pole=[0]*(len(x)-1)
print(pole)




plt.figure(figsize=(6,6))
plt.axhline(0,color='black')
plt.axvline(0,color='black')
plt.scatter(np.real(zeros),np.imag(zeros),color='black',marker='o',label='Zero')
plt.scatter(np.real(pole),np.imag(pole),color='red',marker='x',label='polses')
plt.xlabel('real')
plt.ylabel('imag')
plt.legend()



plt.show()