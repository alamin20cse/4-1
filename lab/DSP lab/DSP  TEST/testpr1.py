import matplotlib.pyplot as plt
import numpy as np
n=np.arange(-10,11)
x=np.array([abs(i) if -3<=i<=3 else 0 for i in n])

def shift(x,n,shiftA):
    return np.array([x[n.tolist().index(k-shiftA)] if (k-shiftA) in n else 0 for k in n])

ya=x
yb=shift(x,n,1)
yc=shift(x,n,-1)
yd=(shift(x,n,1)+x+shift(x,n,-1))/3
ye=np.maximum.reduce([x,shift(x,n,1),shift(x,n,-1)])
yf=np.cumsum(x)

results=[ya,yb,yc,yd,ye,yf]
title=[
    'y(n)=x(n)',
    'y(n)=x(n+1)',
    'y(n)=x(n-1)',
    'y(n)=[x(n+1)+x(n-1)+x]/3',
    'y(n) = max(x(n+1), x(n), x(n - 1))',
    'y(n) = cumulative sum of x(k)',
]

fig,axs=plt.subplots(6,1,figsize=(10,15))

for i in range(6):
    axs[i].stem(n,results[i])

plt.show()