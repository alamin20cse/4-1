import matplotlib.pyplot as plt
import numpy as np
ts=1/100
f=2
t=np.arange(0,1,ts)
x=22*np.sin(2*np.pi*f*t)

plt.plot(x)
plt.show()
