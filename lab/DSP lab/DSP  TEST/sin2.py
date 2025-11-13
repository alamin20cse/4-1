import matplotlib.pyplot as plt
import numpy as np
ts=1/100
t=np.arange(0,1,ts)
f=1
x=2*np.sin(2*np.pi*f*t)
f=8
x+=22*np.sin(2*np.pi*f*t)
f=3
x=1*np.sin(2*np.pi*f*t)


plt.figure(figsize=(10,10))
plt.plot(t,x)



plt.show()