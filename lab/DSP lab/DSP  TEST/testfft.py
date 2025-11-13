import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,5,2,6])
N=len(x)
print(N)
n=np.arange(N)
X=np.fft.fft(x);
print(X)
plt.figure(figsize=(10,12))
plt.subplot(2,2,1)
plt.stem(n,x)
plt.title("Orginal")


plt.subplot(2,2,2)
plt.stem(n,abs(X))
plt.title('FFT')

plt.subplot(2,2,3)
plt.stem(n,np.angle(X),basefmt=' ')
plt.title('angle')
t=np.arange(N)



plt.figure(figsize=(10,10))
for k in range(N):
    cp=(1/N)*X[k]*np.exp(1j*2*np.pi*t*k/N)
    print('cp real ',cp.real)
    plt.subplot(N,1,k+1)
    plt.stem(n,cp.real,basefmt=' ')



plt.show()