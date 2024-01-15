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

# plt.rcParams["figure.figsize"] = [7.00, 3.50]
# plt.rcParams["figure.autolayout"] = True

root = tkinter.Tk()
root.wm_title("Embedding in Tk")

def set_sinusoids_exec(num_sin):
    lines = []

    for idx in range(num_sin - 1):
        line, = ax.plot([], [], lw=2, label=f'Sinusoida {idx + 1}', color='gray', linestyle='-', alpha=0.5)
        lines.append(line)

    line, = ax.plot([], [], lw=2, label='Sinusoida Sun', color='red')
    lines.append(line)

    ax.legend()
    return lines

def init_base_exec(lines):
    # print('press me')
    # wait()
    for line in lines:
        line.set_data([], [])
    return lines

# plt.axes(xlim=(0, 1), ylim=(-2, 2))
fig = plt.Figure(dpi=100)
ax = fig.add_subplot(xlim=(0, 1), ylim=(-1, 1))
# ax = fig.add_subplot(xlim=(0, 1), ylim=(-1, 1))


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


frq=100

Sin1=Sinuosidal_wave(frequency=1, amplitude=1, time=float(1), frequency_sampling=int(frq), shift=0)
Sin2=Sinuosidal_wave(frequency=2, amplitude=1, time=float(1), frequency_sampling=int(frq), shift=0)
SinSum=Sin1.value+Sin1.value
# Sin3=Sinuosidal_wave(frequency=3, amplitude=2, time=float(1), frequency_sampling=int(100), shift=0)
# Sin4=Sinuosidal_wave(frequency=4, amplitude=3, time=float(1), frequency_sampling=int(100), shift=0)
# Sin5=Sinuosidal_wave(frequency=5, amplitude=4, time=float(1), frequency_sampling=int(100), shift=0)


sin_list=[Sin1,Sin2]
# sin_num2=[Sin1, Sin2, Sin3, Sin4, Sin5]
sin_list_values=[sinusoid.value for sinusoid in sin_list]
sin_list_values.append(sum([sin.create_value_for_anime(False) for sin in sin_list]))
sin_list.append(sum([sin.create_value_for_anime(False) for sin in sin_list]))

sinusoids = set_sinusoids_exec(len(sin_list_values))
init_base_exec(sinusoids)
ax.set_ylim(min([value for sin in sin_list_values for value in sin])*1.5, max([value for sin in sin_list_values for value in sin])*1.5)

fig, ax = plt.subplots()

x = np.linspace(0, 0.95, frq)

def baseanimate(frame, lines, num_sin):

    return_value = []
    sum_of_elemnts=0

    for id_of_element, line in enumerate(lines):
        try:
            y = sin_list[id_of_element].create_value_for_anime(frame)
            sum_of_elemnts+=y
            line.set_data(x,y)
            return_value.append(line)
        except AttributeError:
            line.set_data(x, sum_of_elemnts)
            return_value.append(line)
    return return_value


anim = animation.FuncAnimation(fig, baseanimate, init_func=lambda: init_base_exec(sinusoids), fargs=(sinusoids, sin_list_values), frames=200, interval=100, blit=True)

tkinter.mainloop()

