import matplotlib.pyplot as plt
import numpy as np

# Define n
n = np.arange(-10, 11)

# Create x(n)
x = []
for i in n:
    if -3 <= i <= 3:
        x.append(abs(i))
    else:
        x.append(0)
x = np.array(x)

# Define shift function (simple loop version)
def shift(x, n, shift_amount):
    y = []
    for k in n:
        if (k - shift_amount) in n:
            idx = np.where(n == (k - shift_amount))[0][0]
            y.append(x[idx])
        else:
            y.append(0)
    return np.array(y)

# Different operations
y = x
yb = shift(x, n, 1)
yc = shift(x, n, -1)
yd = (shift(x, n, 1) + x + shift(x, n, -1)) / 3
ye = np.maximum.reduce([shift(x, n, 1), x, shift(x, n, -1)])
yf = np.cumsum(x)

# Plot
fig, axs = plt.subplots(6, 1, figsize=(10, 15))
titles = [
    '(a) y(n) = x(n)',
    '(b) y(n) = x(n - 1)',
    '(c) y(n) = x(n + 1)',
    '(d) y(n) = (1/3)[x(n+1) + x(n) + x(n - 1)]',
    '(e) y(n) = max(x(n+1), x(n), x(n - 1))',
    '(f) y(n) = cumulative sum of x(k)'
]
results = [y, yb, yc, yd, ye, yf]

for i in range(6):
    axs[i].stem(n, results[i], basefmt=" ")
    axs[i].set_ylabel("y(n)")
    axs[i].set_title(titles[i])
    axs[i].grid(True)

axs[-1].set_xlabel("n")
plt.tight_layout()
plt.show()
