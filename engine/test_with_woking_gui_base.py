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
# ax = fig.add_subplot(xlim=(0, 1), ylim=(-1, 1))
ax = fig.add_subplot(xlim=(0, 1), ylim=(-1, 1))
line1, = ax.plot([], [], lw=2, label='Sinusoida 1')
line2, = ax.plot([], [], lw=2, label='Sinusoida 2')

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
    print('dupa')
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

Sin1=Sinuosidal_wave(frequency=3, amplitude=2, time=float(1), frequency_sampling=int(1000), shift=0)

def animate(i):
    fs=1000
    #przedział próbkowania uwzględniajacy częstoliwośc próbkowania
    ts = 1.0/fs
    t = np.arange(0,1,ts)
    #sinusioda dla częstoliwości 1 Hz i amplutudzie 3
    freq1 = 2
    x = np.linspace(0, 2, 1000)
    x1 = 3*np.sin(2*np.pi*freq1*t*(x + 0.01 * i))
    x1 = 3*np.sin(2*np.pi*freq1*(x + 0.01 * i))
    y = 0.5*np.sin(2 * np.pi * freq1*(x + 0.01 * i))
    # line.set_data(x, Sin1.shift_update((x + 0.01 * i)))
    # ax.set_ylim(Sin1.shift_update((x + 0.01 * i)).min()*1.1, Sin1.shift_update((x + 0.01 * i)).max()*1.1)

    # line.set_data(x, y)
    ax.set_ylim(x1.min()*2, x1.max()*2)

    line1.set_data(x, x1)
    line2.set_data(x, y)
    # line.set_data(x, y)
    return line1, line2

anim = animation.FuncAnimation(fig, animate, init_func=init,frames=200, interval=100, blit=True)

tkinter.mainloop()