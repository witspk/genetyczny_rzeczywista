from populacja import ESelection, ECross, EMutation
from runner import runner;

# parametry ilosc populacji, wielkosc populacji, długosc chromosomu, prawdopodobienstwo krzyrzowania, prawdopodobienstwo mutacji, prawdopodobienstwo inwersji, wielkości przedziału

import time

start = time.time()
print("TEST 1 \n \
       wielkosc_populacji=100,\n \
       liczba_epok=1000,\n \
       rodzaj_selekcji=ESelection.BEST,\n \
       parametr_selekcji=10,\n \
       rodzaj_krzyzowania=ECross.ARITHMETIC,\n \
       p_krzyzowania=0.8,\n \
       rodzaj_mutacji=EMutation.UNIFORM,\n \
       p_mutacji=0.5,\n \
       liczba_elitarnych=5")
runner(wielkosc_populacji=100,
           liczba_epok=1000,
           rodzaj_selekcji=ESelection.BEST,
           parametr_selekcji=10,
           rodzaj_krzyzowania=ECross.ARITHMETIC,
           p_krzyzowania=0.8,
           rodzaj_mutacji=EMutation.UNIFORM,
           p_mutacji=0.5,
           liczba_elitarnych=5)
end = time.time()
print("Czas egzekucji algorytmu: "+ str(end-start))
start = time.time()
print("TEST 2 \n \
       wielkosc_populacji=100,\n \
       liczba_epok=100,\n \
       rodzaj_selekcji=ESelection.BEST,\n \
       parametr_selekcji=10,\n \
       rodzaj_krzyzowania=ECross.ARITHMETIC,\n \
       p_krzyzowania=0.9,\n \
       rodzaj_mutacji=EMutation.GAUSS,\n \
       p_mutacji=0.4,\n \
       liczba_elitarnych=2")
runner(wielkosc_populacji=100,
           liczba_epok=100,
           rodzaj_selekcji=ESelection.BEST,
           parametr_selekcji=10,
           rodzaj_krzyzowania=ECross.ARITHMETIC,
           p_krzyzowania=0.9,
           rodzaj_mutacji=EMutation.GAUSS,
           p_mutacji=0.4,
           liczba_elitarnych=2)
end = time.time()
print("Czas egzekucji algorytmu: "+ str(end-start))
start = time.time()
print("TEST 3 \n \
       wielkosc_populacji=10,\n \
       liczba_epok=10000,\n \
       rodzaj_selekcji=ESelection.ROULETTE,\n \
       parametr_selekcji=4,\n \
       rodzaj_krzyzowania=ECross.HEURISTIC,\n \
       p_krzyzowania=0.8,\n \
       rodzaj_mutacji=EMutation.GAUSS,\n \
       p_mutacji=0.5,\n \
       liczba_elitarnych=1")
runner(wielkosc_populacji=10,
           liczba_epok=10000,
           rodzaj_selekcji=ESelection.ROULETTE,
           parametr_selekcji=4,
           rodzaj_krzyzowania=ECross.HEURISTIC,
           p_krzyzowania=0.8,
           rodzaj_mutacji=EMutation.GAUSS,
           p_mutacji=0.5,
           liczba_elitarnych=1)
end = time.time()
print("Czas egzekucji algorytmu: "+ str(end-start))
start = time.time()
print("TEST 4 \n \
       wielkosc_populacji=1000,\n \
       liczba_epok=1000,\n \
       rodzaj_selekcji=ESelection.BEST,\n \
       parametr_selekcji=20,\n \
       rodzaj_krzyzowania=ECross.HEURISTIC,\n \
       p_krzyzowania=0.8,\n \
       rodzaj_mutacji=EMutation.UNIFORM,\n \
       p_mutacji=0.5,\n \
       liczba_elitarnych=2")
runner(wielkosc_populacji=1000,
           liczba_epok=1000,
           rodzaj_selekcji=ESelection.BEST,
           parametr_selekcji=20,
           rodzaj_krzyzowania=ECross.HEURISTIC,
           p_krzyzowania=0.8,
           rodzaj_mutacji=EMutation.UNIFORM,
           p_mutacji=0.5,
           liczba_elitarnych=2)
end = time.time()
print("Czas egzekucji algorytmu: "+ str(end-start))
start = time.time()
print("TEST 5 \n \
       wielkosc_populacji=1000,\n \
       liczba_epok=100,\n \
       rodzaj_selekcji=ESelection.ROULETTE,\n \
       parametr_selekcji=30,\n \
       rodzaj_krzyzowania=ECross.ARITHMETIC,\n \
       p_krzyzowania=0.4,\n \
       rodzaj_mutacji=EMutation.UNIFORM,\n \
       p_mutacji=0.2,\n \
       liczba_elitarnych=30")
runner(wielkosc_populacji=10000,
           liczba_epok=100,
           rodzaj_selekcji=ESelection.BEST,
           parametr_selekcji=30,
           rodzaj_krzyzowania=ECross.ARITHMETIC,
           p_krzyzowania=0.4,
           rodzaj_mutacji=EMutation.UNIFORM,
           p_mutacji=0.2,
           liczba_elitarnych=30)
end = time.time()
print("Czas egzekucji algorytmu: "+ str(end-start))


