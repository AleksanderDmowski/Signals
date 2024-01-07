import numpy as np


class Set_frequency_sampling:
    
    def __init__(self, frequency_sampling: int)-> None:
        self.fs= frequency_sampling
    
    def get_fs_value(self):
        return self.fs

class Set_time:

    def __init__(self, time: float)-> None:
        self.t= time
    
    def get_t_value(self):
        return self.t

class Create_sinuosidal_wave(Set_frequency_sampling, Set_time):

    def __init__(self, frequency: int, amplitude: float, frequency_sampling: int, time: float) -> None:
        self.freq = frequency
        self.amplitude = amplitude
        self.fs = frequency_sampling
        self.ts = 1.0/frequency_sampling
        self.t=time
        self.sampling_interval_points = np.arange(0,self.t,self.ts)
        self.value = self.amplitude * np.sin(2*np.pi*self.freq*self.sampling_interval_points)
        Set_time.__init__(self, time=time)
        Set_frequency_sampling.__init__(self, frequency_sampling=frequency_sampling)
       
    def get_sin_value(self):
        return self.amplitude * np.sin(2*np.pi*self.freq*self.t)