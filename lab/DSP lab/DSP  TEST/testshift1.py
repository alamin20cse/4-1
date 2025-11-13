import matplotlib.pyplot as plt
import numpy as np

n=np.arange(-10,10)
x=np.array([abs(i) if -3<=i<=3 else 0 for i in n])
print(x)

def shift(x,n,shift_amount):
    return np.array([x[n.tolist().index(k-shift_amount)]  if(k-shift_amount) in n else 0 for k in n])
ya=x
yb=shift(x,n,1)
yc=shift(x,n,-1)
yd=(1/3)*(shift(x,n,1)+x+shift(x,n,-1))
ye=np.maximum.reduce([shift(x,n,1),x,shift(x,n,-1)])
yf=np.cumsum(x)


resuts=[ya,yb,yc,yd,ye,yf]

titles=[
    'y(n)=x(n)',
    'y(n)=x(n+1)',
    'Y(n)=x(n-1)',
    'y(n)=(x(n+1)+x(n-1)+x(n))/3',
    'y(n)=max([shift(x,n,1),x,shift(x,n,-1)])',
    'y(n)=comelative sum of x(n)'
    
]

fig,axs=plt.subplots(6,1, figsize=(10,10))
for i in range(6):
    axs[i].stem(n,resuts[i])
    axs[i].set_title(titles[i])


plt.show()