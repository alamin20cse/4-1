import numpy as np

x = np.array([1, 2, 3])
h = np.array([0, 0.5, 1])

# flip h for convolution
h_flip = h[::-1]

# length of output = len(x) + len(h) - 1
N = len(x) + len(h) - 1
y_conv = np.zeros(N)

# convolution using loop
for n in range(N):
    for k in range(len(x)):
        if (n - k) >= 0 and (n - k) < len(h_flip):
            y_conv[n] += x[k] * h_flip[n - k]

print("Convolution result:", y_conv)


# # correlation using loop (no flip)
# y_corr = np.zeros(N)

# for n in range(N):
#     for k in range(len(x)):
#         if (n - k) >= 0 and (n - k) < len(h):
#             y_corr[n] += x[k] * h[n - k]

# print("Correlation result:", y_corr)
