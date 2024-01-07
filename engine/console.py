import sys
import tkinter as tk
from tkinter import ttk
import numpy as np


if __name__ == '__main__': 
    pass
    from math_lib import Create_sinuosidal_wave, Set_frequency_sampling, Set_time
else:
    pass
    from .math_lib import Create_sinuosidal_wave, Set_frequency_sampling, Set_time

import matplotlib.pyplot as plt
# from matplotlib import animation
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class SignalsGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Sinusoidal Wave Generator")
        # self.table = tk.Frame(self.root)

        # Utwórz lewą i prawą ramkę
        self.left_frame = tk.Frame(self.root)
        self.left_frame.grid(row=0, column=0, padx=(0, 10), sticky="nsew")

        self.right_frame = tk.Frame(self.root)
        self.right_frame.grid(row=0, column=1, sticky="nsew")

        # Ustaw proporcje dla kolumn, aby lewa i prawa ramka miały odpowiednie rozmiary
        # self.root.columnconfigure(0, weight=1)
        # self.root.columnconfigure(1, weight=1)

        self.create_widgets()

        self.root.protocol("WM_DELETE_WINDOW", self.close_window)

    def create_widgets(self):
        # Label i Entry dla czasu
        tk.Label(self.left_frame, text="Time [s]:").grid(row=0, column=0)
        self.time_entry = tk.Entry(self.left_frame)
        self.time_entry.grid(row=0, column=1)
        self.time_entry.insert(0, 1.0)
    
        # Label i Entry dla częstotliwości próbkowania
        tk.Label(self.left_frame, text="Frequency Sampling:").grid(row=1, column=0)
        self.freq_sampling_entry = tk.Entry(self.left_frame)
        self.freq_sampling_entry.grid(row=1, column=1)
        self.freq_sampling_entry.insert(0, 100)
        # Przycisk do dodawania nowych linijek
        ttk.Button(self.left_frame, text="Add sinusoid", command=self.add_line).grid(row=2, column=0, columnspan=1, sticky="ew")
        ttk.Button(self.left_frame, text="Remove last sinusoid", command=self.remove_line).grid(row=2, column=1, columnspan=1, sticky="ew")
        ttk.Button(self.left_frame, text="Generate plot", command=self.button_to_generate_plot).grid(row=2, column=2, columnspan=2, sticky="ew")

        # Bazowa linijka
        self.add_line()

        # Inicjalizacja wykresu Matplotlib
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.line, = self.ax.plot([], [], lw=2)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.right_frame)  # Stwórz widżet Matplotlib Canvas
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(column=4, columnspan=4, sticky="nsew")

        # Inicjalizacja animacji
        # self.anim = FuncAnimation(self.fig, self.update_plot, init_func=self.init_plot, blit=False)


    def add_line(self):
        # Label i Entry dla częstotliwości i amplitudy
        row_num = (len(self.left_frame.grid_slaves())//4)+3 # Odczytaj aktualną ilość linijek
        tk.Label(self.left_frame, text=f"Frequency {row_num-3}:").grid(row=row_num, column=0)
        self.freq_entry = tk.Entry(self.left_frame)
        self.freq_entry.grid(row=row_num, column=1)
        self.freq_entry.insert(0, 0)

        tk.Label(self.left_frame, text=f"Amplitude {row_num-3}:").grid(row=row_num, column=2)
        self.amp_entry = tk.Entry(self.left_frame)
        self.amp_entry.grid(row=row_num, column=3)
        self.amp_entry.insert(0, 1)

        
    def remove_line(self):
        # Usuń ostatnią linijkę (Frequency i Amplitude)
        last_line = len(self.left_frame.grid_slaves())
        [self.left_frame.grid_slaves()[0].destroy() for _ in range(4)  if last_line > 11]


    def generate_plot_data(self):
        self.frequencies = [int(float(entry.get())) for entry in self.left_frame.grid_slaves() if isinstance(entry, tk.Entry) and entry.grid_info()['column'] == 1][:-2][::-1]
        self.amplitudes = [float(entry.get()) for entry in self.left_frame.grid_slaves() if isinstance(entry, tk.Entry) and entry.grid_info()['column'] == 3][::-1]
        self.get_time = self.time_entry.get()
        self.get_fs = self.freq_sampling_entry.get()
 

    def create_plot(self):
        self.frequency_sampling=Set_frequency_sampling(frequency_sampling=self.get_fs)
        time=Set_time(time=self.get_time)
        self.sin_list=[Create_sinuosidal_wave(frequency=self.frequencies[n], amplitude=self.amplitudes[n], time=float(time.t), frequency_sampling=int(self.frequency_sampling.fs)) for n in range(len( self.frequencies))]
        self.sin_sum=sum([sin_instance.value for sin_instance  in self.sin_list])

        self.ax.clear()  # Wyczyść poprzednią zawartość wykresu
        self.ax.plot(self.sin_list[0].sampling_interval_points, self.sin_sum, 'r')
        self.ax.set_ylabel('Amplitude')
        self.canvas.draw()


    # initialization function: plot the background of each frame
    # def anime_init(self):
    #     self.line.set_data([], [])
    #     return self.line,

    # animation function.  This is called sequentially
    # def animate(self):
    #     x = np.linspace(0, max([sin_instance.amplitude for sin_instance  in self.sin_list]), self.sin_list[0].sampling_interval_points)
    #     y =  self.sin_sum
    #     self.line.set_data(x, y)
    #     return self.line


    # call the animator.  blit=True means only re-draw the parts that have changed.
    def run_anime(self):
        anime = FuncAnimation(self.fig, self.animate, init_func=self.anime_init, frames=200, interval=20, blit=True) 
        plt.show()

    def button_to_generate_plot(self):
        self.generate_plot_data()
        self.create_plot()
        # self.run_anime()

    def run(self):
        self.root.mainloop()
    
    def close_window(self):
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()  # Zniszczenie głównego okna
            sys.exit()


def app():
    return SignalsGUI(tk.Tk())

if __name__ == '__main__':
    app().run()
 