import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 5, 2, 6])
N = len(x)
print(f"Length of x: {N}")

X = np.fft.fft(x)
n = np.arange(N)
print(x)