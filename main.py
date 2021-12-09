
from runner import runner;
from osobnik import Osobnik
from populacja import Populacja, ESelection, ECross, EMutation

# parametry ilosc populacji, wielkosc populacji, długosc chromosomu, prawdopodobienstwo krzyrzowania, prawdopodobienstwo mutacji, prawdopodobienstwo inwersji, wielkości przedziału

import time

start = time.time()
print("poczatek testu")
runner()

end = time.time()
print("Czas egzekucji algorytmu: "+ str(end-start))



