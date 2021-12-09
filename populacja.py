import random
from enum import Enum
from math import ceil, floor

from osobnik import Osobnik
from FitnessFunction import FitnessFunction
import copy


class ESelection(Enum):
    BEST = 1
    ROULETTE = 2
    TOURNAMENT = 3


class ECross(Enum):
    ARITHMETIC = 1
    HEURISTIC = 2


class EMutation(Enum):
    UNIFORM = 1
    GAUSS = 2


class Populacja:
    f = FitnessFunction()

    def __init__(self, *args):
        if len(args) > 0:
            n = args[0]

            if isinstance(n, int):
                self.population = []
                for x in range(n):
                    self.population.append(Osobnik(random.uniform(self.f.a, self.f.b),random.uniform(self.f.a, self.f.b)))
        else:
            self.population = []

    # wypisuje po pulacje na konsle do testów
    def print(self):
        print("Lp:chromo:Fitness")
        counter = 1

        for x in self.population:
            print(str(counter) + ":" + str(x.asString()) +  ":" + str(self.f.value(x.chromo[0],x.chromo[0])))
            counter = counter + 1

    def selekcja(self, rodzaj_selekcji, parametr_selekcji):
        if rodzaj_selekcji == ESelection.BEST:
            return self.best_number(parametr_selekcji)
        elif rodzaj_selekcji == ESelection.ROULETTE:
            return self.selekcja_kolem()
        elif rodzaj_selekcji == ESelection.TOURNAMENT:
            return self.selekcja_turniejowa(parametr_selekcji)
        else:
            pass

    def best_number(self, param):
        new_pop = Populacja()
        ranking = []
        for i in range(len(self.population)):
            decoded = self.population[i].chromo
            ranking.append((i, self.f.value(decoded[0],decoded[1])))
        ranking.sort(key=lambda x: x[1])
        for x in ranking[:int(param)]:
            new_pop.dodaj(self.population[x[0]])
        return new_pop

    def selekcja_kolem(self):
        new_pop = Populacja()
        przeliczone = []
        dystrybuantaSum = 0
        dystrybuanta = []

        # przelicznenie na decimal
        for x in range(len(self.population)):
            decoded = self.population[x].chromo
            przeliczone.append(self.f.value(decoded[0], decoded[1]))
        prawdopodobienstwo = []
        sumaOdwrotnosci = 0
        # Obliczamy sumę funkcji dopasowania wszystkich osobników
        for var in przeliczone:
            sumaOdwrotnosci = sumaOdwrotnosci + 1.00 / var
        # Obliczamy prawdopodobieństwo wyboru poszczególnych osobników
        prawdopodobienstwoSum = 0
        for var in przeliczone:
            prawdopodobienstwo.append((1 / var) / sumaOdwrotnosci)
            prawdopodobienstwoSum = prawdopodobienstwoSum + (1 / var) / sumaOdwrotnosci
        # Liczymy dystrubuante
        for var in prawdopodobienstwo:
            dystrybuanta.append(dystrybuantaSum + var)
            dystrybuantaSum = dystrybuantaSum + var
        # Teraz „kręcimy naszym kołem ruletki”. Losujemy liczby z zakresu [0,1].
        for i in range(0, floor(len(przeliczone) / 2)):
            wylosowana = random.random()
            roznicaNajmniejsza = 1

            for j in range(0, len(dystrybuanta) - 1):
                roznica = abs(abs(dystrybuanta[j]) - wylosowana)
                if (roznica < roznicaNajmniejsza):
                    roznicaNajmniejsza = roznica
                    dobranyOsobnik = j
            new_pop.dodaj(self.population[dobranyOsobnik+1])
        return new_pop

    def selekcja_turniejowa(self, k):
        new_pop = Populacja()
        group = []
        przeliczone = []
        for x in range(len(self.population)):
            decoded = self.population[x].chromo
            przeliczone.append(self.f.value(decoded[0], decoded[1]))

        indexList = list(range(len(self.population) - 1))
        for i in range(0, floor(len(przeliczone) / k)):
            if len(indexList) >= k:
                indexGroup = random.sample(indexList, k=int(k))
            else :
                indexGroup = indexList
            for var in indexGroup:
                group.append([var, przeliczone[var]])
                indexList.remove(var)
            groupWinner = min(group, key=lambda x: x[1])
            new_pop.dodaj(self.population[groupWinner[0]])
        return new_pop

    # helper dodaje  osobnika do populacji
    def dodaj(self, n):
        if isinstance(n, Osobnik):
            self.population.append(n)

    # krzyżuje osobniki aż powstanie cała populacja bez tych ze strateii elitarnej
    def krzyzowanie(self, rodzaj_krzyzowania, p_krzyzowania, ilosc_po_krzyżowaniu):
        if rodzaj_krzyzowania == ECross.ARITHMETIC:
            return self.krzyzowanie_arytmetyczne( p_krzyzowania, ilosc_po_krzyżowaniu)
        elif rodzaj_krzyzowania == ECross.HEURISTIC:
            return self.krzyzowanie_arytmetyczne( p_krzyzowania, ilosc_po_krzyżowaniu)
        else:
            pass

    def krzyzowanie_arytmetyczne(self, p_krzyzowania, ilosc_po_krzyżowaniu):
        new_pop = Populacja()
        new_pop += self
        for i in range(len(new_pop.population), ilosc_po_krzyżowaniu):
            new_pop.dodaj(Osobnik(1,1))
        return new_pop

    def krzyzowanie_heurystyczne(self, p_krzyzowania, ilosc_po_krzyżowaniu):
        new_pop = Populacja()
        new_pop += self
        for i in range(len(new_pop), ilosc_po_krzyżowaniu):
            new_pop.dodaj(Osobnik(1, 1))
        return new_pop



    def mutuj(self, rodzaj_mutacji, p_mutacji):
        if rodzaj_mutacji == EMutation.UNIFORM:
            return self.mutacja_rownomierna(p_mutacji)
        elif rodzaj_mutacji == EMutation.INDEX_CHANGE:
            return self.mutacja_zmiana(p_mutacji)
        elif rodzaj_mutacji == EMutation.GAUSS:
            return self.mutacja_gaussa(p_mutacji)
        else:
            pass

    def mutacja_rownomierna(self, p_mutacji):
        new_pop = Populacja()
        for x in self.population:
            # losowanie prawdopodobienstwa
            p = random.random()
            # mutowanie
            if p < p_mutacji:
                # losowanie punktu mutowania
                pp = random.random()
                if pp < 0.5:
                    o = Osobnik(random.uniform(self.f.a, self.f.b), x.chromo[1])
                else:
                    o = Osobnik(x.chromo[0], random.uniform(self.f.a, self.f.b))
                new_pop.dodaj(o)
            else:
                new_pop.dodaj(x)
        return new_pop

    def mutacja_gaussa(self, p_mutacji):
        new_pop = Populacja()
        new_pop += self
        return new_pop

    def nowa_epoka(self, rodzaj_selekcji, parametr_selekcji, rodzaj_krzyzowania, p_krzyzowania, rodzaj_mutacji, p_mutacji,
                   liczba_elitarnych):
        best_pop = self.best_number(liczba_elitarnych)
        ilosc_elit = len(best_pop.population)
        wielkosc_populacji = len(self.population)
        ilosc_po_krzyzowaniu = wielkosc_populacji - ilosc_elit
        new_pop = self \
            .selekcja(rodzaj_selekcji, parametr_selekcji) \
            .krzyzowanie(rodzaj_krzyzowania, p_krzyzowania, ilosc_po_krzyzowaniu) \
            .mutuj(rodzaj_mutacji, p_mutacji)
        return new_pop + best_pop

    def __add__(self, other):
        new_pop = copy.deepcopy(self)
        new_pop.population.extend(other.population)
        return new_pop







