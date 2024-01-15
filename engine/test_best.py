import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

if __name__ == '__main__': 
    from math_lib import Sinuosidal_wave
else:
    pass
    from .math_lib import Sinuosidal_wave

import msvcrt as m
def wait():
    m.getch()

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


# sin_list_values.append(sinsum)
# sin_list.append(sinsum)

fig, ax = plt.subplots()

def set_sinusoids_exec(num_sin):
    lines = []

    for idx in range(num_sin - 1):
        line, = ax.plot([], [], lw=2, label=f'Sinusoida {idx + 1}', color='gray', linestyle='-', alpha=0.5)
        lines.append(line)

    line, = ax.plot([], [], lw=2, label='Sinusoida Sun', color='red')
    lines.append(line)

    return lines

def init_base_exec(lines):
    # print('press me')
    # wait()
    for line in lines:
        line.set_data([], [])
    return lines

ax.set_xlim(0,1)
x = np.linspace(0, 0.95, frq)

def baseanimate(frame, lines, num_sin):
    print('im frame ', frame)
    # wait()

    
    return_value = []
    sum_of_elemnts=0

    for id_of_element, line in enumerate(lines):
        print(id_of_element)
        wait()
        try:
            y = sin_list[id_of_element].create_value_for_anime(frame)
            sum_of_elemnts+=y
            line.set_data(x,y)
            return_value.append(line)
        except AttributeError:
            line.set_data(x, sum_of_elemnts)
            return_value.append(line)
        
    return return_value

ax.set_ylim(min([value for sin in sin_list_values for value in sin])*1.5, max([value for sin in sin_list_values for value in sin])*1.5)
sinusoids = set_sinusoids_exec(len(sin_list_values))
# init_base_exec(sinusoids)

anim = animation.FuncAnimation(fig, baseanimate, init_func=lambda: init_base_exec(sinusoids), fargs=(sinusoids, sin_list_values), frames=200, interval=100, blit=True)

plt.legend()
plt.show()
