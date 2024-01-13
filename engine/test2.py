
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib import pyplot as plt, animation
import numpy as np

if __name__ == '__main__': 
    from math_lib import Sinuosidal_wave
else:
    pass
    from .math_lib import Sinuosidal_wave, Set_frequency_sampling, Set_time


Sin1=Sinuosidal_wave(frequency=3, amplitude=2, time=float(1), frequency_sampling=int(100), shift=0)



def f(x, a, b):
    return np.sin((x/b)+a)

def f2(x, y, a):
    return np.sin((x/y)+a)

def sin(amplitude,freq,sampling_interval_points,a):
    return (amplitude * np.sin(2*np.pi*freq*sampling_interval_points+a))

ts=0.1
t=1.0
x=np.arange(0,t,ts)
y=4

fig = plt.figure()

print('sina :',Sin1.value)


ax = fig.add_subplot(111)
Sin1b, = ax.plot(Sin1.sampling_interval_points, Sin1.value, linestyle='--',label='Sin1 wave traveling left')
# Sin2b, = ax.plot(sampling_interval_points, Sin2b, linestyle='--',label='Sin1 wave traveling left')
line1, = ax.plot(x, f(x,0,1), linestyle='--',label='sin wave traveling left')
# line1, = ax.plot(x, f2(x,1,0), linestyle='--',label='sin wave traveling left')
# line2, = ax.plot(x, f2(x,2,-1), linestyle='--',label='sin wave traveling right with b='+str(y))
plt.ion()

# fig.canvas.draw()
plt.show()
for a in np.arange(1,25,ts):
    Sin1b.set_ydata(Sin1.shift_update(a))
    # Sin2b.set_ydata(sin(2,3,sampling_interval_points,a))
    line1.set_ydata(f2(x,1,a))
#     # line2.set_ydata(f(x,-a,b))
#     # if(b>1):
#     #     b=b-0.1
    fig.canvas.draw()
    plt.legend(loc=1)
    plt.show()
    plt.pause(0.01)