import numpy as np

# x = np.array([1, 2, 3])
# h = np.array([0, 0.5, 1])
N=4
# # -------------------------
# # Manual Convolution
# # -------------------------
# # h কে উল্টে নিতে হবে
# h_flipped = h[::-1]

# # full mode length = len(x) + len(h) - 1
# n = len(x) + len(h) - 1
# conv_result = np.zeros(n)
# print(conv_result)

t = np.arange(N)

for k in range(N):
    print(k,k*t)
    