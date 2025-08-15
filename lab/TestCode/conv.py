import numpy as np
from scipy.signal import correlate,convolve

x = np.array([1, 2, 3])
h = np.array([0, 0.5, 1])
conv=convolve(x,h)
cor=correlate(x,h)

print(conv)
print(cor)