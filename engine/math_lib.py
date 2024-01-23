import numpy as np

class Sinuosidal_wave():

    def __init__(self, frequency: int, amplitude: float, time: float, frequency_sampling: int, shift = int):
        self.frequency = frequency
        self.amplitude = amplitude
        self.frequency_sampling = frequency_sampling
        self.time_sampled = 1.0/self.frequency_sampling 
        self.time = time
        self.shift=shift
        self.samples = np.arange(0,self.time,self.time_sampled)
        self.value = self.amplitude * np.sin(2*np.pi*self.frequency*self.samples+self.shift)

    def shift_update(self, shift):
        self.shift = shift
        return self.amplitude * np.sin(2*np.pi*self.frequency*self.samples+self.shift)

    def create_value_for_anime(self, frame):
        self.frame= frame
        x = np.linspace(0, 2, self.frequency_sampling)
        # self.anime = np.linspace(0, self.time*2, self.time_sampled)
        # return self.amplitude * np.sin(2*np.pi*self.frequency*self.samples*self.anime+self.shift)
        if not frame:
            return self.amplitude * np.sin(2*np.pi*self.frequency*x+self.shift)
        return self.amplitude * np.sin(2*np.pi*self.frequency*(x+0.01*self.frame)+self.shift)
    # def update_time_sampled(self, shift):
    
    def create_wave(self):
        return self.amplitude * np.sin(2*np.pi*self.frequency*self.samples+self.shift)
