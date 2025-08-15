import numpy as np
import matplotlib.pyplot as plt

sr=100
t=sr/100;

f=1;
x=10*np.sin(np.pi*f*t)
plt.figure(figsize=(8,10))
plt.show()