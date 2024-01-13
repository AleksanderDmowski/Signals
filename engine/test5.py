# Załóżmy, że sin_num to lista obiektów sin, a każdy obiekt sin ma zmienną value

if __name__ == '__main__': 
    from math_lib import Sinuosidal_wave
else:
    pass
    from .math_lib import Sinuosidal_wave

# Przykładowa klasa sin
class Sin:
    def __init__(self, value):
        self.value = value

# Przykładowa lista obiektów sin
sin_num = [Sin(3), Sin(7), Sin(5), Sin(2)]

Sin1=Sinuosidal_wave(frequency=2, amplitude=1, time=float(1), frequency_sampling=int(100), shift=0)
Sin2=Sinuosidal_wave(frequency=4, amplitude=2, time=float(1), frequency_sampling=int(100), shift=0)

sin_num2=[Sin1, Sin2]
# Znajdź największą wartość value
najwieksza_wartosc = max(sin_num, key=lambda x: x.value).value
najwieksza_wartosc2 = 

# Wyświetl wynik
print("Największa wartość value:", najwieksza_wartosc)
print("Największa wartość value:", najwieksza_wartosc2)