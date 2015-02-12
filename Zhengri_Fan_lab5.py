import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

t_i = 0
t_f = 20
N = 100000000
dt = (t_f-t_i)/N

xIdn = 0
vIdn = 1
xvPlot = np.array([[None] * N ,[None] * N])

m = 0.1
g = 9.8
k = 3

x_0 = 0
v_0 = 0

xvPlot[xIdn,0] = x_0
xvPlot[vIdn,0] = v_0

for i in range(1, N):
    F = -m*g - k * xvPlot[xIdn,i - 1]
    a = F/m
    xvPlot[vIdn,i] = xvPlot[vIdn,i - 1] + a * dt
    xvPlot[xIdn,i] = xvPlot[xIdn,i - 1] + xvPlot[vIdn,i - 1] * dt
##    print((xvPlot[vIdn,i], xvPlot[xIdn,i]))

tArray = np.arange(t_i, t_f, dt)
plot1 = plt.plot(tArray, xvPlot[xIdn])
plot2 = plt.plot(tArray, xvPlot[vIdn])
plt.show()
