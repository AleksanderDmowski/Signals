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

# x:3
# for i in range(x):
frequency_sampling=200
Sin1=Sinuosidal_wave(frequency=2, amplitude=1, time=float(1), frequency_sampling=int(frequency_sampling), shift=0)
Sin2=Sinuosidal_wave(frequency=4, amplitude=2, time=float(1), frequency_sampling=int(frequency_sampling), shift=0)
Sin3=Sinuosidal_wave(frequency=6, amplitude=3, time=float(1), frequency_sampling=int(frequency_sampling), shift=0)

num_sin=[]
num_sin.append(Sin1)
num_sin.append(Sin2)
num_sin.append(Sin3)

sinsum=[sum(sin.value) for sin in num_sin]

base=True
if base:
    line1, = ax.plot([], [], lw=1.5, label='Sinusoida 1',color='gray',linestyle='-', alpha=0.5)
    line2, = ax.plot([], [], lw=1.5, label='Sinusoida 2',color='gray',linestyle='-', alpha=0.5)
    line3, = ax.plot([], [], lw=1.5, label='Sinusoida 3',color='gray',linestyle='-', alpha=0.5)
    lineSum, = ax.plot([], [], lw=2, label='Sinusoida Sun',color='red')    
    

def set_sinusoids(num_sin):
    lines = []
    for _ in range(len(num_sin)):
        line, = ax.plot([], [], lw=2, label=f'Sinusoida {_ + 1}')
        lines.append(line)
    return lines

def init_base():
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    lineSum.set_data([], [])
    return line1, line2, line3, lineSum

def init(num_sin):
    init_lines=[]
    for line in num_sin:
        init_lines.append(line.set_data([], []))

    return init_lines

def init_sinusoids(num_sin):
    init_lines = []
    for line in num_sin:
        init_lines.append(line.set_data([], []))
    return init_lines


list_sin=set_sinusoids(num_sin)

init_sin=init(list_sin)



def base_animate(i):
    x = np.linspace(0, 2, 100)

    # for sin in num_sin:
    #     init_sin[sin].set_data([x], [num_sin[sin.value]])

    
    for index, sin in enumerate(num_sin):
        list_sin[index].set_data(x, sin.value)


    ax.set_ylim(num_sin.value.min()*2, num_sin.value.max()*2)

    return init_sin


def baseanimate(i):
    # fs=100
    # # przedział próbkowania uwzględniajacy częstoliwośc próbkowania
    # ts = 1.0/fs
    # t = np.arange(0,1,ts)*2
    # #sinusioda dla częstoliwości 1 Hz i amplutudzie 3
    # freq1 = 2
    x = np.linspace(0, 2, frequency_sampling)
    # x1 = 3*np.sin(2*np.pi*freq1*t)
    # x2 = 3*np.sin(2*np.pi*freq1*(t + 0.01 * i))
    # y = 0.5*np.sin(2 * np.pi * freq1*(x + 0.01 * i))
    # line.set_data(x, Sin1.shift_update((x + 0.01 * i)))
    # ax.set_ylim(Sin1.shift_update((x + 0.01 * i)).min()*1.1, Sin1.shift_update((x + 0.01 * i)).max()*1.1)

    # line.set_data(x, y)
    # ax.set_ylim(y.min()*2, y.max()*2)
    rng = np.random.default_rng()
    r=rng.random()
    line1.set_data(x, Sin1.create_value_for_anime(i)*r)
    line2.set_data(x, Sin2.create_value_for_anime(i)*(r/2))
    line3.set_data(x, Sin3.create_value_for_anime(i)*(r**r))
    lineSum.set_data(x, (Sin1.create_value_for_anime(i)*r+Sin2.create_value_for_anime(i)*(r/2)+Sin3.create_value_for_anime(i)*(r**r)))

    # line1.set_data(x, x1)
    # line2.set_data(x, x2)
      
    ax.set_ylim(min([value for sin in num_sin for value in sin.value])*2, max([value for sin in num_sin for value in sin.value])*2)

    return line1, line2, line3, lineSum

if base:
    pass
    
anim = animation.FuncAnimation(fig, baseanimate, init_func=init_base,frames=100, interval=100, blit=True)

tkinter.mainloop()