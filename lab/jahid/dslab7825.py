x = [1, 2, 3]
h = [0, 0.5, 1]

n = len(x)
m = len(h)

conv_len = n + m - 1
conv = [0] * conv_len

for i in range(conv_len):
    for k in range(n):
        if 0 <= i - k < m:
            conv[n]