from pylab import *
import numpy as np
ion()


##for i in range(10):
##    plot(np.random.rand(10))
##    draw()

omega = 2
k = 1

k1 = .5
omega1 = 4

def first_wave (x,t):
    return cos(k*x-omega*t)

def second_wave (x,t):
    return cos(k1*x-omega1*t)

x=arange(0,100,0.01)
traveling_wave, = plot(x, first_wave(x,0) + second_wave(x,0))
#traveling_wave2, = plot(x, second_wave(x,0))
t = 0
dt = 0.01
while t < 1000:
    traveling_wave.set_ydata(first_wave(x,t) + second_wave(x,t))
    #traveling_wave2.set_ydata(second_wave(x,t))
    t += dt
    draw()
