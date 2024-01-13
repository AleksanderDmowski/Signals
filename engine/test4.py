import tkinter
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib import pyplot as plt, animation
import numpy as np

if __name__ == '__main__': 
    from math_lib import Sinuosidal_wave
else:
    pass
    from .math_lib import Sinuosidal_wave

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

root = tkinter.Tk()
root.wm_title("Embedding in Tk")

# plt.axes(xlim=(0, 1), ylim=(-2, 2))
fig = plt.Figure(dpi=100)
fig, ax = plt.subplots(figsize=(8, 6))
line, = ax.plot([], [], lw=2)

# ax.relim()
# update ax.viewLim using the new dataLim
ax.autoscale_view()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()

toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
toolbar.update()

canvas.mpl_connect(
    "key_press_event", lambda event: print(f"you pressed {event.key}"))
canvas.mpl_connect("key_press_event", key_press_handler)

button = tkinter.Button(master=root, text="Quit", command=root.quit)
button.pack(side=tkinter.BOTTOM)

toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

def init():
    line.set_data([], [])
    return line,

x1=Sinuosidal_wave(frequency=3, amplitude=2, time=float(1), frequency_sampling=int(1000), shift=0)

def animate(i):
    fs=100
    #przedział próbkowania uwzględniajacy częstoliwośc próbkowania
    ts = 1.0/fs
    t = np.arange(0,1,ts)
    #sinusioda dla częstoliwości 1 Hz i amplutudzie 3
    freq1 = 7
    x = np.linspace(0, 2, 1000)
    y = 0.5*np.sin(2 * np.pi * freq1*(x + 0.01 * i))
    ax.set_ylim(y.min()*1.1, y.max()*1.1)
    line.set_data(x, y)
    return line,
    
anim = animation.FuncAnimation(fig, animate, init_func=init,frames=200, interval=100, blit=True)

tkinter.mainloop()

