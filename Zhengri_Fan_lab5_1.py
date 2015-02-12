import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import math

t_i = 0
t_f = 20
N = 100000
dt = (t_f-t_i)/N
tArray = np.arange(t_i, t_f, dt)



nArray = np.array([None] * N)
n_0 = 10000
nArray[0] = n_0

realValue = np.array([None] * N)
realValue[0] = n_0

lamda = 0.1

for i in range(1, N):
    dN = -lamda * nArray[i-1]
    nArray[i] = nArray[i-1] + dN * dt
    realValue[i] = n_0 * math.exp(-lamda * tArray[i])

##plot1 = plt.plot(tArray, nArray)
##plot2 = plt.plot(tArray, realValue)
plot3 = plt.plot(tArray, (realValue - nArray)/realValue)
plt.show()
